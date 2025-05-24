'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *

class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.cell = None
        self.list_type = []
        self.current_cl = None
        self.current_access = None
    def init(self):
        mem = [
                Symbol("getInt",MType([],IntType()), CName("io", True)),
                Symbol("putIntLn",MType([IntType()],VoidType()), CName("io", True)),
                Symbol("putInt",MType([IntType()],VoidType()), CName("io", True)),
                Symbol("getFloat",MType([],FloatType()), CName("io", True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()), CName("io", True)),
                Symbol("putFloat",MType([FloatType()],VoidType()), CName("io", True)),
                Symbol("getBool",MType([],BoolType()), CName("io", True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()), CName("io", True)),
                Symbol("putBool",MType([BoolType()],VoidType()), CName("io", True)),
                Symbol("getString",MType([],StringType()), CName("io", True)),
                Symbol("putStringLn",MType([StringType()],VoidType()), CName("io", True)),
                Symbol("putString",MType([StringType()],VoidType()), CName("io", True)),
                Symbol("putLn",MType([],VoidType()), CName("io", True))
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self, class_name):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(class_name), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(class_name), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def emitObjectClinit(self, lst_decl, env):
        frame = Frame("<clinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        lst_assign = []
        for decl in lst_decl:
            if isinstance(decl, VarDecl):
                name = Id(decl.varName)
                typ = decl.varType
                value = decl.varInit
                if value is None:
                    value = self.default_value(typ)
                lst_assign += [Assign(name, value)]
            elif isinstance(decl, ConstDecl):
                name = Id(decl.conName)
                typ = decl.conType
                value = decl.iniExpr
                lst_assign += [Assign(name, value)]
        self.visit(Block(lst_assign), env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        get_lst_func = [Symbol(func.name, MType([par.parType for par in func.params], func.retType), CName(self.className, True)) for func in ast.decl if isinstance(func, FuncDecl)]
        self.list_function = c + get_lst_func
        env = {}
        env['env'] = [c]
        ###STRUCT###
        self.list_type = [decl for decl in ast.decl if isinstance(decl, StructType) or isinstance(decl, InterfaceType)]
        for struct in self.list_type:
            if isinstance(struct, StructType):
                struct.methods = [meth for meth in ast.decl if isinstance(meth, MethodDecl) and meth.recType.name == struct.name]
        ###ENDSTR###
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or isinstance(x, ConstDecl) else a, ast.decl, env)
        reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)
        # reduce(lambda a, x: self.visit(x, a), ast.decl, env)
        
        self.emitObjectInit(self.className)
        self.emitObjectClinit(ast.decl, env)
        self.emit.printout(self.emit.emitEPILOG())

        for cl in self.list_type:
            self.current_cl = cl
            self.emit = Emitter(self.path + '/' + cl.name + '.j')
            envi = {'env' : env['env']}
            self.visit(cl, envi)
            self.emit.printout(self.emit.emitEPILOG())
        return env

    ## TODO decl ------------------------------
    def visitFuncDecl(self, ast: FuncDecl, o):
        self.function = ast
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o):
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o

    def visitVarDecl(self, ast: VarDecl, o):
        name = ast.varName
        val = ast.varInit
        typ = ast.varType
        #case: var x int;
        check_arr_not_init = False
        if not val:
            if type(typ) is ArrayType:
                # check_arr_not_init = True
                val = typ
            else:
                val = self.default_value(typ)

        env = o.copy()
        env['frame'] = Frame("", VoidType()) 
        rhs_code, rhs_typ = self.visit(val, env)

        #case: var x = 0;
        if not typ: typ = rhs_typ
        if isinstance(typ, Id):
            typ = ClassType(typ.name)
        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(name, typ, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, typ, True, False, None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(name, typ, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, name, typ, frame.getStartLabel(), frame.getEndLabel(), frame)) 
            #need to revisit here, cause the previous is a imagine visit only to get the type, we need the code based on the frame here
            #pass the o here, not env -> need here is the rhs_code
            # o['isLeft'] = False

            rhs_code, rhs_typ = self.visit(val, o)
            if type(typ) is FloatType and type(rhs_typ) is IntType:
                rhs_code += self.emit.emitI2F(frame)
            self.emit.printout(rhs_code)
            self.emit.printout(self.emit.emitWRITEVAR(name, typ, index, frame))                    
        return o
    
    def visitFuncCall(self, ast: FuncCall, o):
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)
        env = o.copy()
        if o.get('stmt'):
            env["stmt"] = False
            [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o
        
        func_code = "".join([str(self.visit(x, env)[0]) for x in ast.args])
        func_code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])
        return func_code, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))

        for item in ast.member:
            if type(item) in [FuncCall, MethCall]:
                env["stmt"] = True
            else:
                env['stmt'] = False
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o
    
    def visitId(self, ast: Id, o):
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if not sym:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR('this', ClassType(self.current_cl.name), 0, o['frame']), ClassType(self.current_cl.name)
            return self.emit.emitREADVAR('this', ClassType(self.current_cl.name), 0, o['frame']), ClassType(self.current_cl.name)

        if o.get('isLeft'):
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                return self.emit.emitPUTSTATIC(f'{self.className}/{sym.name}', sym.mtype, o['frame']), sym.mtype    
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:         
            return self.emit.emitGETSTATIC(f'{self.className}/{sym.name}', sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o):
        # frame = o['frame']
        if isinstance(ast.lhs, Id):
            sym = next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]), None)
            if sym is None:
                imp_var = VarDecl(ast.lhs.name, None, ast.rhs)
                return self.visit(imp_var, o)
        # env = o.copy()
        o["stmt"] = False

        rhs, rhs_typ = None, None
        lhs, lhs_typ = None, None
        if isinstance(ast.lhs, FieldAccess):
            o['isLeft'] = True
            lhs, lhs_typ = self.visit(ast.lhs, o)
            o['isLeft'] = False
            rhs, rhs_typ = self.visit(ast.rhs, o)
        elif isinstance(ast.lhs, ArrayCell):
            o['isLeft'] = True
            lhs, lhs_typ = self.visit(ast.lhs, o)
            o['isLeft'] = False
            rhs, rhs_typ = self.visit(ast.rhs, o)
        else:
            o['isLeft'] = False
            rhs, rhs_typ = self.visit(ast.rhs, o)
            o['isLeft'] = True
            lhs, lhs_typ = self.visit(ast.lhs, o)
            o['isLeft'] = False
        if type(lhs_typ) is FloatType and type(rhs_typ) is IntType:
            rhs += self.emit.emitI2F(o['frame'])
        
        if isinstance(ast.lhs, FieldAccess):
            self.emit.printout(lhs)
            self.emit.printout(rhs)
            self.emit.printout(self.emit.emitPUTFIELD(f'{self.current_access}/{ast.lhs.field}', lhs_typ, o['frame']))
        elif isinstance(ast.lhs, ArrayCell): 
            self.emit.printout(lhs)
            self.emit.printout(rhs)
            self.emit.printout(self.emit.emitASTORE(lhs_typ, o['frame']))
        else:
            self.emit.printout(rhs)
            self.emit.printout(lhs)
        return o

    def visitReturn(self, ast: Return, o):
        if ast.expr:
            expr, expr_type = self.visit(ast.expr, o)
            self.emit.printout(expr)
            self.emit.printout(self.emit.emitRETURN(expr_type, o['frame']))
        else: self.emit.printout(self.emit.emitRETURN(VoidType(), o['frame']))
        return o

    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        # o['isLeft'] = True
        
        l, ltype = self.visit(ast.left, o)
        r, rtype = self.visit(ast.right, o)
        frame = o['frame']

        if isinstance(ltype, IntType) and isinstance(rtype, FloatType):
            l += self.emit.emitI2F(frame)
            ltype = FloatType()
        elif isinstance(ltype, FloatType) and isinstance(rtype, IntType):
            r += self.emit.emitI2F(frame)
            rtype = FloatType()
        binary_code = l + r
        ###for short circuit only###
        short_code = l
        if op == '&&':
            short_label = frame.getNewLabel()
            end_label = frame.getNewLabel()
            short_code += self.emit.emitIFEQ(short_label, frame)

            short_code += l
            short_code += r
            short_code += self.emit.emitANDOP(frame)
            short_code += self.emit.emitGOTO(end_label, frame)

            short_code += self.emit.emitLABEL(short_label, frame)
            short_code += self.emit.emitPUSHICONST('false', frame)

            short_code += self.emit.emitLABEL(end_label, frame)
            return short_code, BoolType()
        elif op == '||':
            short_label = frame.getNewLabel()
            end_label = frame.getNewLabel()
            short_code += self.emit.emitIFNE(short_label, frame)

            short_code += l
            short_code += r
            short_code += self.emit.emitOROP(frame)
            short_code += self.emit.emitGOTO(end_label, frame)

            short_code += self.emit.emitLABEL(short_label, frame)
            short_code += self.emit.emitPUSHICONST('true', frame)

            short_code += self.emit.emitLABEL(end_label, frame)
            return short_code, BoolType()        ############################
        if op in ['+', '-']:
            if isinstance(ltype, StringType):
                binary_code += self.emit.emitINVOKEVIRTUAL('java/lang/String/concat', MType([StringType()], StringType()), frame)
            else:
                binary_code += self.emit.emitADDOP(op, ltype, frame)
            return binary_code, ltype
        elif op in ['*', '/']:
            binary_code += self.emit.emitMULOP(op, ltype, frame)
            return binary_code, ltype
        elif op == '%':
            binary_code += self.emit.emitMOD(frame)
            return binary_code, IntType()
        elif op == '&&':
            binary_code += self.emit.emitANDOP(frame)
            return binary_code, BoolType()
        elif op == '||':
            binary_code += self.emit.emitOROP(frame)
            return binary_code, BoolType()
        else:
            if isinstance(ltype, StringType):
                binary_code += self.emit.emitINVOKEVIRTUAL('java/lang/String/compareTo', MType([StringType()], IntType()), frame)
                binary_code += self.emit.emitPUSHICONST(0, frame)+ self.emit.emitREOP(op, IntType(), frame)
            else:
                binary_code += self.emit.emitREOP(op, ltype, frame)
            return binary_code, BoolType()
              
    def visitUnaryOp(self, ast: UnaryOp, o):
        op = ast.op
        frame = o['frame']
        opr, opr_type = self.visit(ast.body, o)
        if op == '!':
            opr += self.emit.emitNOT(opr_type, frame)
        else: opr += self.emit.emitNEGOP(opr_type, frame)
        return opr, opr_type
    
    def visitIntLiteral(self, ast: IntLiteral, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()
    
    def visitFloatLiteral(self, ast: FloatLiteral, o):
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, o):
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()
    
    def visitArrayLiteral(self, ast: ArrayLiteral, o):
        array_code = self.travel_array_literal(ast.value, ast.eleType, ast.dimens, o)
        # array_type = self.visit(ArrayType(ast.dimens, ast.eleType))
        return array_code, ArrayType(ast.dimens, ast.eleType)
    
    def travel_array_literal(self, array_lst, eletype, dimens, o):
        frame = o['frame']
        array_code = self.emit.emitPUSHICONST(len(array_lst), frame)
        if not isinstance(array_lst[0], list):
            array_code += self.emit.emitNEWARRAY(eletype, frame)
            idx = 0 
            for ele in array_lst:
                array_code += self.emit.emitDUP(frame)
                array_code += self.emit.emitPUSHCONST(idx, IntType(), frame)
                array_code += self.visit(ele, o)[0]
                array_code += self.emit.emitASTORE(eletype, frame)
                idx += 1
            return array_code
        array_code += self.emit.emitANEWARRAY(ArrayType(dimens[0:len(dimens)-1], eletype), frame)
        idx = 0
        for lst in array_lst:
            array_code += self.emit.emitDUP(frame)
            array_code += self.emit.emitPUSHCONST(idx, IntType(), frame)
            array_code += self.travel_array_literal(lst, eletype, dimens[1:] ,o)
            array_code += self.emit.emitASTORE(StringType(), frame)
            idx += 1
        return array_code


    def visitArrayCell(self, ast: ArrayCell, o):
        env = o.copy()
        env['isLeft'] = False
        array_code, array_type = self.visit(ast.arr, env)

        frame = o['frame']
        cnt = 0
        for idx in ast.idx:
            array_code += self.visit(idx, env)[0]
            if (cnt != len(ast.idx) - 1):
                array_code += self.emit.emitALOAD(array_type, frame)
            cnt += 1

        return_type = None
        if len(ast.idx) == len(array_type.dimens):#case non-value type
            return_type = array_type.eleType
            if o.get('isLeft'): 
                self.cell = ast
                # env['frame'].push()
            else: array_code += self.emit.emitALOAD(return_type, frame)
        else:
            cell_len = len(ast.idx)
            return_type = ArrayType(array_type.dimens[cell_len:], array_type.eleType)
            if o.get('isLeft'): 
                self.cell = ast
                # env['frame'].push()

            else: array_code += self.emit.emitALOAD(return_type, frame)
        return array_code, return_type

    
    #use for case : var x [2]int; 
    def default_value(self, typ):
        # dim = array_type.dimens
        eletype = typ
        tmp = None
        if isinstance(eletype, IntType): tmp = IntLiteral(0)
        elif isinstance(eletype, FloatType): tmp = FloatLiteral(0.0)
        elif isinstance(eletype, BoolType): tmp = BooleanLiteral("false")
        elif isinstance(eletype, StringType): tmp = StringLiteral('\"\"')
        elif isinstance(eletype, ArrayType):
            def array_value(element_type, dim):
                if isinstance(dim[0], Id):
                    pass
                else: get_dimen = dim[0].value
                if len(dim) == 1:
                    return [self.default_value(element_type) for _ in range(get_dimen)]
                return [array_value(element_type, dim[1:]) for _ in range(get_dimen)]
            tmp = ArrayLiteral(eletype.dimens, eletype.eleType, array_value(eletype.eleType, eletype.dimens))
        elif isinstance(eletype, Id):
            # instance = self.lookup(eletype.name, self.list_type, lambda x: x.name)
            tmp = StructLiteral(eletype.name, [])
        return tmp
        
    def visitIf(self, ast: If, o):
        frame = o['frame']
        else_label = frame.getNewLabel()
        exit_label = frame.getNewLabel()

        expr, expr_typ = self.visit(ast.expr, o)
        self.emit.printout(expr)
        self.emit.printout(self.emit.emitIFFALSE(else_label, frame))
        
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(exit_label, frame))

        self.emit.printout(self.emit.emitLABEL(else_label, frame))
        if ast.elseStmt:
            self.visit(ast.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(exit_label, frame))
        return o
    
    def visitForBasic(self, ast: ForBasic, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        frame = env['frame']
        frame.enterLoop()
        start_label = frame.getNewLabel()
        break_label = frame.getBreakLabel()
        continue_label = frame.getContinueLabel()

        #enter loop
        self.emit.printout(self.emit.emitLABEL(start_label, frame))
        expr, expr_typ = self.visit(ast.cond, env)
        self.emit.printout(expr)

        self.emit.printout(self.emit.emitIFFALSE(break_label, frame))
        self.visit(ast.loop, env)

        self.emit.printout(self.emit.emitLABEL(continue_label, frame))
        self.emit.printout(self.emit.emitGOTO(start_label, frame))
        self.emit.printout(self.emit.emitLABEL(break_label, frame))
        frame.exitLoop()

        return o

    def visitForStep(self, ast: ForStep, o):
        env = o.copy()
        env['env'] = [[]] + env['env']
        frame = env['frame']
        frame.enterLoop()
        start_label = frame.getNewLabel()
        check_label = frame.getNewLabel()
        break_label = frame.getBreakLabel()
        continue_label = frame.getContinueLabel()

        #enter loop
        self.emit.printout(self.emit.emitLABEL(start_label, frame))
        self.visit(ast.init, env)

        self.emit.printout(self.emit.emitLABEL(check_label, frame))
        expr, expr_typ = self.visit(ast.cond, env)
        self.emit.printout(expr)

        self.emit.printout(self.emit.emitIFFALSE(break_label, frame))
        self.visit(ast.loop, env)

        #update
        self.emit.printout(self.emit.emitLABEL(continue_label, frame))
        self.visit(ast.upda, env)
        self.emit.printout(self.emit.emitGOTO(check_label, frame))
        self.emit.printout(self.emit.emitLABEL(break_label, frame))
        frame.exitLoop()

        return o
        
    def visitForEach(self, ast: ForEach, o):
        return o
    
    def visitContinue(self, ast: Continue, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o
    
    def visitBreak(self, ast: Break, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o
    
    def visitConstDecl(self, ast: ConstDecl, o):
        con_to_var = VarDecl(ast.conName, ast.conType, ast.iniExpr)
        return self.visit(con_to_var, o)
    
    def visitArrayType(self, ast: ArrayType, o):
        env = o.copy()
        env['isLeft'] = False
        code = reduce(lambda acc, ele: acc + self.visit(ele, env)[0], ast.dimens, '')
        code += self.emit.emitMULTIANEWARRAY(ast, len(ast.dimens), o['frame'])
        return code, ast
    

    def visitFieldAccess(self, ast: FieldAccess, o):
        env = o.copy()
        env['isLeft'] = False
        code_field, type_reiceiver = self.visit(ast.receiver, env)
        # o['frame'] = env['frame']
        accessed_struct = self.lookup(type_reiceiver.name, self.list_type, lambda x: x.name)
        accessed_field = self.lookup(ast.field, accessed_struct.elements, lambda x: x[0])
        # if o.get('isLeft'):
        #     code_field += self.emit.emitPUTFIELD(f'{type_reiceiver.name}/{ast.field}', accessed_field[1], o['frame'])
        # else:
        if not o.get('isLeft'):
            code_field += self.emit.emitGETFIELD(f'{type_reiceiver.name}/{ast.field}', accessed_field[1], o['frame'])
        else: self.current_access = type_reiceiver.name
        return code_field, accessed_field[1]

    def visitMethCall(self, ast: MethCall, o):
        env = o.copy()
        code_meth, type_reiceiver = self.visit(ast.receiver, env)
        accessed_type = self.lookup(type_reiceiver.name, self.list_type, lambda x: x.name)
        is_struct = False
        if isinstance(accessed_type, StructType):
            meth = next(filter(lambda x: x.fun.name == ast.metName, accessed_type.methods), None)
            sym = Symbol(meth.fun.name, MType([par.parType for par in meth.fun.params],meth.fun.retType), CName(accessed_type.name))
            is_struct = True
        elif isinstance(accessed_type, InterfaceType):
            meth = next(filter(lambda x: x.name == ast.metName, accessed_type.methods))
            sym = Symbol(meth.name, MType(meth.params, meth.retType), CName(accessed_type.name))
        
        if o.get('stmt'):
            env['stmt'] = False
            self.emit.printout(code_meth)
            [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
            if is_struct:
                self.emit.printout(self.emit.emitINVOKEVIRTUAL(f'{sym.value.value}/{ast.metName}', sym.mtype, env['frame']))
            else:
                self.emit.printout(self.emit.emitINVOKEINTERFACE(f'{sym.value.value}/{ast.metName}', sym.mtype, env['frame']))
            return o
        
        func_code = ''.join([self.visit(param, env)[0] for param in ast.args])
        code_meth += func_code
        code_meth += self.emit.emitINVOKEVIRTUAL(f'{sym.value.value}/{ast.metName}', sym.mtype, env['frame']) if is_struct else self.emit.emitINVOKEINTERFACE(f'{sym.value.value}/{ast.metName}', sym.mtype, env['frame'])
        return code_meth, sym.mtype.rettype

    def visitStructLiteral(self, ast: StructLiteral, o):
        # struct = self.lookup(ast.name, self.list_type, lambda x: x.name)
        code_literal = self.emit.emitNEW(ast.name, o['frame']) + self.emit.emitDUP(o['frame'])
        lst_type = []
        for ele in ast.elements:
            field, field_type = self.visit(ele[1], o)
            code_literal += field
            lst_type += [field_type]
        constructor_type = MType(lst_type, VoidType())
        code_literal += self.emit.emitINVOKESPECIAL(o['frame'], f'{ast.name}/<init>', constructor_type)
        return code_literal, Id(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o):
        return self.emit.emitPUSHNULL(o['frame']), Id('')

    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))
        for inter in self.list_type:
            if isinstance(inter, InterfaceType) and self.check_type(inter, ast, True):
                self.emit.printout(self.emit.emitIMPLEMENT(inter.name))
                # break
        
        for field in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(field[0], field[1], False, False, None))

        #struct <init>(params)
        self.visit(MethodDecl(None, None, FuncDecl('<init>', reduce(lambda acc, ele: acc + [ParamDecl(ele[0], ele[1])], ast.elements, []),
                                                            VoidType(), Block([Assign(FieldAccess(Id('this'), ele[0]), Id(ele[0])) for ele in ast.elements]))), o)
        #struct <init>()
        self.visit(MethodDecl(None, None, FuncDecl('<init>', [], VoidType(), Block([]))), o)

        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, o)

    def visitMethodDecl(self, ast: MethodDecl, o):
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType([i.parType for i in ast.fun.params], ast.fun.retType)
        env = o.copy()
        env['frame'] = frame

        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)

        this_idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR( this_idx, 'this', ClassType(self.current_cl.name), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if not ast.receiver:
            self.emit.printout(self.emit.emitREADVAR('this', ClassType(self.current_cl.name), this_idx, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        env['env'] = [[]] + env['env']
        env = reduce(lambda acc, ele: self.visit(ele, acc), ast.fun.params, env)

        self.visit(ast.fun.body, env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if isinstance(ast.fun.retType, VoidType):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java/lang/Object", True))
        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, o)

    def visitPrototype(self, ast: Prototype, o):
        frame = Frame(ast.name, ast.retType)
        self.emit.printout(self.emit.emitAMETHOD(ast.name, MType(ast.params, ast.retType), frame))
        # self.emit.printout(self.emit.emitENDMETHOD(frame))
        return o


    def check_type(self, lhs, rhs, flag):
        if isinstance(lhs, Id):
            lhs = self.lookup(lhs.name, self.list_type, lambda x: x.name)
        if isinstance(rhs, Id):
            rhs = self.lookup(rhs.name, self.list_type, lambda x: x.name)

        #case lhs is null and rhs is a Struct or Interface
        if lhs is None:
            return True
        
        #flag is just only for the case of the input is 2 struct and interface.
        if flag:
            if isinstance(lhs, InterfaceType) and isinstance(rhs, StructType):
                lhs_method = [Symbol(func.name, MType(func.params, func.retType), None) for func in  lhs.methods]
                rhs_method = [Symbol(func.fun.name, MType([p.parType for p in func.fun.params], func.fun.retType), None) for func in rhs.methods]
                for method in lhs_method:
                    res = self.lookup(method.name, rhs_method, lambda x: x.name)
                    if res is None: return False
                    if len(method.mtype.partype) != len(res.mtype.partype): return False
                    lst_param_check = []
                    for x, y in zip(method.mtype.partype, res.mtype.partype):
                        # if isinstance(x, Id) and isinstance(y, Id):
                        #     if x.name != y.name: return False
                        # if type(x) != type(y): return False
                        lst_param_check += [self.check_type(x, y, False)]
                    # if isinstance(method.mtype.rettype, Id) and isinstance(res.mtype.rettype, Id):
                    #     if method.mtype.rettype.name != res.mtype.rettype.name: return False
                    # if type(method.mtype.rettype) != type(res.mtype.rettype): return False
                    if not all(lst_param_check):
                        return False
                    if not self.check_type(method.mtype.rettype, res.mtype.rettype, False):
                        return False
                return True
            # elif isinstance(lhs, FloatType) and isinstance(rhs, IntType):
            #     return True
        
        if (isinstance(lhs, StructType) and isinstance(rhs, StructType)) or (isinstance(lhs, InterfaceType) and isinstance(rhs, InterfaceType)):
            return lhs.name == rhs.name
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            for x, y in zip(lhs.dimens, rhs.dimens):
                left_val = x.value
                right_val = y.value
                if left_val != right_val: return False

            if isinstance(lhs.eleType, Id) and isinstance(rhs.eleType, Id):
                return lhs.eleType.name == rhs.eleType.name
            if isinstance(lhs.eleType, FloatType) and isinstance(rhs.eleType, IntType):
                return True
            return type(lhs.eleType) == type(rhs.eleType)
        return type(lhs) == type(rhs)
