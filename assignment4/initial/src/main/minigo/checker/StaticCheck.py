"""
 * @author nhphung
 Dinh Ba Khanh - 2252323
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):
        
    
    def __init__(self,ast):
        self.ast = ast
        self.built_in_function = [
                Symbol("getInt",MType([],IntType())),
                Symbol("putIntLn",MType([IntType()],VoidType())),
                Symbol("putInt",MType([IntType()],VoidType())),
                Symbol("getFloat",MType([],FloatType())),
                Symbol("putFloatLn",MType([FloatType()],VoidType())),
                Symbol("putFloat",MType([FloatType()],VoidType())),
                Symbol("getBool",MType([],BoolType())),
                Symbol("putBoolLn",MType([BoolType()],VoidType())),
                Symbol("putBool",MType([BoolType()],VoidType())),
                Symbol("getString",MType([],StringType())),
                Symbol("putStringLn",MType([StringType()],VoidType())),
                Symbol("putString",MType([StringType()],VoidType())),
                Symbol("putLn",MType([],VoidType()))
        ]
        self.list_function = []
        self.list_field = []
        self.called_function = None
        self.list_struct = []
        self.list_interface = []

    
    def check(self):
        return self.visit(self.ast,[self.built_in_function])

    def check_type_param(self, lhs, rhs, c):
        if isinstance(lhs, Id):
            lhs = self.lookup(lhs.name, self.list_struct + self.list_interface, lambda x: x.name)
        if isinstance(rhs, Id):
            rhs = self.lookup(rhs.name, self.list_struct + self.list_interface, lambda x: x.name)

        if isinstance(rhs, NilLiteral):
            return True
        if (isinstance(lhs, StructType) and isinstance(rhs, StructType)) or (isinstance(lhs, InterfaceType) and isinstance(rhs, InterfaceType)):
            return lhs.name == rhs.name
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            for x, y in zip(lhs.dimens, rhs.dimens):
                left_val = self.get_val(x, c)
                right_val = self.get_val(y, c)
                if left_val != right_val: return False
            if isinstance(lhs.eleType, Id) and isinstance(rhs.eleType, Id):
                return lhs.eleType.name == rhs.eleType.name
            return type(lhs.eleType) == type(rhs.eleType)
        return type(lhs) == type(rhs)

    def check_type(self, lhs, rhs, flag, c):
        if isinstance(lhs, Id):
            lhs = self.lookup(lhs.name, self.list_struct + self.list_interface, lambda x: x.name)
        if isinstance(rhs, Id):
            rhs = self.lookup(rhs.name, self.list_struct + self.list_interface, lambda x: x.name)

        if isinstance(lhs, (StructType, InterfaceType)) and isinstance(rhs, NilLiteral):
            return True
        if flag:
            if isinstance(lhs, InterfaceType) and isinstance(rhs, StructType):
                lhs_method = [Symbol(func.name, MType(func.params, func.retType), None) for func in  lhs.methods]
                rhs_method = [Symbol(func.fun.name, MType([p.parType for p in func.fun.params], func.fun.retType), None) for func in rhs.methods]
                for method in lhs_method:
                    res = self.lookup(method.name, rhs_method, lambda x: x.name)
                    if res is None: return False
                    if len(method.mtype.partype) != len(res.mtype.partype): return False
                    for x, y in zip(method.mtype.partype, res.mtype.partype):
                        if isinstance(x, Id) and isinstance(y, Id):
                            if x.name != y.name: return False
                        if type(x) != type(y): return False
                    if isinstance(method.mtype.rettype, Id) and isinstance(res.mtype.rettype, Id):
                        if method.mtype.rettype.name != res.mtype.rettype.name: return False
                    if type(method.mtype.rettype) != type(res.mtype.rettype): return False
                return True
            elif isinstance(lhs, FloatType) and isinstance(rhs, IntType):
                return True
        
        if (isinstance(lhs, StructType) and isinstance(rhs, StructType)) or (isinstance(lhs, InterfaceType) and isinstance(rhs, InterfaceType)):
            return lhs.name == rhs.name
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            if len(lhs.dimens) != len(rhs.dimens):
                return False
            for x, y in zip(lhs.dimens, rhs.dimens):
                left_val = self.get_val(x, c)
                right_val = self.get_val(y, c)
                if left_val != right_val: return False

            if isinstance(lhs.eleType, Id) and isinstance(rhs.eleType, Id):
                return lhs.eleType.name == rhs.eleType.name
            if isinstance(lhs.eleType, FloatType) and isinstance(rhs.eleType, IntType):
                return True
            return type(lhs.eleType) == type(rhs.eleType)
        return type(lhs) == type(rhs)

    def get_val(self, expr, c):
        if isinstance(expr, Id): 
            get_sym = [i for l in c for i in l]
            fil = next(filter(lambda x: x.name == expr.name, get_sym), None)
            return self.get_val(fil.value, c)
        if isinstance(expr, (IntLiteral, FloatLiteral)):
            return expr.value
        elif isinstance(expr, BinaryOp):
            o = expr.op
            l = self.get_val(expr.left, c)
            r = self.get_val(expr.right, c)
            if o == '+': return l + r
            elif o == '-': return l - r
            elif o == '*': return l * r
            elif o == '/': return int(l / r)
            elif o == '%': return l % r
        elif isinstance(expr, UnaryOp):
            o = expr.op
            b = self.get_val(expr.body, c)
            if o == '-': return -b

    def check_arr_value(self, nested_list, c):
        if isinstance(nested_list, list):
            for ele in nested_list:
                if isinstance(ele, list): self.check_arr_value(ele, c)
                else: self.visit(ele, c)
        else:
            self.visit(nested_list, c)

    def visitProgram(self, ast: Program, c):
        #traverse first time to find Function, Struct, Interface
        self.list_function = reduce(lambda acc, ele: acc + [ele] if isinstance(ele, FuncDecl) else acc, ast.decl, [])
        self.list_struct = reduce(lambda acc, ele: acc + [ele] if isinstance(ele, StructType) else acc, ast.decl, [])
        self.list_interface = reduce(lambda acc, ele: acc + [ele] if isinstance(ele, InterfaceType) else acc, ast.decl, [])
        #traverse second time to record method and store into struct
        for decl in ast.decl:
            if isinstance(decl, MethodDecl):
                res = self.lookup(decl.recType.name, self.list_struct + self.list_interface, lambda x : x.name)
                if isinstance(res, StructType):
                    lst_method = res.methods
                    check_elem = self.lookup(decl.fun.name, res.elements, lambda x: x[0])
                    check_name = self.lookup(decl.fun.name, lst_method, lambda x: x.fun.name)
                    if (check_name is not None) or (check_elem is not None):
                        raise Redeclared(Method(), decl.fun.name)
                    lst_method += [decl]
                elif isinstance(res, StructType):
                    pass
        #traverse third time to do project
        c = [[]]
        c[0] += self.built_in_function
        reduce(lambda acc, ele: self.visit(ele, acc), ast.decl, c)

    def visitVarDecl(self, ast: VarDecl, c):
        nam = ast.varName
        lef_typ = ast.varType
        rig_typ = ast.varInit
        res = self.lookup(nam, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(), ast.varName)
        #Type
        if rig_typ is not None: rig_typ = self.visit(rig_typ, c)
        if lef_typ is None:
            if isinstance(rig_typ, StructType): rig_typ = Id(rig_typ.name)
            c[0] = [Symbol(ast.varName, rig_typ, None)] + c[0]
            return c
        elif rig_typ is None:
            c[0] = [Symbol(ast.varName, lef_typ, None)] + c[0]
            return c
        check = self.check_type(lef_typ, rig_typ, True, c)
        if not check:
            raise TypeMismatch(ast)
        
        c[0] = [Symbol(ast.varName, lef_typ, ast.varInit)] + c[0]
        return c

    def visitConstDecl(self, ast: ConstDecl, c):
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Constant(), ast.conName)

        rig_typ = self.visit(ast.iniExpr, c)
        if isinstance(rig_typ, NilLiteral):
            raise TypeMismatch(ast)
        c[0] = [Symbol(ast.conName, rig_typ, ast.iniExpr)] + c[0]
        return c
    

    def visitFuncDecl(self, ast: FuncDecl, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Function(), ast.name)
        
        func_scope = [[]] + c
        func_scope = reduce(lambda acc, ele: self.visit(ele, acc), ast.params ,func_scope)
        param_type = [item.mtype for item in func_scope[0]]
        self.called_function = ast
        self.visit(ast.body, func_scope)
        c[0] = [Symbol(ast.name, MType(param_type, ast.retType), None)] + c[0]
        return c

    def visitMethodDecl(self, ast: MethodDecl, c):
        func_scope = [[], [Symbol(ast.receiver, ast.recType, None)]] + c
        func_scope = reduce(lambda acc, ele: self.visit(ele, acc), ast.fun.params ,func_scope)
        self.called_function = ast
        self.visit(ast.fun.body, func_scope)
        return c
    
    def visitParamDecl(self, ast: ParamDecl, c):
        nam = ast.parName
        typ = ast.parType

        res = self.lookup(nam, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), nam)
        ret = Symbol(nam, typ, None)
        c[0] = [ret] + c[0]
        return c
    
    def visitStructType(self, ast: StructType, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)
        lst_field = []
        for field in ast.elements:
            check_field = self.lookup(field[0], lst_field, lambda x: x.name)
            if not check_field is None:
                raise Redeclared(Field(), field[0])
            lst_field += [Symbol(field[0],field[1],None)]
        c[0] = [Symbol(ast.name, Id(ast.name), 'type')] + c[0]
        return c

    def visitPrototype(self, ast: AST.Prototype, c):
        res = self.lookup(ast.name, c, lambda x: x.name)
        if res is not None:
            raise Redeclared(Prototype(), ast.name)
        ret = Symbol(ast.name, MType(ast.params, ast.retType), None)
        return [ret] + c
    
    def visitInterfaceType(self, ast: InterfaceType, c):
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if res is not None:
            raise Redeclared(Type(), ast.name)
        reduce(lambda acc, ele: self.visit(ele, acc), ast.methods, [])
        c[0] = [Symbol(ast.name, Id(ast.name), 'type')] + c[0]
        return c
    
    def visitForBasic(self, ast: ForBasic, c):
        get_cond = self.visit(ast.cond, c)
        if not isinstance(get_cond, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.loop, c)
        return c

    def visitForStep(self, ast: ForStep, c):
        check_cond_scope = [[]] + c
        get_init = self.visit(ast.init, check_cond_scope)
        get_cond = self.visit(ast.cond, get_init)
        if not isinstance(get_cond, BoolType):
            raise TypeMismatch(ast)
        for_block = Block([ast.init] + [ast.upda] + ast.loop.member)
        self.visit(for_block, c)
        return c

    def visitForEach(self, ast: ForEach, c):
        arr = self.visit(ast.arr, c)
        if not isinstance(arr, ArrayType):
            raise TypeMismatch(ast)
        index = ast.idx.name
        value = ast.value.name
        if c is None: raise Undeclared(Identifier(), ast.idx.name)
        get_sym = [i for l in c for i in l]
        check_idx = self.lookup(index, get_sym, lambda x: x.name)
        if check_idx is None: raise Undeclared(Identifier(), ast.idx.name)
        elif not isinstance(check_idx.mtype, IntType): raise TypeMismatch(ast)

        check_val = self.lookup(value, get_sym, lambda x: x.name)

        if check_val is None: raise Undeclared(Identifier(), ast.value.name)
        if isinstance(check_val.mtype, ArrayType):
            reduce_size_arr = ArrayType(arr.dimens[1:], arr.eleType)
            chec_typ_val = self.check_type_param(check_val.mtype, reduce_size_arr, c)
            if not chec_typ_val: raise TypeMismatch(ast)
        else:
            chec_typ_val = self.check_type_param(check_val.mtype, arr.eleType, c)
            if not chec_typ_val: raise TypeMismatch(ast)

        for_block = ast.loop
        self.visit(for_block, c)
        return c

    def visitBlock(self, ast: Block, c):
        block = ast.member
        locsco = [[]] + c
        for stmt in block:
            locsco = self.visit(stmt, locsco) if not isinstance(stmt, (FuncCall, MethCall)) else self.visit(stmt, (locsco, True))

    def visitFuncCall(self, ast:FuncCall, c):
        check_statement = False
        if isinstance(c, tuple):
            c = c[0]
            check_statement = True
        get_lst_symbol = [Symbol(func.name, MType([f.parType for f in func.params], func.retType), None) for func in self.list_function]
        res = self.lookup(ast.funName, get_lst_symbol + self.built_in_function, lambda x: x.name)
        #check shadowing

        get_sym = [i for l in c for i in l]
        fil = next(filter(lambda x: x.name == ast.funName, get_sym), None)
        if fil is not None:
            if not isinstance(fil.mtype, MType):
                raise Undeclared(Function(), ast.funName)
        if res is None:
            raise Undeclared(Function(), ast.funName)
        else:
            if len(res.mtype.partype) != len(ast.args):
                raise TypeMismatch(ast)
            for l, r in zip(res.mtype.partype, ast.args):
                r = self.visit(r, c)
                if not self.check_type_param(l, r, c):
                    raise TypeMismatch(ast)
            if check_statement and (not isinstance(res.mtype.rettype, VoidType)):
                raise TypeMismatch(ast)
            elif (not check_statement) and (isinstance(res.mtype.rettype, VoidType)):
                raise TypeMismatch(ast)
        if not check_statement:
            return res.mtype.rettype 
        return c
        
    def visitMethCall(self, ast:MethCall, c):
        check_statement = False
        if isinstance(c, tuple):
            c = c[0]
            check_statement = True
        
        rec = self.visit(ast.receiver, c)
        if not isinstance(rec, Id):
            raise TypeMismatch(ast)
        find_type = self.lookup(rec.name, self.list_struct + self.list_interface, lambda x : x.name)
        if find_type is None: raise Undeclared(Method(), ast.metName)
        res = self.lookup(ast.metName, find_type.methods, lambda x: x.fun.name if isinstance(find_type, StructType) else x.name)
        if res is None: raise Undeclared(Method(), ast.metName)
        else:
            res = Symbol(res.fun.name, MType([f.parType for f in res.fun.params], res.fun.retType), None) if isinstance(res, MethodDecl) else Symbol(res.name,MType(res.params, res.retType) , None)
            if len(res.mtype.partype) != len(ast.args):

                raise TypeMismatch(ast)
            for l, r in zip(res.mtype.partype, ast.args):
                r = self.visit(r, c)
                if not self.check_type_param(l, r, c):
                    raise TypeMismatch(ast)
            if check_statement and (not isinstance(res.mtype.rettype, VoidType)):
                raise TypeMismatch(ast)
            elif (not check_statement) and isinstance(res.mtype.rettype, VoidType):
                raise TypeMismatch(ast)
        if not check_statement:
            return res.mtype.rettype
        return c
    
    def visitId(self, ast:Id, c):
        if c is None: 
            raise Undeclared(Identifier(), ast.name)
        get_sym = [i for l in c for i in l]
        fil = next(filter(lambda x: x.name == ast.name, get_sym), None)
        if fil is None:
            raise Undeclared(Identifier(), ast.name)
        elif isinstance(fil.mtype, Id) and isinstance(fil.value, str):
            if fil.value == 'type': raise Undeclared(Identifier(), ast.name)
        get_id_type = fil.mtype
        return get_id_type
    
    def visitFieldAccess(self, ast:FieldAccess, c):
        rec = self.visit(ast.receiver, c)
        if isinstance(rec, Id):
            rec = self.lookup(rec.name, self.list_struct + self.list_interface, lambda x: x.name)
        if isinstance(rec, InterfaceType): raise TypeMismatch(ast)
        if not isinstance(rec, StructType): 
            raise TypeMismatch(ast)
        res = self.lookup(ast.field, rec.elements, lambda x: x[0])
        if res is None: raise Undeclared(Field(), ast.field)
        get_field_type = res[1]
        return get_field_type

    def visitIntType(self, ast, c):
        ret_type = ast
        return ret_type
    def visitFloatType(self, ast, c):
        ret_type = ast
        return ret_type
    def visitBoolType(self, ast, c):
        ret_type = ast
        return ret_type
    def visitStringType(self, ast, c):
        ret_type = ast
        return ret_type
    def visitVoidType(self, ast, c): 
        ret_type = ast
        return ret_type
    
    def visitArrayType(self, ast:ArrayType, c):
        get_dim = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.dimens, [])
        if not IntType() in get_dim:
            raise TypeMismatch(ast)
        return ast
    
    def visitAssign(self, ast:Assign, c):
        rhs = self.visit(ast.rhs, c)
        lhs = ast.lhs
        if isinstance(lhs, Id):
            try:
                lhs = self.visit(ast.lhs, c)
            except Undeclared as e:
                c[0] = [Symbol(e.n, rhs, ast.rhs)] + c[0]
                return c
        else:
            lhs = self.visit(ast.lhs, c)
        check_type = self.check_type(lhs, rhs, True, c)
        if not check_type:
            raise TypeMismatch(ast)
        return c
    
    def visitIf(self, ast, c):
        get_cond = self.visit(ast.expr, c)
        if not isinstance(get_cond, BoolType):
            raise TypeMismatch(ast)
        elif ast.elseStmt is not None:
            return self.visit(ast.elseStmt, c)
        return c
    
    def visitContinue(self, ast, c):
        ret_type = ast
        return ret_type
    def visitBreak(self, ast, c):
        ret_type = ast
        return ret_type

    def visitReturn(self, ast:Return, c):
        curr_type = self.called_function.retType if isinstance(self.called_function, FuncDecl) else self.called_function.fun.retType
        if isinstance(curr_type, VoidType):
            if ast.expr is not None: 
                expr = self.visit(ast.expr, c)
                if not isinstance(expr, VoidType):
                    raise TypeMismatch(ast)
            return c
        expr_type = self.visit(ast.expr, c)
        func_type = curr_type
        if isinstance(expr_type, Symbol):
            expr_type = expr_type.mtype
        if not self.check_type(expr_type, func_type, False, c):
            if isinstance(expr_type, NilLiteral): pass
            else: raise TypeMismatch(ast)
        return c
    
    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        op = ast.op
        if isinstance(left,Symbol):
            left = left.mtype
        if isinstance(right, Symbol):
            right = right.mtype
        if op == '+':
            if isinstance(left, StringType) and isinstance(right, StringType):
                return StringType()
            elif isinstance(left, IntType) and isinstance(right, IntType):
                return IntType()
            elif isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
                return FloatType()
            raise TypeMismatch(ast)
        elif op in ['-', '*', '/']:
            if isinstance(left, IntType) and isinstance(right, IntType):
                return IntType()
            elif isinstance(left, (IntType, FloatType)) and isinstance(right, (IntType, FloatType)):
                return FloatType()
            raise TypeMismatch(ast)
        elif op == '%':
            if isinstance(left, IntType) and isinstance(right, IntType):
                return IntType()
            raise TypeMismatch(ast)
        elif op in ['==', '!=', '<', '<=', '>', '>=']:
            if type(left) == type(right):
                return BoolType()
            raise TypeMismatch(ast)
        elif op in ['!', '||', '&&']:
            if isinstance(left, BoolType) and isinstance(right, BoolType):
                return BoolType()
            raise TypeMismatch(ast)
        
    def visitUnaryOp(self, ast, c):
        opr = self.visit(ast.body, c)
        op = ast.op
        if isinstance(opr, Symbol): opr = opr.mtype
        if op == '-':
            if isinstance(opr, IntType): return IntType()
            elif isinstance(opr, FloatType): return FloatType()
            raise TypeMismatch(ast)
        elif op == '!':
            if isinstance(opr, BoolType): return BoolType()
            raise TypeMismatch(ast)
        
    def visitArrayCell(self, ast:ArrayCell, c):
        arr = self.visit(ast.arr, c)
        if isinstance(arr, Symbol): arr = arr.mtype
        if not isinstance(arr, ArrayType):
            raise TypeMismatch(ast)
        
        lst_typ = reduce(lambda acc, ele: [self.visit(ele, c)] + acc, ast.idx, [])
        
        is_int = all(reduce(lambda acc, ele: acc + [isinstance(ele, IntType)], lst_typ, []))
        if not is_int:
            raise TypeMismatch(ast)
        
        if len(lst_typ) == len(arr.dimens):
            return arr.eleType
        elif len(lst_typ) < len(arr.dimens):
            diff = len(arr.dimens) - len(lst_typ)
            diff = len(arr.dimens) - diff
            ret_lst = arr.dimens[diff: ]
            return ArrayType(ret_lst, arr.eleType)
        
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, c):
        ret_type = IntType()
        return ret_type
    def visitFloatLiteral(self, ast, c):
        ret_type = FloatType()
        return ret_type
    def visitBooleanLiteral(self, ast, c):
        ret_type = BoolType()
        return ret_type
    def visitStringLiteral(self, ast, c):
        ret_type = StringType()
        return ret_type
    def visitNilLiteral(self, ast, c):
        ret_type = ast
        return ret_type

    def visitArrayLiteral(self, ast:ArrayLiteral, c):
        get_lst_val = ast.value
        self.check_arr_value(get_lst_val, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast:StructLiteral, c):
        for element in ast.elements:
            ele_typ = element[1]
            self.visit(ele_typ, c)
        name = ast.name
        res = self.lookup(name, self.list_struct, lambda x: x.name)
        if res is None:
            raise TypeMismatch(ast)
        return res