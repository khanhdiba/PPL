import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_502(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_503(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_504(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_505(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_506(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_507(self):
        input = '''
                    func main(){putBool(true);};
                '''
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_508(self):
        input = '''
                    const a = 10;
                    const b = 20;
                    func main() {
                        var c = a + b;
                        c *= 2;
                        putInt(c)
                    };
                '''
        expect = '60'
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_509(self):
        input = '''
                    func main(){
                        putStringLn("Hello World")
                    }
                '''
        expect = 'Hello World\n'
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_510(self):
        input = '''
                    func add(x, y int) int {
                        return x + y;
                    }

                    func main(){
                        x := add(1, 2)
                        putInt(x)
                    }

                '''
        expect = '3'
        self.assertTrue(TestCodeGen.test(input,expect,510))
    
    def test_511(self):
        input = '''
                    func sub(x, y int) int {
                        return x - y;
                    }

                    func main(){
                        x := sub(1, 2)
                        putInt(x)
                    }
                '''
        expect = '-1'
        self.assertTrue(TestCodeGen.test(input,expect,511))
    
    def test_512(self):
        input = '''
                    func mul(x, y int) int {
                        return x * y;
                    }

                    func main(){
                        x := mul(1, 2)
                        putInt(x)
                    }
                '''
        expect = '2'
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_513(self):
        input = '''
                    func div(x, y int) int {
                        return x / y;
                    }

                    func main(){
                        x := div(1, 2)
                        putInt(x)
                    }
                '''
        expect = '0'
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test_514(self):
        input = '''
                    func mod(x, y int) int {
                        return x % y;
                    }

                    func main(){
                        x := mod(1, 2)
                        putInt(x)
                    }
                '''
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_515(self):
        input = '''
                    func power(x int) int {
                        return x * x;
                    }
                    func main(){
                        x := power(2)
                        putInt(x)
                    }
                '''
        expect = '4'
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_516(self):
        input = '''
                    func cube(x int) int {
                        return x * x * x;
                    }
                    func main(){
                        x := cube(2)
                        putInt(x)
                    }
                '''
        expect = '8'
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_517(self):
        input = '''
                    func tetra(x int) int {
                        return x * x * x * x;
                    }
                    func main(){
                        x := tetra(2)
                        putInt(x)
                    }
                '''
        expect = '16'
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_518(self):
        input = '''
                    func isEqual(x, y int) boolean {
                        return x == y;
                    }
                    func main(){
                        x := isEqual(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'false'
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_519(self):
        input = '''
                    func isEqual(x, y int) boolean {
                        return x == y;
                    }
                    func isNotEqual(x, y int) boolean{
                        return !isEqual(x, y);
                    }
                    func main(){
                        x := isNotEqual(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_520(self):
        input = '''
                    func isLT(x, y int) boolean {
                        return x < y;
                    }
                    func main(){
                        x := isLT(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_521(self):
        input = '''
                    func isLE(x, y int) boolean {
                        return x <= y;
                    }
                    func main(){
                        x := isLE(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_522(self):
        input = '''
                    func isGT(x, y int) boolean {
                        return x > y;
                    }
                    func main(){
                        x := isGT(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'false'
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_523(self):
        input = '''
                    func isGE(x, y int) boolean {
                        return x >= y;
                    }
                    func main(){
                        x := isGE(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'false'
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_524(self):
        input = '''
                    func isGT(x, y int) boolean {
                        return x > y;
                    }
                    func main(){
                        x := isGT(1, 2)
                        putBool(x)
                    }
                '''
        expect = 'false'
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_525(self):
        input = '''
                    func Hello(name string){
                        putString("Hello ")
                        putStringLn(name)
                    }
                    func main(){
                        Hello("Khanh")
                        Hello("Leonard")
                    }
                '''
        expect = 'Hello Khanh\nHello Leonard\n'
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_526(self):
        input = '''
            func main(){
                if (true) {
                    putStringLn("This is true");
                }
            }
        '''
        expect = 'This is true\n'
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_527(self):
        input = '''
            func main(){
                if (false) {
                    putStringLn("Should not print");
                }
            }
        '''
        expect = ''
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_528(self):
        input = '''
            func main(){
                if (false) {
                    putStringLn("False branch");
                } else {
                    putStringLn("Else branch");
                }
            }
        '''
        expect = 'Else branch\n'
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_529(self):
        input = '''
            func main(){
                x := 5;
                if (x > 3) {
                    putIntLn(x);
                } else {
                    putIntLn(0);
                }
            }
        '''
        expect = '5\n'
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_530(self):
        input = '''
            func main(){
                x := 10;
                if (x > 0) {
                    if (x < 20) {
                        putStringLn("Between 0 and 20");
                    }
                }
            }
        '''
        expect = 'Between 0 and 20\n'
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_531(self):
        input = '''
            func main(){
                a := 5;
                if (a == 5) {
                    putStringLn("Equal to 5");
                }
            }
        '''
        expect = 'Equal to 5\n'
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_532(self):
        input = '''
            func main(){
                a := 3;
                if (a == 1) {
                    putStringLn("One");
                } else if (a == 2) {
                    putStringLn("Two");
                } else {
                    putStringLn("Other");
                }
            }
        '''
        expect = 'Other\n'
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_533(self):
        input = '''
            func main(){
                a := 5;
                b := 10;
                if (a < b && b == 10) {
                    putStringLn("Condition met");
                }
            }
        '''
        expect = 'Condition met\n'
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_534(self):
        input = '''
            func main(){
                a := 0;
                if (a == 0 || a == 1) {
                    putStringLn("Valid");
                }
            }
        '''
        expect = 'Valid\n'
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_535(self):
        input = '''
            func main(){
                valid := false;
                if (!valid) {
                    putStringLn("Not valid");
                }
            }
        '''
        expect = 'Not valid\n'
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_536(self):
        input = '''
            func main(){
                i := 0;
                for i := 0; i < 3; i := i + 1 {
                    if (i == 1) {
                        putInt(i);
                    }
                }
            }
        '''
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_537(self):
        input = '''
            func main(){
                x := 2;
                if (x == 1) {
                    putInt(1);
                } else if (x == 2) {
                    putInt(2);
                } else {
                    putInt(3);
                }
            }
        '''
        expect = '2'
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_538(self):
        input = '''
            func isEven(x int) boolean {
                return x % 2 == 0;
            }
            func main(){
                if (isEven(4)) {
                    putStringLn("Even");
                }
            }
        '''
        expect = 'Even\n'
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_539(self):
        input = '''
            const flag = true;
            func main(){
                if (flag) {
                    putStringLn("Constant true");
                }
            }
        '''
        expect = 'Constant true\n'
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_540(self):
        input = '''
            func main(){
                s := "abc";
                if (s == "abc") {
                    putStringLn("Matched");
                }
            }
        '''
        expect = 'Matched\n'
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_541(self):
        input = '''func main(){ok := true;if (ok) {putStringLn("OK");};};'''
        expect = 'OK\n'
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_542(self):
        input = '''func main(){a := 10;if (a < 5) {putInt(a);};};'''
        expect = ''
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_543(self):
        input = '''func main(){a := 5;if (a < 3) {putStringLn("Small");} else {if (a == 5) {putStringLn("Exactly five");};};};'''
        expect = 'Exactly five\n'
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_544(self):
        input = '''func main(){a := 5;if (a > 3) {putInt(1);}; if (a < 10) {putInt(2);};};'''
        expect = '12'
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_545(self):
        input = '''func main(){a := 5;if (a == 6) {putStringLn("No");};};'''
        expect = ''
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_546(self):
        input = '''func main(){x := 1;y := 2;if (!(x == y || y < x)) {putStringLn("True branch");};};'''
        expect = 'True branch\n'
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_547(self):
        input = '''func getVal() int {return 10;}; func main(){if (getVal() == 10) {putStringLn("Ten");};};'''
        expect = 'Ten\n'
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_548(self):
        input = '''func main(){x := 1;x := x + 2; if (x == 3) {putStringLn("Three");};};'''
        expect = 'Three\n'
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_549(self):
        input = '''func main(){x := 5;if (x == 5) {x := 10;putInt(x);};};'''
        expect = '10'
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_550(self):
        input = '''func say(msg string){putStringLn(msg);};func main(){if (true) {say("Hello from if");};};'''
        expect = 'Hello from if\n'
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_551(self):
        input = '''
                    func main(){
                        for i := 0; i < 3; i := i + 1 {
                            putIntLn(i);
                        };
                    };
                '''
        expect = '0\n1\n2\n'
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_552(self):
        input = '''
                    func main(){
                        i := 0;
                        for i < 3 {
                            putIntLn(i);
                            i := i + 1;
                        };
                    };
                '''
        expect = '0\n1\n2\n'
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_553(self):
        input = '''
                    func main(){
                        if (true) {
                            i := 1
                            putIntLn(i);
                        };
                    };
                '''
        expect = '1\n'
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_554(self):
        input = '''
                    func factorial(n int) int {
                        if (n <= 1) {
                            return 1;
                        };
                        return n * factorial(n - 1);
                    };

                    func main(){
                        putInt(factorial(5));
                    };
                '''
        expect = '120'
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_555(self):
        input = '''
                    func main(){
                        sum := 0;
                        for i := 1; i <= 5; i := i + 1 {
                            sum := sum + i;
                        };
                        putInt(sum);
                    };
                '''
        expect = '15'
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_556(self):
        input = '''
                    func isEven(n int) boolean {
                        return n % 2 == 0;
                    };

                    func main(){
                        putBool(isEven(4));
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_557(self):
        input = '''
                    func isOdd(n int) boolean {
                        return n % 2 != 0;
                    };

                    func main(){
                        putBool(isOdd(5));
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_558(self):
        input = '''
                    func max(a, b int) int {
                        if (a > b) {
                            return a;
                        };
                        return b;
                    };

                    func main(){
                        putInt(max(10, 20));
                    };
                '''
        expect = '20'
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_559(self):
        input = '''
                    func fib(n int) int {
                        if (n <= 1) {
                            return n;
                        };
                        return fib(n - 1) + fib(n - 2);
                    };

                    func main(){
                        putInt(fib(6));
                    };
                '''
        expect = '8'
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_560(self):
        input = '''
                    func main(){
                        putInt(15);
                    };
                '''
        expect = '15'
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_561(self):
        input = '''
                    func squareSum(a, b int) int {
                        return a*a + b*b;
                    };

                    func main(){
                        putInt(squareSum(3, 4));
                    };
                '''
        expect = '25'
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_562(self):
        input = '''
                    func main(){
                        x := 10;
                        if (x > 5) {
                            putStringLn("Greater");
                        };
                    };
                '''
        expect = 'Greater\n'
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_563(self):
        input = '''
                    func main(){
                        x := 3;
                        if (x % 2 == 0) {
                            putStringLn("Even");
                        } else {
                            putStringLn("Odd");
                        };
                    };
                '''
        expect = 'Odd\n'
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_564(self):
        input = '''
                    func main(){
                        i := 0;
                        for i < 3 {
                            putIntLn(i);
                            i := i + 1;
                        };
                    };
                '''
        expect = '0\n1\n2\n'
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_565(self):
        input = '''
                    func main(){
                        //a := [3]int{1, 2, 3};
                        for i := 1; i < 4; i+=1 {
                            putIntLn(i);
                        };
                    };
                '''
        expect = '1\n2\n3\n'
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_566(self):
        input = '''
                    func main(){
                        str := "abc";
                        putStringLn(str);
                    };
                '''
        expect = 'abc\n'
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_567(self):
        input = '''
                    func addFive(x int) int {
                        return x + 5;
                    };

                    func main(){
                        putInt(addFive(10));
                    };
                '''
        expect = '15'
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_568(self):
        input = '''
                    func fact(n int) int {
                        res := 1;
                        for i := 1; i <= n; i := i + 1 {
                            res := res * i;
                        };
                        return res;
                    };

                    func main(){
                        putInt(fact(4));
                    };
                '''
        expect = '24'
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_569(self):
        input = '''
                    func main(){
                        if (true) {
                            putInt(1);
                        } else {
                            putInt(0);
                        };
                    };
                '''
        expect = '1'
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_570(self):
        input = '''
                    func main(){
                        i := 0;
                        for i < 2 {
                            j := 0;
                            for j < 2 {
                                putInt(i * 2 + j);
                                j := j + 1;
                            };
                            i := i + 1;
                        };
                    };
                '''
        expect = '0123'
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_571(self):
        input = '''
                    func greet(n string){
                        putStringLn("Hello " + n);
                    };

                    func main(){
                        greet("World");
                    };
                '''
        expect = 'Hello World\n'
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_572(self):
        input = '''
                    func check(n int){
                        if (n % 2 == 0) {
                            putStringLn("Even");
                        } else if (n % 3 == 0) {
                            putStringLn("Div by 3");
                        } else {
                            putStringLn("Other");
                        };
                    };

                    func main(){
                        check(9);
                    };
                '''
        expect = 'Div by 3\n'
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_573(self):
        input = '''
                    func main(){
                        s := 0;
                        for i := 1; i <= 100; i := i + 1 {
                            s := s + i;
                        };
                        putInt(s);
                    };
                '''
        expect = '5050'
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_574(self):
        input = '''
                    func main(){
                        for i := 10; i >= 1; i := i - 1 {
                            if (i % 2 == 0) {
                                putInt(i);
                            };
                        };
                    };
                '''
        expect = '108642'
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_575(self):
        input = '''
                    func main(){
                        putFloat(3.14);
                    };
                '''
        expect = '3.14'
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_576(self):
        input = '''
                    func main(){
                        a := 5.0;
                        b := 2.0;
                        putFloat(a / b);
                    };
                '''
        expect = '2.5'
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_577(self):
        input = '''
                    func main(){
                        sum := 0;
                        for i := 1; i < 5; i += 1 {
                            sum += i;
                        };
                        putInt(sum);
                    };
                '''
        expect = '10'
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_578(self):
        input = '''
                    func sum(n int) int {
                        if (n == 0) {
                            return 0;
                        };
                        return n + sum(n - 1);
                    };

                    func main(){
                        putInt(sum(10));
                    };
                '''
        expect = '55'
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_579(self):
        input = '''
                    func main(){
                        putBool(1 < 2 && 3 > 2);
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_580(self):
        input = '''
                    func main(){
                        if (!(false || true) && true) {
                            putString("Nope");
                        } else {
                            putString("Yes");
                        };
                    };
                '''
        expect = 'Yes'
        self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_581(self):
        input = '''
                    func main(){
                        a := true;
                        if (a) {
                            putStringLn("True branch");
                        };
                    };
                '''
        expect = 'True branch\n'
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_582(self):
        input = '''
                    func main(){
                        for i := 0; i < 5; i := i + 1 {
                            if (i % 2 == 0) {
                                putInt(i);
                            };
                        };
                    };
                '''
        expect = '024'
        self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_583(self):
        input = '''
                    func main(){
                        if (false) {
                            putInt(1);
                        } else if (true) {
                            putInt(2);
                        } else {
                            putInt(3);
                        };
                    };
                '''
        expect = '2'
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_584(self):
        input = '''
                    func max(a, b int) int {
                        if (a > b) {
                            return a;
                        } else {
                            return b;
                        }

                    };

                    func main(){
                        putInt(max(8, 5));
                    };
                '''
        expect = '8'
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_585(self):
        input = '''
                    func main(){
                        for i := 1; i <= 3; i := i + 1 {
                            for j := 1; j <= 2; j := j + 1 {
                                putInt(i * j);
                            };
                        };
                    };
                '''
        expect = '123246'
        self.assertTrue(TestCodeGen.test(input,expect,585))

    def test_586(self):
        input = '''
                    func isEven(n int) bool {
                        return n % 2 == 0;
                    };

                    func main(){
                        putBool(isEven(6));
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_587(self):
        input = '''
                    func sumDigits(n int) int {
                        sum := 0;
                        for n > 0 {
                            sum := sum + n % 10;
                            n := n / 10;
                        };
                        return sum;
                    };

                    func main(){
                        putInt(sumDigits(123));
                    };
                '''
        expect = '6'
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_588(self):
        input = '''
                    func fib(n int) int {
                        if (n <= 1) {
                            return n;
                        };
                        return fib(n - 1) + fib(n - 2);
                    };

                    func main(){
                        putInt(fib(6));
                    };
                '''
        expect = '8'
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_589(self):
        input = '''
                    func main(){
                        x := 3;
                        y := 4;
                        z := 5;
                        if (x*x + y*y == z*z) {
                            putString("Pythagorean triple");
                        };
                    };
                '''
        expect = 'Pythagorean triple'
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_590(self):
        input = '''
                    func main(){
                        s := "Hello";
                        s := s + " ";
                        s := s + "World";
                        putStringLn(s);
                    };
                '''
        expect = 'Hello World\n'
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_591(self):
        input = '''
                    func reverse(n int) int {
                        rev := 0;
                        for n != 0 {
                            rev := rev * 10 + n % 10;
                            n := n / 10;
                        };
                        return rev;
                    };

                    func main(){
                        putInt(reverse(123));
                    };
                '''
        expect = '321'
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_592(self):
        input = '''
                    func main(){
                        total := 15
                        putInt(total);
                    };
                '''
        expect = '15'
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_593(self):
        input = '''
                    func power(a, b int) int {
                        res := 1;
                        for i := 0; i < b; i := i + 1 {
                            res := res * a;
                        };
                        return res;
                    };

                    func main(){
                        putInt(power(2, 10));
                    };
                '''
        expect = '1024'
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_594(self):
        input = '''
                    func isPrime(n int) bool {
                        if (n < 2) {
                            return false;
                        };
                        for i := 2; i*i <= n; i := i + 1 {
                            if (n % i == 0) {
                                return false;
                            };
                        };
                        return true;
                    };

                    func main(){
                        putBool(isPrime(11));
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_595(self):
        input = '''
                    func factorial(n int) int {
                        if (n == 0) {
                            return 1;
                        };
                        return n * factorial(n - 1);
                    };

                    func main(){
                        putInt(factorial(5));
                    };
                '''
        expect = '120'
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_596(self):
        input = '''
                    func main(){
                        for i := 1; i <= 5; i := i + 1 {
                            if (i == 3) {
                                continue;
                            };
                            putInt(i);
                        };
                    };
                '''
        expect = '1245'
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_597(self):
        input = '''
                    func main(){
                        x := 0;
                        for true {
                            if (x == 3) {
                                break;
                            };
                            putInt(x);
                            x := x + 1;
                        };
                    };
                '''
        expect = '012'
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_598(self):
        input = '''
                    func main(){
                        i := 1;
                        for i < 4{
                            putInt(i)
                            i += 1
                        }
                    };
                '''
        expect = '123'
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_599(self):
        input = '''
                    func isLeapYear(y int) bool {
                        return (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
                    };

                    func main(){
                        putBool(isLeapYear(2024));
                    };
                '''
        expect = 'true'
        self.assertTrue(TestCodeGen.test(input,expect,599))

    def test_600(self):
        input = '''
                    func main(){
                        a := 10;
                        b := 20;
                        c := 30;
                        if (a < b && b < c) {
                            putString("Increasing");
                        };
                    };
                '''
        expect = 'Increasing'
        self.assertTrue(TestCodeGen.test(input,expect,600))










