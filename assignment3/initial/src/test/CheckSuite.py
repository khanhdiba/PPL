import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_001(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_002(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_003(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,403))
     
    '''Redeclared'''
    def test_004(self):
        input = """var a int; const a = 1;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_005(self):
        input = """var a int; func a () {return;};"""
        expect = "Redeclared Function: a\n"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_006(self):
        input = '''
                var a int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                '''
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_007(self):
        input = '''
                var add int = 100;
                func add (x, y int) int {
                    return x + y;
                };
    
                '''
        expect = "Redeclared Function: add\n"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_008(self):
        input = '''
                var putInt int;
                '''
        expect = "Redeclared Variable: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_009(self):
        input = '''
                const putLn = 10;
                '''
        expect = "Redeclared Constant: putLn\n"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_010(self):
        input = '''
                var a = 1;
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_011(self):
        input = '''
                var putInt int;
                '''
        expect = "Redeclared Variable: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_012(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) putInt(){return;};
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_013(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) x(){return;};
                '''
        expect = "Redeclared Method: x\n"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_014(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) a(){return;};
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_015(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) putInt(s int){
                    var s = 100;
                    return;
                };
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_016(self):
        input = """var a int; var b int; var a int; """
        expect = "Redeclared Variable: a\n"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_017(self):
        input = """var a int = 1.2;"""
        expect = "Type Mismatch: VarDecl(a,IntType,FloatLiteral(1.2))\n"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_018(self):
        input = Program([VarDecl("a",IntType(),Id("b"))])
        expect = "Undeclared Identifier: b\n"
        self.assertTrue(TestChecker.test(input,expect,418))
     
    def test_019(self):
        input = """var a int; const a = 1;"""
        expect = "Redeclared Constant: a\n"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_020(self):
        input = """var a int; func a () {return;};"""
        expect = "Redeclared Function: a\n"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_021(self):
        input = '''
                var a int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                '''
        expect = "Redeclared Type: a\n"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_022(self):
        input = '''
                var add int = 100;
                func add (x, y int) int {
                    return x + y;
                };
    
                '''
        expect = "Redeclared Function: add\n"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_023(self):
        input = '''
                var putInt int;
                '''
        expect = "Redeclared Variable: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_024(self):
        input = '''
                const putLn = 10;
                '''
        expect = "Redeclared Constant: putLn\n"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_025(self):
        input = '''
                var a = 1;
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_026(self):
        input = '''
                var putInt int;
                '''
        expect = "Redeclared Variable: putInt\n"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_027(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) putInt(){return;};
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_028(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) x(){return;};
                '''
        expect = "Redeclared Method: x\n"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_029(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) a(){return;};
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_030(self):
        input = '''
                var x int;
                type a struct {
                    x int;
                    y int;
                }
                const b = 10;
                func (s a) putInt(s int){
                    var s = 100;
                    return;
                };
                '''
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_031(self):
        input = '''
                func main() {
                    a := 1
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_032(self):
        input = '''
                func main() {
                    a := b
                }
                '''
        expect = 'Undeclared Identifier: b\n'
        self.assertTrue(TestChecker.test(input,expect,432))


    def test_033(self):
        input = '''
                func main() {
                    a += 1
                }
                '''
        expect = 'Undeclared Identifier: a\n'
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_034(self):
        input = '''
                var x = 1;
                func main() {
                    x += 2;
                    putIntLn(x)
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_035(self):
        input = '''
                func main() {
                    for x := 1; x < 10; b := 1 {
                            var b = 2;
                        }
                }
                '''
        expect = 'Redeclared Variable: b\n'
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_036(self):
        input = '''
                func main() {
                    for x < 2 {
                            var b = 2;
                    }
                }
                '''
        expect = 'Undeclared Identifier: x\n'
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_037(self):
        input = '''
                func main() {
                    for idx, val := range [3] int {1,2,3} {
                            var b = 2;
                    }
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_038(self):
        input = '''
                func main() {
                    if (x < 2) {
                        continue;
                    }
                }
                '''
        expect = 'Undeclared Identifier: x\n'
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_039(self):
        input = '''
                func main() {
                    if(true){
                        break;
                    }
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_040(self):
        input = '''
                func main() {
                    if (false){
                        continue;
                    }
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_041(self):
        input = '''
                var x int;
                var x float;
                '''
        expect = 'Redeclared Variable: x\n'
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_042(self):
        input = '''
                func foo() {return;}
                func foo() {return;}
                func main() {return;}
                '''
        expect = 'Redeclared Function: foo\n'
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_043(self):
        input = '''
                func main(x int, x float) {return;}
                '''
        expect = 'Redeclared Parameter: x\n'
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_044(self):
        input = '''
                func main() {
                    var x int;
                    var x bool;
                }
                '''
        expect = 'Redeclared Variable: x\n'
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_045(self):
        input = '''
                var x int;
                func main() {
                    var x float;
                    var x bool;
                }
                '''
        expect = 'Redeclared Variable: x\n'
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_046(self):
        input = '''
                func main() {
                    x := 5;
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_047(self):
        input = '''
                func main() {
                    foo();
                }
                '''
        expect = 'Undeclared Function: foo\n'
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_048(self):
        input = '''
                type A struct {
                    x int;
                    x float;
                }
                func main() {return;}
                '''
        expect = 'Redeclared Field: x\n'
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_049(self):
        input = '''
                type A struct {
                    x int;
                }

                func main() {
                    var a A;
                    var y = a.y;
                }
                '''
        expect = 'Undeclared Field: y\n'
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_050(self):
        input = '''
                func main() {
                    var x int;
                    var x string;
                }
                '''
        expect = 'Redeclared Variable: x\n'
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_051(self):
        input = '''
                var x int;
                func foo() {
                    var x bool;
                    var x string;
                }
                func main() {return;}
                '''
        expect = 'Redeclared Variable: x\n'
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_052(self):
        input = '''
                func main() {
                    var a int;
                    var a bool;
                }
                '''
        expect = 'Redeclared Variable: a\n'
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_053(self):
        input = '''
                func main() {
                    a := 1;
                }
                '''
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_054(self):
        input = '''
                func main() {
                    var x int;
                    x := y;
                }
                '''
        expect = 'Undeclared Identifier: y\n'
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_055(self):
        input = '''
                func main() {
                    y();
                }
                '''
        expect = 'Undeclared Function: y\n'
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_056(self):
        input = '''
                func foo() {return;}
                func main() {
                    foo();
                    foo();
                    var foo = 1;
                    foo();
                }
                '''
        expect = 'Undeclared Function: foo\n'
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_057(self):
        input = '''
                type A struct {
                    name string;
                }

                func main() {
                    var a A;
                    a.age := 20;
                }
                '''
        expect = 'Undeclared Field: age\n'
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_058(self):
        input = '''
                func foo(x int) {return;}
                func main() {
                    var x int;
                    foo(x);
                    foo(y);
                }
                '''
        expect = 'Undeclared Identifier: y\n'
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_059(self):
        input = '''
                func main() {
                    var a int;
                    var b int;
                    var a float;
                }
                '''
        expect = 'Redeclared Variable: a\n'
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_060(self):
        input = '''
                func foo() {return;}
                func bar() {return;}
                func foo() {return;}
                func main() {return;}
                '''
        expect = 'Redeclared Function: foo\n'
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_061(self):
        input = '''
                    var x int = 1.0;
                '''
        expect = 'Type Mismatch: VarDecl(x,IntType,FloatLiteral(1.0))\n'
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_062(self):
        input = '''
            func main() {
                a := 1.2;
                var b int = a;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,IntType,Id(a))\n'
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_063(self):
        input = '''
            var a int = true;
        '''
        expect = 'Type Mismatch: VarDecl(a,IntType,BooleanLiteral(true))\n'
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_064(self):
        input = '''
            func main() {
                var x bool = 1;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,Id(bool),IntLiteral(1))\n'
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_065(self):
        input = '''
            func main() {
                var x float = true;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,FloatType,BooleanLiteral(true))\n'
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_066(self):
        input = '''
            func main() {
                x := 1;
                x := true;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(x),BooleanLiteral(true))\n'
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_067(self):
        input = '''
            var x string = 1;
        '''
        expect = 'Type Mismatch: VarDecl(x,StringType,IntLiteral(1))\n'
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_068(self):
        input = '''
            func main() {
                a := 1.5;
                var b boolean = a;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,Id(a))\n'
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_069(self):
        input = '''
            func main() {
                var s string = true;
            }
        '''
        expect = 'Type Mismatch: VarDecl(s,StringType,BooleanLiteral(true))\n'
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_070(self):
        input = '''
            func main() {
                x := "hello";
                var y float = x;
            }
        '''
        expect = 'Type Mismatch: VarDecl(y,FloatType,Id(x))\n'
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_071(self):
        input = '''
            func main() {
                var x int = 1.1;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,FloatLiteral(1.1))\n'
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_072(self):
        input = '''
            func main() {
                var b boolean = "true";
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,StringLiteral("true"))\n'
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_073(self):
        input = '''
            func main() {
                var c string = false;
            }
        '''
        expect = 'Type Mismatch: VarDecl(c,StringType,BooleanLiteral(false))\n'
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_074(self):
        input = '''
            func main() {
                a := "hi";
                var b bool = a;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,Id(bool),Id(a))\n'
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_075(self):
        input = '''
            func main() {
                x := 1;
                x := 2.0;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(x),FloatLiteral(2.0))\n'
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_076(self):
        input = '''
            func main() {
                var a int = "123";
            }
        '''
        expect = 'Type Mismatch: VarDecl(a,IntType,StringLiteral("123"))\n'
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_077(self):
        input = '''
            func main() {
                var f float = "1.1";
            }
        '''
        expect = 'Type Mismatch: VarDecl(f,FloatType,StringLiteral("1.1"))\n'
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_078(self):
        input = '''
            func main() {
                b := true;
                var s string = b;
            }
        '''
        expect = 'Type Mismatch: VarDecl(s,StringType,Id(b))\n'
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_079(self):
        input = '''
            func main() {
                s := "abc";
                var x int = s;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,Id(s))\n'
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_080(self):
        input = '''
            func main() {
                var x float = "3.14";
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,FloatType,StringLiteral("3.14"))\n'
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_081(self):
        input = '''
            func main() {
                var x int = "abc";
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,StringLiteral("abc"))\n'
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_082(self):
        input = '''
            func main() {
                a := false;
                a := 0;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(a),IntLiteral(0))\n'
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_083(self):
        input = '''
            func main() {
                var b boolean = 123;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,IntLiteral(123))\n'
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_084(self):
        input = '''
            func main() {
                var c string = 1.23;
            }
        '''
        expect = 'Type Mismatch: VarDecl(c,StringType,FloatLiteral(1.23))\n'
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_085(self):
        input = '''
            func main() {
                x := "abc";
                x := true;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(x),BooleanLiteral(true))\n'
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_086(self):
        input = '''
            func main() {
                var x int = false;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,BooleanLiteral(false))\n'
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_087(self):
        input = '''
            func main() {
                var f float = false;
            }
        '''
        expect = 'Type Mismatch: VarDecl(f,FloatType,BooleanLiteral(false))\n'
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_088(self):
        input = '''
            func main() {
                var f float = "hello";
            }
        '''
        expect = 'Type Mismatch: VarDecl(f,FloatType,StringLiteral("hello"))\n'
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_089(self):
        input = '''
            func main() {
                var b boolean = 3.14;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,FloatLiteral(3.14))\n'
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_090(self):
        input = '''
            func main() {
                s := "true";
                var x boolean = s;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,BoolType,Id(s))\n'
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_091(self):
        input = '''
            func main() {
                var i int = false;
            }
        '''
        expect = 'Type Mismatch: VarDecl(i,IntType,BooleanLiteral(false))\n'
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_092(self):
        input = '''
            func main() {
                var s string = 1.2;
            }
        '''
        expect = 'Type Mismatch: VarDecl(s,StringType,FloatLiteral(1.2))\n'
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_093(self):
        input = '''
            func main() {
                var b boolean = "false";
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,StringLiteral("false"))\n'
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_094(self):
        input = '''
            func main() {
                var x int = 3.14;
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,FloatLiteral(3.14))\n'
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_095(self):
        input = '''
            func main() {
                s := "hi";
                s := 0;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(s),IntLiteral(0))\n'
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_096(self):
        input = '''
            func main() {
                var b boolean = 1;
            }
        '''
        expect = 'Type Mismatch: VarDecl(b,BoolType,IntLiteral(1))\n'
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_097(self):
        input = '''
            func main() {
                var s string = false;
            }
        '''
        expect = 'Type Mismatch: VarDecl(s,StringType,BooleanLiteral(false))\n'
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_098(self):
        input = '''
            func main() {
                x := 1.1;
                x := "1.1";
            }
        '''
        expect = 'Type Mismatch: Assign(Id(x),StringLiteral("1.1"))\n'
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_099(self):
        input = '''
            func main() {
                y := true;
                y := 1.0;
            }
        '''
        expect = 'Type Mismatch: Assign(Id(y),FloatLiteral(1.0))\n'
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_100(self):
        input = '''
            func main() {
                var x int = "100";
            }
        '''
        expect = 'Type Mismatch: VarDecl(x,IntType,StringLiteral("100"))\n'
        self.assertTrue(TestChecker.test(input, expect, 500))
