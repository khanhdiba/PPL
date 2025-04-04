import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """func main() {};"""
    #     expect = str(Program([FuncDecl("main",[],VoidType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """func main () {}; var x int ;"""
    #     expect = str(Program([FuncDecl("main",[],VoidType(),Block([])),VarDecl("x",IntType(),None)]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))
   
    """Var Declaration"""
    def test_001(self):
        input = """var x int ;"""
        expect = Program([VarDecl("x",IntType(),None)])
        self.assertTrue(TestAST.checkASTGen(input,str(expect),301))

    def test_002(self):
        input = """var x int = 1 ;"""
        expect = Program([VarDecl("x", IntType(), IntLiteral(1))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 302))
    
    def test_003(self):
        input = """var x string = true ;"""
        expect = Program([VarDecl("x", StringType(), BooleanLiteral(True))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 303))

    def test_004(self):
        input = """var x boolean = \"This is a text\" ;"""
        expect = Program([VarDecl("x", BoolType(), StringLiteral("\"This is a text\""))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 304))
    
    def test_005(self):
        input = """var x int ; var y float ; var z boolean ;"""
        expect = Program([VarDecl("x", IntType(), None),VarDecl("y", FloatType(), None), VarDecl("z", BoolType(), None)])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 305))

    def test_006(self):
        input = """
                var x = 0x11
                var y = 0b101

                """
        expect = Program([VarDecl("x",None, IntLiteral("0x11")), VarDecl("y",None,IntLiteral("0b101"))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 306))

    def test_007(self):
        input = """
                var y = nil ;
                var x ID = [2][3] arr {1,2,3} ;
                """
        expect = Program([VarDecl("y",None,NilLiteral()),VarDecl("x",Id("ID"),ArrayLiteral([IntLiteral(2),IntLiteral(3)],Id("arr"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 307))

    def test_008(self):
        input = """var people People = People{name : "John" };"""
        expect = Program([VarDecl("people", Id("People"), StructLiteral("People",[("name",StringLiteral("\"John\""))]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 308))

    def test_009(self):
        input = """var a = (1 + 2) ;"""
        expect = Program([VarDecl("a",None,BinaryOp("+",IntLiteral(1),IntLiteral(2)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 309))

    def test_010(self):
        input = """var a = a[1][2] ;"""
        expect = Program([VarDecl("a",None,ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 310))

    def test_011(self):
        input = """var x = -5;"""
        expect = Program([VarDecl("x", None, UnaryOp("-", IntLiteral(5)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 311))

    def test_012(self):
        input = """var x = !true;"""
        expect = Program([VarDecl("x", None, UnaryOp("!", BooleanLiteral(True)))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 312))

    def test_013(self):
        input = """var arr = arr[1][2][3];"""
        expect = Program([VarDecl("arr", None, ArrayCell(Id("arr"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 313))

    def test_014(self):
        input = """var a = 1 + 2 * 3 - 4 / 2;"""
        expect = Program([
            VarDecl("a", None, 
                    BinaryOp("-", 
                        BinaryOp("+", 
                            IntLiteral(1), 
                            BinaryOp("*", IntLiteral(2), IntLiteral(3))
                        ), 
                        BinaryOp("/", IntLiteral(4), IntLiteral(2))
                    )
            )
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 314))

    def test_015(self):
        input = """var point = Point{x: 1, y: 2};"""
        expect = Program([
            VarDecl("point", None, StructLiteral("Point", [
                ("x", IntLiteral(1)), 
                ("y", IntLiteral(2))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 315))

    def test_016(self):
        input = """var x = a.b.c;"""
        expect = Program([
            VarDecl("x", None, FieldAccess(FieldAccess(Id("a"), "b"), "c"))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 316))

    def test_017(self):
        input = """var f = x || 2;"""
        expect = Program([
            VarDecl("f", None, BinaryOp("||",Id("x"),IntLiteral(2)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 317))

    def test_018(self):
        input = """var condition = x > 10;"""
        expect = Program([
            VarDecl("condition", None, BinaryOp(">", Id("x"), IntLiteral(10)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 318))

    def test_019(self):
        input = """var sum = a + b * c;"""
        expect = Program([
            VarDecl("sum", None, BinaryOp("+", Id("a"), BinaryOp("*", Id("b"), Id("c"))))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 319))

    def test_020(self):
        input = """var flag = !is_valid;"""
        expect = Program([
            VarDecl("flag", None, UnaryOp("!", Id("is_valid")))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 320))

    def test_021(self):
        input = """const PI = 3.14;"""
        expect = Program([
            ConstDecl("PI", None, FloatLiteral(3.14))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 321))

    def test_022(self):
        input = """const GREETING = "Hello, world!";"""
        expect = Program([
            ConstDecl("GREETING", None, StringLiteral('"Hello, world!"'))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 322))

    def test_023(self):
        input = """const MAX_VALUE = 100;"""
        expect = Program([
            ConstDecl("MAX_VALUE", None, IntLiteral(100))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 323))

    def test_024(self):
        input = """const IS_ACTIVE = true;"""
        expect = Program([
            ConstDecl("IS_ACTIVE", None, BooleanLiteral(True))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 324))

    def test_025(self):
        input = """const NEGATIVE_ONE = -1;"""
        expect = Program([
            ConstDecl("NEGATIVE_ONE", None, UnaryOp("-", IntLiteral(1)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 325))

    def test_026(self):
        input = """const SMALL_NUMBER = 1.2e-3;"""
        expect = Program([
            ConstDecl("SMALL_NUMBER", None, FloatLiteral("1.2e-3"))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 326))

    def test_027(self):
        input = """const ARR = arr[1][2][3];"""
        expect = Program([
            ConstDecl("ARR", None, ArrayCell(Id("arr"), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 327))

    def test_028(self):
        input = """const COLOR = "red";"""
        expect = Program([
            ConstDecl("COLOR", None, StringLiteral('"red"'))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 328))

    def test_029(self):
        input = """const HALF_PI = PI / 2;"""
        expect = Program([
            ConstDecl("HALF_PI", None, BinaryOp("/", Id("PI"), IntLiteral(2)))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 329))

    def test_030(self):
        input = """const MESSAGE = GREETING + " How are you?";"""
        expect = Program([
            ConstDecl("MESSAGE", None, BinaryOp("+", Id("GREETING"), StringLiteral('" How are you?"')))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 330))

    def test_031(self):
        input = """func foo() {};"""
        expect = Program([
            FuncDecl("foo",[], VoidType(), Block([]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 331))

    def test_032(self):
        input = """func add(a int, b int) int { return a + b; } ;"""
        expect = Program([
            FuncDecl("add", [
                ParamDecl("a", IntType()), 
                ParamDecl("b", IntType())
            ], IntType(), Block([Return(BinaryOp("+", Id("a"), Id("b")))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 332))

    def test_033(self):
        input = """func greet(name string) string { return "Hello, " + name; };"""
        expect = Program([
            FuncDecl("greet", [
                ParamDecl("name", StringType())
            ], StringType(), Block([Return(BinaryOp("+", StringLiteral('"Hello, "'), Id("name")))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 333))

    def test_034(self):
        input = """func is_even(n int) boolean { return n % 2 == 0; };"""
        expect = Program([
            FuncDecl("is_even", [
                ParamDecl("n", IntType())
            ], BoolType(), Block([Return(BinaryOp("==", BinaryOp("%", Id("n"), IntLiteral(2)), IntLiteral(0)))]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 334))

    def test_035(self):
        input = """func do_nothing() {};"""
        expect = Program([
            FuncDecl("do_nothing", [], VoidType(), Block([]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 335))

    def test_036(self):
        input = """func factorial(n int) int { if (n == 0) { return 1; }; return n * factorial(n - 1); };"""
        expect = Program([
            FuncDecl("factorial", [
                ParamDecl("n", IntType())
            ], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), Block([Return(IntLiteral(1))]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 336))

    def test_037(self):
        input = """func print_numbers(n int) { 
                        for i := 1; i <= n; i += 1 { 
                            print(i); 
                        }
                    };"""
        expect = Program([
            FuncDecl("print_numbers", [
                ParamDecl("n", IntType())
            ], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(1)), 
                        BinaryOp("<=", Id("i"), Id("n")), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([FuncCall("print", [Id("i")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 337))

    def test_038(self):
        input = """func max(a int, b int) int { if (a > b) { return a; }; return b; };"""
        expect = Program([
            FuncDecl("max", [
                ParamDecl("a", IntType()), 
                ParamDecl("b", IntType())
            ], IntType(), Block([
                If(BinaryOp(">", Id("a"), Id("b")), Block([Return(Id("a"))]), None),
                Return(Id("b"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 338))

    def test_039(self):
        input = """func power(base float, exp int) float { var result = 1.0; return result; };"""
        expect = Program([
            FuncDecl("power", [
                ParamDecl("base", FloatType()), 
                ParamDecl("exp", IntType())
            ], FloatType(), Block([
                VarDecl("result", None, FloatLiteral(1.0)),
                Return(Id("result"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 339))

    def test_040(self):
        input = """func swap(x int, y int) { 
                        var temp = x; 
                        x := y; 
                        y := temp; 
                    };"""
        expect = Program([
            FuncDecl("swap", [
                ParamDecl("x", IntType()), 
                ParamDecl("y", IntType())
            ], VoidType(), Block([
                VarDecl("temp", None, Id("x")),
                Assign(Id("x"), Id("y")),
                Assign(Id("y"), Id("temp"))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 340))

    def test_041(self):
        input = """func (p Person) getName() string { return p.name; };"""
        expect = Program([
            MethodDecl("p", Id("Person"), FuncDecl("getName", [], StringType(), Block([
                Return(FieldAccess(Id("p"), "name"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 341))

    def test_042(self):
        input = """func (p Person) setName(newName string) { p.name := newName; };"""
        expect = Program([
            MethodDecl("p", Id("Person"), FuncDecl("setName", [
                ParamDecl("newName", StringType())
            ], VoidType(), Block([
                Assign(FieldAccess(Id("p"), "name"), Id("newName"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 342))

    def test_043(self):
        input = """func (r Rectangle) getArea() float { return r.width * r.height; };"""
        expect = Program([
            MethodDecl("r", Id("Rectangle"), FuncDecl("getArea", [], FloatType(), Block([
                Return(BinaryOp("*", FieldAccess(Id("r"), "width"), FieldAccess(Id("r"), "height")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 343))

    def test_044(self):
        input = """func (r Rectangle) setDimensions(w float, h float) { 
                        r.width := w; 
                        r.height := h; 
                    };"""
        expect = Program([
            MethodDecl("r", Id("Rectangle"), FuncDecl("setDimensions", [
                ParamDecl("w", FloatType()),
                ParamDecl("h", FloatType())
            ], VoidType(), Block([
                Assign(FieldAccess(Id("r"), "width"), Id("w")),
                Assign(FieldAccess(Id("r"), "height"), Id("h"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 344))

    def test_045(self):
        input = """func (c Car) startEngine() { print("Engine started!"); };"""
        expect = Program([
            MethodDecl("c", Id("Car"), FuncDecl("startEngine", [], VoidType(), Block([
                FuncCall("print", [StringLiteral('"Engine started!"')])
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 345))

    def test_046(self):
        input = """func (c Car) accelerate(speed int) { c.currentSpeed := c.currentSpeed + speed; };"""
        expect = Program([
            MethodDecl("c", Id("Car"), FuncDecl("accelerate", [
                ParamDecl("speed", IntType())
            ], VoidType(), Block([
                Assign(FieldAccess(Id("c"), "currentSpeed"), 
                       BinaryOp("+", FieldAccess(Id("c"), "currentSpeed"), Id("speed")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 346))

    def test_047(self):
        input = """func (b BankAccount) deposit(amount float) { b.balance := b.balance + amount; };"""
        expect = Program([
            MethodDecl("b", Id("BankAccount"), FuncDecl("deposit", [
                ParamDecl("amount", FloatType())
            ], VoidType(), Block([
                Assign(FieldAccess(Id("b"), "balance"), 
                       BinaryOp("+", FieldAccess(Id("b"), "balance"), Id("amount")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 347))

    def test_048(self):
        input = """func (b BankAccount) withdraw(amount float) boolean { 
                        if (b.balance >= amount) { 
                            b.balance := b.balance - amount; 
                            return true; 
                        }; 
                        return false; 
                    };"""
        expect = Program([
            MethodDecl("b", Id("BankAccount"), FuncDecl("withdraw", [
                ParamDecl("amount", FloatType())
            ], BoolType(), Block([
                If(BinaryOp(">=", FieldAccess(Id("b"), "balance"), Id("amount")), 
                   Block([
                       Assign(FieldAccess(Id("b"), "balance"), 
                              BinaryOp("-", FieldAccess(Id("b"), "balance"), Id("amount"))),
                       Return(BooleanLiteral(True))
                   ]), None),
                Return(BooleanLiteral(False))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 348))

    def test_049(self):
        input = """func (s Student) getFullName() string { return s.firstName + " " + s.lastName; };"""
        expect = Program([
            MethodDecl("s", Id("Student"), FuncDecl("getFullName", [], StringType(), Block([
                Return(BinaryOp("+", 
                                BinaryOp("+", FieldAccess(Id("s"), "firstName"), StringLiteral('" "')), 
                                FieldAccess(Id("s"), "lastName")))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 349))

    def test_050(self):
        input = """func (s Student) updateGrade(newGrade float) { s.grade := newGrade; };"""
        expect = Program([
            MethodDecl("s", Id("Student"), FuncDecl("updateGrade", [
                ParamDecl("newGrade", FloatType())
            ], VoidType(), Block([
                Assign(FieldAccess(Id("s"), "grade"), Id("newGrade"))
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 350))

    def test_051(self):
        input = """type Person struct { name string; age int; };"""
        expect = Program([
            StructType("Person", [
                ("name", StringType()),
                ("age", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 351))

    def test_052(self):
        input = """type Rectangle struct { width float; height float; };"""
        expect = Program([
            StructType("Rectangle", [
                ("width", FloatType()),
                ("height", FloatType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 352))

    def test_053(self):
        input = """type Car struct { brand string; model string; year int; };"""
        expect = Program([
            StructType("Car", [
                ("brand", StringType()),
                ("model", StringType()),
                ("year", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 353))

    def test_054(self):
        input = """type Book struct { title string; author string; pages int; };"""
        expect = Program([
            StructType("Book", [
                ("title", StringType()),
                ("author", StringType()),
                ("pages", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 354))

    def test_055(self):
        input = """type Student struct { id int; name string; gpa float; };"""
        expect = Program([
            StructType("Student", [
                ("id", IntType()),
                ("name", StringType()),
                ("gpa", FloatType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 355))

    def test_056(self):
        input = """type Employee struct { id int; name string; salary float; department string; };"""
        expect = Program([
            StructType("Employee", [
                ("id", IntType()),
                ("name", StringType()),
                ("salary", FloatType()),
                ("department", StringType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 356))

    def test_057(self):
        input = """type Address struct { street string; city string; zipcode int; };"""
        expect = Program([
            StructType("Address", [
                ("street", StringType()),
                ("city", StringType()),
                ("zipcode", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 357))

    def test_058(self):
        input = """type Point struct { x float; y float; };"""
        expect = Program([
            StructType("Point", [
                ("x", FloatType()),
                ("y", FloatType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 358))

    def test_059(self):
        input = """type Laptop struct { brand string; price float; isAvailable boolean; };"""
        expect = Program([
            StructType("Laptop", [
                ("brand", StringType()),
                ("price", FloatType()),
                ("isAvailable", BoolType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 359))

    def test_060(self):
        input = """type Product struct { id int; name string; price float; stock int; };"""
        expect = Program([
            StructType("Product", [
                ("id", IntType()),
                ("name", StringType()),
                ("price", FloatType()),
                ("stock", IntType())
            ], [])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 360))

    def test_061(self):
        input = """type Drawable interface { draw(); };"""
        expect = Program([
            InterfaceType("Drawable", [
                Prototype("draw", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 361))

    def test_062(self):
        input = """type Shape interface { getArea() float; };"""
        expect = Program([
            InterfaceType("Shape", [
                Prototype("getArea", [], FloatType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 362))

    def test_063(self):
        input = """type Resizable interface { resize(factor float); };"""
        expect = Program([
            InterfaceType("Resizable", [
                Prototype("resize", [FloatType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 363))

    def test_064(self):
        input = """type Logger interface { log(message string); };"""
        expect = Program([
            InterfaceType("Logger", [
                Prototype("log", [StringType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 364))

    def test_065(self):
        input = """type Comparator interface { compare(a int, b int) boolean; };"""
        expect = Program([
            InterfaceType("Comparator", [
                Prototype("compare", [IntType(), IntType()], BoolType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 365))

    def test_066(self):
        input = """type Serializer interface { serialize() string; deserialize(data string); };"""
        expect = Program([
            InterfaceType("Serializer", [
                Prototype("serialize", [], StringType()),
                Prototype("deserialize", [StringType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 366))

    def test_067(self):
        input = """type Database interface { connect(); disconnect(); };"""
        expect = Program([
            InterfaceType("Database", [
                Prototype("connect", [], VoidType()),
                Prototype("disconnect", [], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 367))

    def test_068(self):
        input = """type Network interface { send(data string); receive() string; };"""
        expect = Program([
            InterfaceType("Network", [
                Prototype("send", [StringType()], VoidType()),
                Prototype("receive", [], StringType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 368))

    def test_069(self):
        input = """type Storage interface { read(key string) string; write(key string, value string); };"""
        expect = Program([
            InterfaceType("Storage", [
                Prototype("read", [StringType()], StringType()),
                Prototype("write", [StringType(), StringType()], VoidType())
            ])
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 369))

    def test_070(self):
        input = """type Vehicle interface { start(); stop(); speedUp(amount float); };"""
        expect = Program([
                InterfaceType("Vehicle", [
                    Prototype("start", [], VoidType()),
                    Prototype("stop", [], VoidType()),
                    Prototype("speedUp", [FloatType()], VoidType())
                ])
            ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 370))

    def test_071(self):
        input = """func test() { if (x > 0) { x := x - 1; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                   Block([Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(1)))]), 
                   None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 371))

    def test_072(self):
        input = """func test() { if (y == 10) { y := y + 1; } else { y := 0; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp("==", Id("y"), IntLiteral(10)), 
                   Block([Assign(Id("y"), BinaryOp("+", Id("y"), IntLiteral(1)))]), 
                   Block([Assign(Id("y"), IntLiteral(0))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 372))

    def test_073(self):
        input = """func test() { if (a < b) { a := b; } else if (a > c) { a := c; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp("<", Id("a"), Id("b")), 
                   Block([Assign(Id("a"), Id("b"))]), 
                   If(BinaryOp(">", Id("a"), Id("c")), 
                      Block([Assign(Id("a"), Id("c"))]), 
                      None))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 373))

    def test_074(self):
        input = """func test() { if (flag) { return; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(Id("flag"), Block([Return(None)]), None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 374))

    def test_075(self):
        input = """func test() { if (num % 2 == 0) { print("Even"); } else { print("Odd"); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp("==", BinaryOp("%", Id("num"), IntLiteral(2)), IntLiteral(0)), 
                   Block([FuncCall("print", [StringLiteral('"Even"')])]), 
                   Block([FuncCall("print", [StringLiteral('"Odd"')])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 375))

    def test_076(self):
        input = """func test() { if (score >= 90) { grade := "A"; } else if (score >= 80) { grade := "B"; } else { grade := "C"; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp(">=", Id("score"), IntLiteral(90)), 
                   Block([Assign(Id("grade"), StringLiteral('"A"'))]), 
                   If(BinaryOp(">=", Id("score"), IntLiteral(80)), 
                      Block([Assign(Id("grade"), StringLiteral('"B"'))]), 
                      Block([Assign(Id("grade"), StringLiteral('"C"'))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 376))

    def test_077(self):
        input = """func test() { if (x < 0) { x := -x; return x; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp("<", Id("x"), IntLiteral(0)), 
                   Block([Assign(Id("x"), UnaryOp("-", Id("x"))), Return(Id("x"))]), 
                   None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 377))

    def test_078(self):
        input = """func test() { if (a == b && c != d) { swap(a, b); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp("&&", BinaryOp("==", Id("a"), Id("b")), BinaryOp("!=", Id("c"), Id("d"))), 
                   Block([FuncCall("swap", [Id("a"), Id("b")])]), 
                   None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 378))

    def test_079(self):
        input = """func test() { if (x > 0) { if (y > 0) { print("Both positive"); }; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp(">", Id("x"), IntLiteral(0)), 
                   Block([If(BinaryOp(">", Id("y"), IntLiteral(0)), 
                             Block([FuncCall("print", [StringLiteral('"Both positive"')])]), 
                             None)]), 
                   None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 379))

    def test_080(self):
        input = """func test() { if (num > 100) { print("Large"); } else if (num > 50) { print("Medium"); } else if (num > 10) { print("Small"); } else { print("Tiny"); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                If(BinaryOp(">", Id("num"), IntLiteral(100)), 
                   Block([FuncCall("print", [StringLiteral('"Large"')])]), 
                   If(BinaryOp(">", Id("num"), IntLiteral(50)), 
                      Block([FuncCall("print", [StringLiteral('"Medium"')])]), 
                      If(BinaryOp(">", Id("num"), IntLiteral(10)), 
                         Block([FuncCall("print", [StringLiteral('"Small"')])]), 
                         Block([FuncCall("print", [StringLiteral('"Tiny"')])]))))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 380))

    def test_081(self):
        input = """func test() { for x := 0; x < 10; x += 1 { print(x); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForStep(Assign(Id("x"), IntLiteral(0)), 
                        BinaryOp("<", Id("x"), IntLiteral(10)), 
                        Assign(Id("x"), BinaryOp("+", Id("x"), IntLiteral(1))),
                        Block([FuncCall("print", [Id("x")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 381))

    def test_082(self):
        input = """func test() { for var i int = 1; i <= 5; i += 1 { sum := sum + i; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForStep(VarDecl("i", IntType(), IntLiteral(1)), 
                        BinaryOp("<=", Id("i"), IntLiteral(5)), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 382))

    def test_083(self):
        input = """func test() { for count := 10; count > 0; count -= 1 { print(count); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForStep(Assign(Id("count"), IntLiteral(10)), 
                        BinaryOp(">", Id("count"), IntLiteral(0)), 
                        Assign(Id("count"), BinaryOp("-", Id("count"), IntLiteral(1))),
                        Block([FuncCall("print", [Id("count")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 383))

    def test_084(self):
        input = """func test() { for i <= 5 { sum := sum + i; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForBasic(BinaryOp("<=", Id("i"), IntLiteral(5)), 
                         Block([Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("i")))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 384))

    def test_085(self):
        input = """func test() { for x > 0 { x := x - 1; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForBasic(BinaryOp(">", Id("x"), IntLiteral(0)), 
                         Block([Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(1)))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 385))

    def test_086(self):
        input = """func test() { for idx, val := range arr { print(idx, val); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForEach(Id("idx"), Id("val"), Id("arr"), 
                         Block([FuncCall("print", [Id("idx"), Id("val")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 386))

    def test_087(self):
        input = """func test() { for key, value := range dictionary { print(key, value); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForEach(Id("key"), Id("value"), Id("dictionary"), 
                         Block([FuncCall("print", [Id("key"), Id("value")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 387))

    def test_088(self):
        input = """func test() { for var x = 2; x < 20; x *= 2 { print(x); }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForStep(VarDecl("x", None, IntLiteral(2)), 
                        BinaryOp("<", Id("x"), IntLiteral(20)), 
                        Assign(Id("x"), BinaryOp("*", Id("x"), IntLiteral(2))),
                        Block([FuncCall("print", [Id("x")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 388))

    def test_089(self):
        input = """func test() { for num, index := range dataset { total := total + num; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForEach(Id("num"), Id("index"), Id("dataset"), 
                         Block([Assign(Id("total"), BinaryOp("+", Id("total"), Id("num")))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 389))

    def test_090(self):
        input = """func test() { for counter >= 0 { counter := counter - 1; }; };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForBasic(BinaryOp(">=", Id("counter"), IntLiteral(0)), 
                         Block([Assign(Id("counter"), BinaryOp("-", Id("counter"), IntLiteral(1)))]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 390))

    def test_091(self):
        input = """func test() { 
                       var x int = 10; 
                       if (x > 5) { 
                           for i := 1; i <= x; i += 1 { print(i); }; 
                       }; 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                VarDecl("x", IntType(), IntLiteral(10)),
                If(BinaryOp(">", Id("x"), IntLiteral(5)), 
                   Block([
                       ForStep(Assign(Id("i"), IntLiteral(1)), 
                               BinaryOp("<=", Id("i"), Id("x")), 
                               Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                               Block([FuncCall("print", [Id("i")])]))
                   ]), None)
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 391))

    def test_092(self):
        input = """type Animal struct { name string; age int; }; 
                   func (a Animal) speak() { print("I am an animal"); };"""
        expect = Program([
            StructType("Animal", [
                ("name", StringType()),
                ("age", IntType())
            ], []),
            MethodDecl("a", Id("Animal"), FuncDecl("speak", [], VoidType(), Block([
                FuncCall("print", [StringLiteral('"I am an animal"')])
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 392))

    def test_093(self):
        input = """type Drawable interface { draw(); }; 
                   type Shape struct { color string; }; 
                   func (s Shape) draw() { print("Drawing shape"); };"""
        expect = Program([
            InterfaceType("Drawable", [
                Prototype("draw", [], VoidType())
            ]),
            StructType("Shape", [
                ("color", StringType())
            ], []),
            MethodDecl("s", Id("Shape"), FuncDecl("draw", [], VoidType(), Block([
                FuncCall("print", [StringLiteral('"Drawing shape"')])
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 393))

    def test_094(self):
        input = """func factorial(n int) int { 
                       if (n == 0) { return 1; }; 
                       return n * factorial(n - 1); 
                   };"""
        expect = Program([
            FuncDecl("factorial", [
                ParamDecl("n", IntType())
            ], IntType(), Block([
                If(BinaryOp("==", Id("n"), IntLiteral(0)), 
                   Block([Return(IntLiteral(1))]), None),
                Return(BinaryOp("*", Id("n"), FuncCall("factorial", [BinaryOp("-", Id("n"), IntLiteral(1))])))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 394))

    def test_095(self):
        input = """func test() { 
                       const PI = 3.14; 
                       var r float = 5.0; 
                       var area float = PI * r * r; 
                       print(area); 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ConstDecl("PI", None, FloatLiteral(3.14)),
                VarDecl("r", FloatType(), FloatLiteral(5.0)),
                VarDecl("area", FloatType(), BinaryOp("*", BinaryOp("*", Id("PI"), Id("r")), Id("r"))),
                FuncCall("print", [Id("area")])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 395))

    def test_096(self):
        input = """func test() { 
                       var arr [5]int; 
                       for i := 0; i < 5; i += 1 { arr[i] := i * i; }; 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                VarDecl("arr", ArrayType([IntLiteral(5)], IntType()), None),
                ForStep(Assign(Id("i"), IntLiteral(0)), 
                        BinaryOp("<", Id("i"), IntLiteral(5)), 
                        Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1))),
                        Block([
                            Assign(ArrayCell(Id("arr"), [Id("i")]), 
                                   BinaryOp("*", Id("i"), Id("i")))
                        ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 396))

    def test_097(self):
        input = """func test() { 
                       for idx, val := range numbers { print(idx, val); }; 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForEach(Id("idx"), Id("val"), Id("numbers"), 
                        Block([FuncCall("print", [Id("idx"), Id("val")])]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 397))

    def test_098(self):
        input = """func test() { 
                       for i := 10; i > 0; i -= 1 { 
                           if (i % 2 == 0) { print(i, " is even"); }; 
                       }; 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                ForStep(Assign(Id("i"), IntLiteral(10)), 
                        BinaryOp(">", Id("i"), IntLiteral(0)), 
                        Assign(Id("i"), BinaryOp("-", Id("i"), IntLiteral(1))),
                        Block([
                            If(BinaryOp("==", BinaryOp("%", Id("i"), IntLiteral(2)), IntLiteral(0)), 
                               Block([FuncCall("print", [Id("i"), StringLiteral('" is even"')])]), 
                               None)
                        ]))
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 398))

    def test_099(self):
        input = """func (p Person) introduce() { 
                       print("Hello, my name is ", p.name); 
                   };"""
        expect = Program([
            MethodDecl("p", Id("Person"), FuncDecl("introduce", [], VoidType(), Block([
                FuncCall("print", [StringLiteral('"Hello, my name is "'), FieldAccess(Id("p"), "name")])
            ])))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 399))

    def test_100(self):
        input = """func test() { 
                       var score int = 85; 
                       if (score >= 90) { grade := "A";
                       } else if (score >= 80) { grade := "B";
                       } else { grade := "C"; }; 
                       print("Your grade is: ", grade); 
                   };"""
        expect = Program([
            FuncDecl("test", [], VoidType(), Block([
                VarDecl("score", IntType(), IntLiteral(85)),
                If(BinaryOp(">=", Id("score"), IntLiteral(90)), 
                   Block([Assign(Id("grade"), StringLiteral('"A"'))]), 
                   If(BinaryOp(">=", Id("score"), IntLiteral(80)), 
                      Block([Assign(Id("grade"), StringLiteral('"B"'))]), 
                      Block([Assign(Id("grade"), StringLiteral('"C"'))]))),
                FuncCall("print", [StringLiteral('"Your grade is: "'), Id("grade")])
            ]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, str(expect), 400))
