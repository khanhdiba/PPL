import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: void main() {} """
    #     input = """func main() {};"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """func foo () {
    #     };"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))
    
    # def test_wrong_miss_close(self):
    #     """Miss ) void main( {}"""
    #     input = """func main({};"""
    #     expect = "Error on line 1 col 11: {"
    #     self.assertTrue(TestParser.checkParser(input,expect,203))
    # def test_wrong_variable(self):
    #     input = """var int;"""
    #     expect = "Error on line 1 col 5: int"
    #     self.assertTrue(TestParser.checkParser(input,expect,204))
    # def test_wrong_index(self):
    #     input = """var i ;"""
    #     expect = "Error on line 1 col 7: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_101(self):
        """Unclosed String"""
        self.assertTrue(TestParser.checkParser("""
            var str string = "Hello"
        """, "successful", 201))

    def test_102(self):
        """Array with Mixed Types (Invalid)"""
        self.assertTrue(TestParser.checkParser("""var arr = [3]int{1, "hello", 3.14};""", "successful", 202))

    def test_103(self):
        """Unexpected Token in Function Declaration"""
        self.assertTrue(TestParser.checkParser("""
            func 123Invalid() {}
        """, "Error on line 2 col 18: 123", 203))

    def test_104(self):
        """Struct Declaration Without Identifier"""
        self.assertTrue(TestParser.checkParser("""
            type struct {
                name string;
            }
        """, "Error on line 2 col 18: struct", 204))

    def test_105(self):
        """Variable Declaration Without Identifier"""
        self.assertTrue(TestParser.checkParser("""
            var  int = 5;
        """, "Error on line 2 col 18: int", 205))

    def test_106(self):
        """Function with Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func missingParam {
                return 42;
            }
        """, "Error on line 2 col 31: {", 206))

    def test_107(self):
        """Array Declaration with Missing Brackets"""
        self.assertTrue(TestParser.checkParser("""
            var arr 5]int;
        """, "Error on line 2 col 21: 5", 207))

    def test_108(self):
        """Misplaced Operator"""
        self.assertTrue(TestParser.checkParser("""
            var result = * 7 + 9;
        """, "Error on line 2 col 26: *", 208))

    def test_109(self):
        """For Loop with Missing Condition"""
        self.assertTrue(TestParser.checkParser("""
            for () {
                print("Hello");
            }
        """, "Error on line 2 col 13: for", 209))

    def test_110(self):
        """If Statement with Incorrect Syntax"""
        self.assertTrue(TestParser.checkParser("""
            if x > 5 {
                print("Wrong syntax");
            }
        """, "Error on line 2 col 13: if", 210))
    def test_111(self):
        """Unexpected Token in Expression"""
        self.assertTrue(TestParser.checkParser("""
            const value = 4 + * 8;
        """, "Error on line 2 col 31: *", 211))

    def test_112(self):
        """Invalid Function Declaration"""
        self.assertTrue(TestParser.checkParser("""
            func func() {
                return 10;
            }
        """, "Error on line 2 col 18: func", 212))
    
    def test_113(self):
        """Missing Colon in Struct Field"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string
                age int;
            }
        """, "successful", 213))
    
    def test_114(self):
        """Incorrect Assignment Operator"""
        self.assertTrue(TestParser.checkParser("""
            var x == 10;
        """, "Error on line 2 col 19: ==", 214))
    
    def test_115(self):
        """Invalid Array Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var numbers [3] int = [1, 2, 3];
        """, "Error on line 2 col 37: ,", 215))
    
    def test_116(self):
        """Function Call Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func main() {
                print "Hello, World!";
            }
        """, "Error on line 3 col 23: \"Hello, World!\"", 216))
    
    def test_117(self):
        """Unexpected Token After Return"""
        self.assertTrue(TestParser.checkParser("""
            func getValue() {
                return 5 6;
            }
        """, "Error on line 3 col 26: 6", 217))
    
    def test_118(self):
        """Unclosed String Literal"""
        self.assertTrue(TestParser.checkParser("""
            var message string = "Hello, world;";
        """, "successful", 218))
    
    def test_119(self):
        """Using a Reserved Keyword as Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var return int = 10;
        """, "Error on line 2 col 17: return", 219))
    
    def test_120(self):
        """Extra Brackets in Function Definition"""
        self.assertTrue(TestParser.checkParser("""
            func double((x int)) {
                return x * 2;
            }
        """, "Error on line 2 col 25: (", 220))
        
    def test_121(self):
        """Struct with Function Pointer"""
        self.assertTrue(TestParser.checkParser("""
            type Calculator struct {
                add func(int, int) int;
            };
        """, "Error on line 3 col 21: func", 221))

    def test_122(self):
        """Function with Default Parameter (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name string = "Guest") {
                print("Hello, " + name);
            }
        """, "Error on line 2 col 36: =", 222))

    def test_123(self):
        """Array with Incorrect Size Declaration"""
        self.assertTrue(TestParser.checkParser("""
            var nums []int = [3]int{1, 2, 3};
        """, "Error on line 2 col 23: ]", 223))

    def test_124(self):
        """Function Without Return Type (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func mystery() {
                return 42;
            }
        """, "successful", 224))

    def test_125(self):
        """Excessive Semicolons"""
        self.assertTrue(TestParser.checkParser("""
            var x int = 10;;;;;
        """, "Error on line 2 col 28: ;", 225))

    def test_126(self):
        """Tuple Declaration (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var pair (int, string) = (5, "hello");
        """, "Error on line 2 col 22: (", 226))

    def test_127(self):
        """Loop Without Condition (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            func main(){
                for () {
                    print("Looping...");
                }
            }
        """, "Error on line 3 col 22: )", 227))

    def test_128(self):
        """String Concatenation Without Operator"""
        self.assertTrue(TestParser.checkParser("""
            var message string = "Hello" "World";
        """, "Error on line 2 col 42: \"World\"", 228))

    def test_129(self):
        """Function with Too Many Parameters"""
        self.assertTrue(TestParser.checkParser("""
            func tooManyParams(a int, b int, c int, d int, e int, f int, g int, h int, i int, j int) {
                print("Too many parameters!");
            }
        """, "successful", 229))

    def test_130(self):
        """Constant Reassignment (Should Fail)"""
        self.assertTrue(TestParser.checkParser("""
            const pi = 3.14;
            pi = 3.14159;
        """, "Error on line 3 col 13: pi", 230))
        
    def test_131(self):
        """Function with No Return Type Specified"""
        self.assertTrue(TestParser.checkParser("""
            func noReturnType(x int, y int) {
                return x + y;
            }
        """, "successful", 231))

    def test_132(self):
        """Array Declaration with Incorrect Bracket Placement"""
        self.assertTrue(TestParser.checkParser("""
            var arr]5[int = {1, 2, 3, 4, 5};
        """, "Error on line 2 col 20: ]", 232))

    def test_133(self):
        """Struct Method Calling Itself Recursively"""
        self.assertTrue(TestParser.checkParser("""
            type Counter struct {
                count int;
                func increment() {
                    self.increment();
                }
            }
        """, "Error on line 4 col 17: func", 233))

    def test_134(self):
        """Invalid Use of Colon in Variable Declaration"""
        self.assertTrue(TestParser.checkParser("""
            var x: int = 10;
        """, "Error on line 2 col 18: :", 234))

    def test_135(self):
        """Function with No Parameters and No Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            func missingParentheses {
                print("Hello");
            }
        """, "Error on line 2 col 37: {", 235))

    def test_136(self):
        """Array with Missing Commas Between Elements"""
        self.assertTrue(TestParser.checkParser("""
            var numbers [5]int = {1 2 3 4 5};
        """, "Error on line 2 col 34: {", 236))

    def test_137(self):
        """Method with Missing Receiver Type in Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                brand string;
            }
            func () drive() {
                print("Driving...");
            }
        """, "Error on line 5 col 19: )", 237))

    def test_138(self):
        """Function Returning Tuple"""
        self.assertTrue(TestParser.checkParser("""
            func getCoordinates() (int, int) {
                return (10, 20);
            }
        """, "Error on line 2 col 35: (", 238))

    def test_139(self):
        """Struct Extending Another Struct Incorrectly"""
        self.assertTrue(TestParser.checkParser("""
            type Animal struct {
                species string;
            }
            type Dog extends Animal {
                breed string;
            }
        """, "Error on line 5 col 22: extends", 239))

    def test_140(self):
        """Use of 'new' Keyword for Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var car = new Car();
        """, "Error on line 2 col 27: Car", 240))
        
    def test_141(self):
        """Struct with Nested Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Engine struct {
                horsepower int
                type string
            }
            
            type Car struct {
                model string
                engine Engine
            }
        """, "Error on line 4 col 17: type", 241))

    def test_142(self):
        """Invalid Variable Initialization"""
        self.assertTrue(TestParser.checkParser("""
            var x int :=;
        """, "Error on line 2 col 23: :=", 242))

    def test_143(self):
        """Struct with Default Values (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            type Phone struct {
                brand string = "Apple"
            }
        """, "Error on line 3 col 30: =", 243))

    def test_144(self):
        """Array with Unspecified Size"""
        self.assertTrue(TestParser.checkParser("""
            var list [3]int = {1, 2, 3};
        """, "Error on line 2 col 31: {", 244))

    def test_145(self):
        """Struct with Method"""
        self.assertTrue(TestParser.checkParser("""
            type Dog struct {
                name string
            }
            func (d Dog) Bark() {
                print("Woof!");
            }
        """, "successful", 245))

    def test_146(self):
        """Function with Incorrect Parameter Syntax"""
        self.assertTrue(TestParser.checkParser("""
            func sum(a int, b int,) int {
                return a + b;
            }
        """, "Error on line 2 col 35: )", 246))

    def test_147(self):
        """Nested If-Else Statement"""
        self.assertTrue(TestParser.checkParser("""
            func check(x int) {
                if (x > 0) {
                    if (x < 10) {
                        print("Single digit");
                    } else {
                        print("Double digit or more");
                    }
                }
            }
        """, "successful", 247))

    def test_148(self):
        """Invalid Return Type"""
        self.assertTrue(TestParser.checkParser("""
            func getData() unknownType {
                return 42;
            }
        """, "successful", 248))

    def test_149(self):
        """Using Reserved Keyword as Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var return int = 5;
        """, "Error on line 2 col 17: return", 249))

    def test_150(self):
        """Function with Missing Return"""
        self.assertTrue(TestParser.checkParser("""
            func getNumber() int {
                var x int = 10;
            }
        """, "successful", 250))

    def test_151(self):
        """Loop with No Condition"""
        self.assertTrue(TestParser.checkParser("""
            func main(){
                for {
                    print("Infinite Loop");
                }
            }            
        """, "Error on line 3 col 21: {", 251))

    def test_152(self):
        """Invalid Character in Variable Name"""
        self.assertTrue(TestParser.checkParser("""
            var num_ber int = 10;
        """, "successful", 252))

    def test_153(self):
        """Valid Interface Implementation"""
        self.assertTrue(TestParser.checkParser("""
            type Animal interface {
                Speak() string
            }
            
            type Cat struct {
                weight int
            }
            
            func (c Cat) Speak() string {
                return "Meow"
            }
        """, "successful", 253))

    def test_154(self):
        """Invalid Operator Usage"""
        self.assertTrue(TestParser.checkParser("""
            var result = 5 / * 2;
        """, "Error on line 2 col 30: *", 254))

    def test_155(self):
        """Function Without Parameters"""
        self.assertTrue(TestParser.checkParser("""
            func greet() {
                print("Hello!");
            }
        """, "successful", 255))

    def test_156(self):
        """Incorrect Use of Colon"""
        self.assertTrue(TestParser.checkParser("""
            var x : int = 10;
        """, "Error on line 2 col 19: :", 256))

    def test_157(self):
        """Nested for Loops"""
        self.assertTrue(TestParser.checkParser("""
            func nestedLoops() {
                var x int = 0;
                for (x < 10) {
                    var y int = 0;
                    for (y < 5) {
                        print(x, y);
                        y += 1;
                    }
                    x += 1;
                }
            }
        """, "successful", 257))

    def test_158(self):
        """Empty Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Empty struct {}
        """, "Error on line 2 col 32: }", 258))

    def test_159(self):
        """Unmatched Parentheses"""
        self.assertTrue(TestParser.checkParser("""
            var y = (5 + (3 * 2;
        """, "Error on line 2 col 32: ;", 259))

    def test_160(self):
        """Function Calling Itself"""
        self.assertTrue(TestParser.checkParser("""
            func recurse(x int) {
                if (x > 0) {
                    recurse(x - 1);
                }
            }
        """, "successful", 260))
        
    def test_161(self):
        """Integer Division"""
        self.assertTrue(TestParser.checkParser("const result = 10 / 2;", "successful", 261))

    def test_162(self):
        """Modulo Operation"""
        self.assertTrue(TestParser.checkParser("const remainder = 10 % 3;", "successful", 262))

    def test_163(self):
        """Bitwise AND Operation"""
        self.assertTrue(TestParser.checkParser("const bitwiseAnd = 5 && 3;", "successful", 263))

    def test_164(self):
        """Bitwise OR Operation"""
        self.assertTrue(TestParser.checkParser("const bitwiseOr = 5 || 3;", "successful", 264))

    def test_165(self):
        """Negative Number Constant"""
        self.assertTrue(TestParser.checkParser("const negValue = -100;", "successful", 265))

    def test_166(self):
        """Array with Mixed Types (Invalid)"""
        self.assertTrue(TestParser.checkParser("""var arr = [1, "hello", 3.14];""", "Error on line 1 col 13: ,", 266))

    def test_167(self):
        """Struct with Uninitialized Field"""
        self.assertTrue(TestParser.checkParser("""
            type Employee struct {
                name string;
                salary float;
            }
        """, "successful", 267))

    def test_168(self):
        """Function with No Return"""
        self.assertTrue(TestParser.checkParser("""
            func doSomething() {
                var x = 5;
                x += 10;
            }
        """, "successful", 268))

    def test_169(self):
        """Function Returning Struct"""
        self.assertTrue(TestParser.checkParser("""
            func createPerson() Person {
                return Person{name: "John", age: 30};
            }
        """, "successful", 269))

    def test_170(self):
        """While Loop"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for x < 10 {
                    x += 1;
                }
            }
        """, "successful", 270))

    def test_171(self):
        """Invalid For Loop Syntax"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for (x < 10) x += 1;
            }
        """, "Error on line 3 col 30: x", 271))

    def test_172(self):
        """Function with Multiple Return Types"""
        self.assertTrue(TestParser.checkParser("""
            func getData() (int, string) {
                return 10, "hello";
            }
        """, "Error on line 2 col 28: (", 272))

    def test_173(self):
        """Switch Case Statement"""
        self.assertTrue(TestParser.checkParser("""
            func checkValue(x int) {
                if (x) {
                    print("One");
                }else if(y){
                    print("Two");
                } else{
                    print("Other");
                }
            }
        """, "successful", 273))

    def test_174(self):
        """Nested If-Else Statement"""
        self.assertTrue(TestParser.checkParser("""
            func checkValue(x int) {
                if (x > 0) {
                    if (x < 10) {
                        print("Single digit positive");
                    } else {
                        print("Two-digit or more");
                    }
                } else {
                    print("Negative or zero");
                }
            }
        """, "successful", 274))

    def test_175(self):
        """Assigning Function Call to Variable"""
        self.assertTrue(TestParser.checkParser("""
            func getNumber() int {
                return 42;
            }
            var num = getNumber();
        """, "successful", 275))

    def test_176(self):
        """Accessing Array Out of Bounds (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            var arr [5]int;
            const value = arr[10];
        """, "successful", 276))

    def test_177(self):
        """Struct with Method Definition (Invalid)"""
        self.assertTrue(TestParser.checkParser("""
            type Car struct {
                func drive() {
                    print("Driving");
                }
            }
        """, "Error on line 3 col 17: func", 277))

    def test_178(self):
        """Using Struct as Function Argument"""
        self.assertTrue(TestParser.checkParser("""
            type Person struct {
                name string;
                age int;
            }
            func greet(p Person) {
                print("Hello " + p.name);
            }
        """, "successful", 278))

    def test_179(self):
        """Using Struct Inside Another Struct"""
        self.assertTrue(TestParser.checkParser("""
            type Address struct {
                city string;
                zip int;
            }
            type Person struct {
                name string;
                addr Address;
            }
        """, "successful", 279))

    def test_180(self):
        """Function with Incorrect Return Type"""
        self.assertTrue(TestParser.checkParser("""
            func getName() int {
                return "John";
            }
        """, "successful", 280))
        
    def test_181(self):
        """Complex Arithmetic Expression"""
        self.assertTrue(TestParser.checkParser("""
            const result = ((a + b) * c) / (d - e) + f;
        """, "successful", 281))

    def test_182(self):
        """Struct with Nested Structs"""
        self.assertTrue(TestParser.checkParser("""
            type Address struct {
                street string;
                city string;
            }
            type Person struct {
                name string;
                address Address;
            }
        """, "successful", 282))

    def test_183(self):
        """Nested Array and Struct Access"""
        self.assertTrue(TestParser.checkParser("""
            func foo(){
                matrix[0][1+1] := [2][2]float{{1.1, a, 0., 7.e-9}, {3.13, 4.4, 2.0e10}}
                data[99-a*b+c/d%f].info.details[2] := StructType{field1: 10, field2: "text"};
            }

            func test_assign() {
                result := records[5].entries[i-7].compute(42,g,h,(u+7)*3,p-9);
            }
        """, "successful", 283))

    def test_184(self):
        """Array with Invalid Syntax"""
        self.assertTrue(TestParser.checkParser("var arr [5] = {1, 2, 3, 4, 5};", "Error on line 1 col 13: =", 284))

    def test_185(self):
        """Interface with Method"""
        self.assertTrue(TestParser.checkParser("""
            type Drawable interface {
                Draw() void;
            }
        """, "successful", 285))

    def test_186(self):
        """Invalid Function Definition with Missing Parentheses"""
        self.assertTrue(TestParser.checkParser("func sum a, b int { return a + b; }", "Error on line 1 col 10: a", 286))

    def test_187(self):
        """Valid for Loop"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                for (x < 10) {
                    x += 1;
                }
            }
        """, "successful", 287))

    def test_188(self):
        """Invalid While Loop Missing Condition"""
        self.assertTrue(TestParser.checkParser("""
            func loop() {
                while {
                    x += 1;
                }
            }
        """, "Error on line 3 col 23: {", 288))

    def test_189(self):
        """Chained Function Calls"""
        self.assertTrue(TestParser.checkParser("const result = foo().bar()[4][5].baz();", "successful", 289))

    def test_190(self):
        """Function with Boolean Return"""
        self.assertTrue(TestParser.checkParser("""
            func isEven(num int) bool {
                return num % 2 == 0;
            }
        """, "successful", 290))

    def test_191(self):
        """Complex Logical Expression"""
        self.assertTrue(TestParser.checkParser("const check = (a && b) || !(c && d);", "successful", 291))

    def test_192(self):
        """Struct with Invalid Array Field"""
        self.assertTrue(TestParser.checkParser("""
            type Student struct {
                grades [int];
            }
        """, "Error on line 3 col 25: int", 292))

    def test_193(self):
        """Function with Parameter"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name, home, file  string, year date) {
                print("Hello, " + name);
            }
        """, "successful", 293))

    def test_194(self):
        """Function with Default Parameter"""
        self.assertTrue(TestParser.checkParser("""
            func greet(name string = "Guest") {
                print("Hello, " + name);
            }
        """, "Error on line 2 col 36: =", 294))

    def test_195(self):
        """Struct Array Initialization"""
        self.assertTrue(TestParser.checkParser("""
            type Employee struct {
                name string;
            }
            var employees [3]Employee = [3]Employee{
                {"Alice","David"},
                {"Bob"},
                {"Charlie"}};
        """, "successful", 295))

    def test_196(self):
        """Loop with Array Iteration"""
        self.assertTrue(TestParser.checkParser("""
            func arrayLoop() {
                var arr [5]int = [5]int{1, 2, 3, 4, 5};
                for i := 0; i < 5; i += 1 {
                    print(arr[i]);
                }
            }
        """, "successful", 296))

    def test_197(self):
        """Loop with Struct Array"""
        self.assertTrue(TestParser.checkParser("""
            func structArrayLoop() {
                for i := 0; i < 10; i += 1 {
                    people[i].name := "Person" + str(i);
                }
            }
        """, "successful", 297))

    def test_198(self):
        """Loop with Function Call and Condition"""
        self.assertTrue(TestParser.checkParser("""
            func conditionalFunctionLoop() {
                for i := 0; i < 5; i += 1 {
                    if (checkValue(i)) {
                        print(i);
                    }
                }
            }
        """, "successful", 298))

    def test_199(self):
        """Nested Struct Initialization"""
        self.assertTrue(TestParser.checkParser("""
            type Engine struct {
                horsepower int;
            }
            type Car struct {
                model string;
                engine Engine;
            }
            const myCar = Car{a: "Tesla", b: Engine{c: 400}};
        """, "successful", 299))

    def test_200(self):
        """Invalid Missing Semicolon"""
        self.assertTrue(TestParser.checkParser("const x = 10 const y = 20;", "Error on line 1 col 14: const", 300))

    def test_201(self):
        """Invalid Missing Semicolon"""
        self.assertTrue(TestParser.checkParser("""func main() {
                                                arr := [2][2][2][2][2]int{{{{{1, 2}, {3, 4}}, {{5, 6}, {7, 8}}}, {{{9, 10}, {11, 12}}, {{13, 14}, {15, 16}}}}, {{{{17, 18}, {19, 20}}, {{21, 22}, {23, 24}}}, {{{25, 26}, {27, 28}}, {{29, 30}, {31, 32}}}}}
                                               };""", "successful", 301))
