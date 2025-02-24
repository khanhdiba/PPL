# import unittest
# from TestUtils import TestLexer

# class LexerSuite(unittest.TestCase):
      
#     def test_001(self):
#         """test identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
#     def test_002(self):
#         self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",102))

#     def test_003(self):
#         """test keyword var"""
#         self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",103))

#     def test_004(self):
#         """test keyword func"""
#         self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",104))
    
#     def test_005(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""int float string123""","""int,float,string123,<EOF>""",105))

#     def test_006(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""if else return""", """if,else,return,<EOF>""", 106))

#     def test_007(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""func type struct""", """func,type,struct,<EOF>""", 107))

#     def test_008(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""boolean const var""", """boolean,const,var,<EOF>""", 108))

#     def test_009(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""continue break range""", """continue,break,range,<EOF>""", 109))

#     def test_010(self):
#         """Keyword"""
#         self.assertTrue(TestLexer.checkLexeme("""nil true false""", """nil,true,false,<EOF>""", 110))

#     def test_011(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""+ - * / %""", """+,-,*,/,%,<EOF>""", 111))

#     def test_012(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""== != < > <= >=""", """==,!=,<,>,<=,>=,<EOF>""", 112))

#     def test_013(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""&& || !""", """&&,||,!,<EOF>""", 113))

#     def test_014(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""=""", """=,<EOF>""", 114))

#     def test_015(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme(""":=""", """:=,<EOF>""", 115))

#     def test_016(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""+= -= *= /=""", """+=,-=,*=,/=,<EOF>""", 116))

#     def test_017(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""%=""", """%=,<EOF>""", 117))

#     def test_018(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme(""". . .""", """.,.,.,<EOF>""", 118))

#     def test_019(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""+ - * / % == !=""", """+,-,*,/,%,==,!=,<EOF>""", 119))

#     def test_020(self):
#         """Operators"""
#         self.assertTrue(TestLexer.checkLexeme("""<= >= && || ! .""", """<=,>=,&&,||,!,.,<EOF>""", 120))

#     def test_021(self):
#         """Separators"""
#         self.assertTrue(TestLexer.checkLexeme("""( ) { } [ ]""", """(,),{,},[,],<EOF>""", 121))

#     def test_022(self):
#         """Separators"""
#         self.assertTrue(TestLexer.checkLexeme("""( { [ ) } ]""", """(,{,[,),},],<EOF>""", 122))

#     def test_023(self):
#         """Separators"""
#         self.assertTrue(TestLexer.checkLexeme(""", ; :""", """,,;,:,<EOF>""", 123))

#     def test_024(self):
#         """Separators"""
#         self.assertTrue(TestLexer.checkLexeme("""(,) {;} [:]""", """(,,,),{,;,},[,:,],<EOF>""", 124))

#     def test_025(self):
#         """Separators"""
#         self.assertTrue(TestLexer.checkLexeme("""( [ { , ; } ] )""", """(,[,{,,,;,},],),<EOF>""", 125))

#     def test_026(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""abc XYZ _var""", """abc,XYZ,_var,<EOF>""", 126))

#     def test_027(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""hello world123 _underscore""", """hello,world123,_underscore,<EOF>""", 127))

#     def test_028(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""x y z""", """x,y,z,<EOF>""", 128))

#     def test_029(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""var1 var_2 VAR_3""", """var1,var_2,VAR_3,<EOF>""", 129))

#     def test_030(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""_leading _123valid a_b_c""", """_leading,_123valid,a_b_c,<EOF>""", 130))

#     def test_031(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""ThisIsAnIdentifier anotherOne yetAnother""", """ThisIsAnIdentifier,anotherOne,yetAnother,<EOF>""", 131))

#     def test_032(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""ID123 name_456 final_var""", """ID123,name_456,final_var,<EOF>""", 132))

#     def test_033(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""_privateVar _testCase _sample""", """_privateVar,_testCase,_sample,<EOF>""", 133))

#     def test_034(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""MixedCASE lowerUPPER _Mix123""", """MixedCASE,lowerUPPER,_Mix123,<EOF>""", 134))

#     def test_035(self):
#         """Identifiers"""
#         self.assertTrue(TestLexer.checkLexeme("""simpleVar complex_Variable another123""", """simpleVar,complex_Variable,another123,<EOF>""", 135))

#     def test_036(self):
#         """Decimal numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0 1 12345 987654321""", """0,1,12345,987654321,<EOF>""", 136))

#     def test_037(self):
#         """Decimal numbers with leading zeros"""
#         self.assertTrue(TestLexer.checkLexeme("""007 000123""", """0,0,7,0,0,0,123,<EOF>""", 137))

#     def test_038(self):
#         """Binary numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0b101 0B1101 0b0 0B1""", """0b101,0B1101,0b0,0B1,<EOF>""", 138))

#     def test_039(self):
#         """Invalid binary numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0b102 0B201""", """0b10,2,0,B201,<EOF>""", 139))  # Should trigger an error

#     def test_040(self):
#         """Octal numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0o7 0O1234 0o0 0O777""", """0o7,0O1234,0o0,0O777,<EOF>""", 140))

#     def test_041(self):
#         """Invalid octal numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0o89 0O908""", """0,o89,0,O908,<EOF>""", 141))  # Should trigger an error

#     def test_042(self):
#         """Hexadecimal numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0x1A3F 0Xabcdef 0x0 0XFF""", """0x1A3F,0Xabcdef,0x0,0XFF,<EOF>""", 142))

#     def test_043(self):
#         """Hexadecimal numbers with uppercase"""
#         self.assertTrue(TestLexer.checkLexeme("""0XABCDEF 0X123456""", """0XABCDEF,0X123456,<EOF>""", 143))

#     def test_044(self):
#         """Invalid hexadecimal numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0xGHIJ 0X12G3""", """0,xGHIJ,0X12,G3,<EOF>""", 144))  # Should trigger an error

#     def test_045(self):
#         """Mixed number formats"""
#         self.assertTrue(TestLexer.checkLexeme("""123 0b101 0O77 0xAF""", """123,0b101,0O77,0xAF,<EOF>""", 145))

#     def test_046(self):
#         """Simple floating-point numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""0.5 123.456 10.0""", """0.5,123.456,10.0,<EOF>""", 146))

#     def test_047(self):
#         """Floating-point numbers with leading/trailing dots"""
#         self.assertTrue(TestLexer.checkLexeme(""".123 456.""", """.,123,456.,<EOF>""", 147))  # Should handle edge cases

#     def test_048(self):
#         """Floating-point numbers with exponents"""
#         self.assertTrue(TestLexer.checkLexeme("""1.23e10 4.56E-5 7.89E+2""", """1.23e10,4.56E-5,7.89E+2,<EOF>""", 148))

#     def test_049(self):
#         """Floating-point numbers with missing digits"""
#         self.assertTrue(TestLexer.checkLexeme(""".e10 123.e-5""", """.,e10,123.e-5,<EOF>""", 149))  # May need handling

#     def test_050(self):
#         """Floating-point numbers with positive/negative signs"""
#         self.assertTrue(TestLexer.checkLexeme("""+3.14 -0.99 +2.71E+4 -6.022e23""", """+,3.14,-,0.99,+,2.71E+4,-,6.022e23,<EOF>""", 150))

#     def test_051(self):
#         """Invalid floating-point numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""1.23e 4.56E+""", """1.23,e,4.56,E,+,<EOF>""", 151))  # Should trigger an error

#     def test_052(self):
#         """Floating-point numbers with multiple dots"""
#         self.assertTrue(TestLexer.checkLexeme("""1.2.3 4..5""", """1.2,.,3,4.,.,5,<EOF>""", 152))  # Should tokenize properly

#     def test_053(self):
#         """float lit"""
#         self.assertTrue(TestLexer.checkLexeme("""0.0""", """0.0,<EOF>""", 153))

#     def test_054(self):
#         """Exponent-only numbers"""
#         self.assertTrue(TestLexer.checkLexeme("""1e10 2E-3 3.0e+2""", """1,e10,2,E,-,3,3.0e+2,<EOF>""", 154))

#     def test_055(self):
#         """Mixed floating-point formats"""
#         self.assertTrue(TestLexer.checkLexeme("""3.1415 2E10 8.99e-2""", """3.1415,2,E10,8.99e-2,<EOF>""", 155))

#     def test_056(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Onii-chan no Baka" ""","""\"Onii-chan no Baka\",<EOF>""", 156))

#     def test_057(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Aishitemasu\\n" ""","""\"Aishitemasu\\n\",<EOF>""", 157))

#     def test_058(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Domain Expansion \\t Black Flash" ""","""\"Domain Expansion \\t Black Flash\",<EOF>""", 158))

#     def test_059(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.checkLexeme(""" "Oppai \\r Oppai \\r Oppai" ""","\"Oppai \\r Oppai \\r Oppai\",<EOF>", 159))

#     def test_060(self):
#         """Literals String"""
#         self.assertTrue(TestLexer.checkLexeme(""" "" """,""""",<EOF>""", 160))
    
#     def test_061(self):
#         """Test literals: string with escape sequences"""
#         self.assertTrue(TestLexer.checkLexeme('"Hello \\n World"', '"Hello \\n World",<EOF>', 161))

#     def test_062(self):
#         """Test literals: empty string"""
#         self.assertTrue(TestLexer.checkLexeme('""', '"",<EOF>', 162))

#     def test_063(self):
#         """Test literals: integer decimal"""
#         self.assertTrue(TestLexer.checkLexeme('12345', '12345,<EOF>', 163))

#     def test_064(self):
#         """Test literals: integer binary"""
#         self.assertTrue(TestLexer.checkLexeme('0b1010', '0b1010,<EOF>', 164))

#     def test_065(self):
#         """Test literals: integer octal"""
#         self.assertTrue(TestLexer.checkLexeme('0o123', '0o123,<EOF>', 165))

#     def test_066(self):
#         """Test literals: integer hexadecimal"""
#         self.assertTrue(TestLexer.checkLexeme('0x1A3F', '0x1A3F,<EOF>', 166))

#     def test_067(self):
#         """Test literals: float with exponent"""
#         self.assertTrue(TestLexer.checkLexeme('123.45e-2', '123.45e-2,<EOF>', 167))

#     def test_068(self):
#         """Test keywords: if-else"""
#         self.assertTrue(TestLexer.checkLexeme('if else', 'if,else,<EOF>', 168))

#     def test_069(self):
#         """Test keywords: for-range"""
#         self.assertTrue(TestLexer.checkLexeme('for range', 'for,range,<EOF>', 169))

#     def test_070(self):
#         """Test operators: arithmetic"""
#         self.assertTrue(TestLexer.checkLexeme('+ - * / %', '+,-,*,/,%,<EOF>', 170))

#     def test_071(self):
#         """Test operators: logical"""
#         self.assertTrue(TestLexer.checkLexeme('&& || !', '&&,||,!,<EOF>', 171))

#     def test_072(self):
#         """Test operators: comparison"""
#         self.assertTrue(TestLexer.checkLexeme('== != < > <= >=', '==,!=,<,>,<=,>=,<EOF>', 172))

#     def test_073(self):
#         """Test separators: brackets"""
#         self.assertTrue(TestLexer.checkLexeme('(){}[]', '(,),{,},[,],<EOF>', 173))

#     def test_074(self):
#         """Test separators: comma and semicolon"""
#         self.assertTrue(TestLexer.checkLexeme(',;', ',,;,<EOF>', 174))

#     def test_075(self):
#         """Test identifier: valid identifiers"""
#         self.assertTrue(TestLexer.checkLexeme('var1 _var2', 'var1,_var2,<EOF>', 175))

#     def test_076(self):
#         """Test identifier: invalid identifier"""
#         self.assertTrue(TestLexer.checkLexeme('1var', '1,var,<EOF>', 176))

#     def test_077(self):
#         """Test literals: illegal escape sequence"""
#         self.assertTrue(TestLexer.checkLexeme('"Hello \\f"', 'Illegal escape in string: "Hello \\f', 177))

#     def test_078(self):
#         """Test literals: unclosed string"""
#         self.assertTrue(TestLexer.checkLexeme('"Hello World', 'Unclosed string: "Hello World', 178))

#     def test_079(self):
#         """Test literals: boolean"""
#         self.assertTrue(TestLexer.checkLexeme('true false', 'true,false,<EOF>', 179))

#     def test_080(self):
#         """Test keywords: return break continue"""
#         self.assertTrue(TestLexer.checkLexeme('return break continue', 'return,break,continue,<EOF>', 180))

#     def test_081(self):
#         """Test keywords: func type struct"""
#         self.assertTrue(TestLexer.checkLexeme('func type struct', 'func,type,struct,<EOF>', 181))

#     def test_082(self):
#         """Test operators: assignment"""
#         self.assertTrue(TestLexer.checkLexeme('= := += -= *= /= %=', '=,:=,+=,-=,*=,/=,%=,<EOF>', 182))

#     def test_083(self):
#         """Test complex expression"""
#         self.assertTrue(TestLexer.checkLexeme('a + b * c - d / e % f', 'a,+,b,*,c,-,d,/,e,%,f,<EOF>', 183))

#     def test_084(self):
#         """Test array indexing"""
#         self.assertTrue(TestLexer.checkLexeme('arr[1][2]', 'arr,[,1,],[,2,],<EOF>', 184))

#     def test_085(self):
#         """Test function call"""
#         self.assertTrue(TestLexer.checkLexeme('foo(1,2,3)', 'foo,(,1,,,2,,,3,),<EOF>', 185))

#     def test_086(self):
#         """Test struct literal"""
#         self.assertTrue(TestLexer.checkLexeme('Person{name:"John",age:30}', 'Person,{,name,:,"John",,,age,:,30,},<EOF>', 186))

#     def test_087(self):
#         """Test interface declaration"""
#         self.assertTrue(TestLexer.checkLexeme('type I interface { foo() }', 'type,I,interface,{,foo,(,),},<EOF>', 187))

#     def test_088(self):
#         """Test for statement"""
#         self.assertTrue(TestLexer.checkLexeme('for i := range arr', 'for,i,:=,range,arr,<EOF>', 188))

#     def test_089(self):
#         """Test method declaration"""
#         self.assertTrue(TestLexer.checkLexeme('func (p Person) walk() {}', 'func,(,p,Person,),walk,(,),{,},<EOF>', 189))

#     def test_090(self):
#         """Test comment: single line"""
#         self.assertTrue(TestLexer.checkLexeme('// this is a comment', '<EOF>', 190))

#     def test_091(self):
#         """Test comment: multi-line"""
#         self.assertTrue(TestLexer.checkLexeme('/* comment */', '<EOF>', 191))

#     def test_092(self):
#         """Test expression with parentheses"""
#         self.assertTrue(TestLexer.checkLexeme('(a+b)*(c-d)', '(,a,+,b,),*,(,c,-,d,),<EOF>', 192))

#     def test_093(self):
#         """Test nested array declaration"""
#         self.assertTrue(TestLexer.checkLexeme('var arr [5][6]int', 'var,arr,[,5,],[,6,],int,<EOF>', 193))

#     def test_094(self):
#         """Test variable assignment"""
#         self.assertTrue(TestLexer.checkLexeme('x = 5', 'x,=,5,<EOF>', 194))

#     def test_095(self):
#         """Test invalid character"""
#         self.assertTrue(TestLexer.checkLexeme('@', 'ErrorToken @', 195))

#     def test_096(self):
#         """Test keywords: const var"""
#         self.assertTrue(TestLexer.checkLexeme('const var', 'const,var,<EOF>', 196))

#     def test_097(self):
#         """Test call statement with expression"""
#         self.assertTrue(TestLexer.checkLexeme('foo(a+b)', 'foo,(,a,+,b,),<EOF>', 197))

#     def test_098(self):
#         """Test complex statement"""
#         self.assertTrue(TestLexer.checkLexeme('if x > 0 { y = x }', 'if,x,>,0,{,y,=,x,},<EOF>', 198))

#     def test_099(self):
#         """Test array literal"""
#         self.assertTrue(TestLexer.checkLexeme('{1,2,3}', '{,1,,,2,,,3,},<EOF>', 199))

#     def test_100(self):
#         """Test complex program snippet"""
#         self.assertTrue(TestLexer.checkLexeme('func main() { var x = 1; if x == 1 { x = 2 } }', 'func,main,(,),{,var,x,=,1,;,if,x,==,1,{,x,=,2,},},<EOF>', 200))

import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_001(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",1))
    
    def test_002(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",2))
    def test_003(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",3))
    def test_004(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",4))
    def test_005(self):
        """test keyword func"""
        input = """
            if
            }
            ]
            )
            """
        expect = "if,},;,],;,),;,<EOF>"

        self.assertTrue(TestLexer.checkLexeme(input,expect,5))

    def test_006(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 6))
    
    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 7))
    
    def test_008(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", 8))
        
    def test_009(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN","<EOF>", 9))

    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 10))

    def test_011(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 11))

    def test_012(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", 12))
    
    def test_013(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", 13))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_014(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 14))

    def test_015(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>", 15))

    def test_016(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 16))

    def test_017(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 17))

    def test_018(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 18))

    def test_019(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 19))

    def test_020(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 20))

    def test_021(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>",21))

    def test_022(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 22))

    def test_023(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>", 23))

    def test_024(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>", 24))
        
    def test_025(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]","[,],<EOF>", 25))
        
    def test_026(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_VOTien","_VOTien,<EOF>", 26))
        
    def test_027(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 27))
        
    def test_028(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 28))
    
    def test_029(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 29))
    
    def test_030(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", 30))
        
    def test_031(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN","<EOF>",31))

    def test_032(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 32))

    def test_033(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 33))

    def test_034(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", 34))
    
    def test_035(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", 35))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_036(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 36))

    def test_037(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>",37))

    def test_038(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 38))

    def test_039(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 39))

    def test_040(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 40))

    def test_041(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 41))

    def test_042(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 42))

    def test_043(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 43))

    def test_044(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 44))

    def test_045(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>",45))

    def test_046(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 46))

    def test_047(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 47))

    def test_048(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 48))

    def test_049(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 49))

    def test_050(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 50))

    def test_051(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 51))

    def test_052(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 52))

    def test_053(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "votien" """, "\"votien\",<EOF>", 53))

    def test_054(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r" """, "\"\\r\",<EOF>", 54))

    def test_055(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", 55))

    def test_056(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" ^ """, "ErrorToken ^", 56))

    def test_057(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 57))

    def test_058(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 58))

    def test_059(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 59))

    def test_060(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 60))

    def test_061(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 61))

    def test_062(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" 123" """, "123,Unclosed string: \" ", 62))

    def test_063(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "123
        " """, "Unclosed string: \"123", 63))

    def test_064(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "&\\&" """, "Illegal escape in string: \"&\\&", 64))

    def test_065(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\z" """, "Illegal escape in string: \"\\z", 65))

    def test_066(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\z" """, "Illegal escape in string: \"\\z", 66))

    def test_067(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12","12,<EOF>", 67))
        
    def test_068(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11","0x11,<EOF>", 68))
    
    def test_069(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 69))
    
    def test_070(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN \\r" ""","\"VOTIEN \\r\",<EOF>", 70))
        
    def test_071(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// VOTIEN","<EOF>",71))

    def test_072(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 72))

    def test_073(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^","ErrorToken ^", 73))

    def test_074(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\n" ""","Unclosed string: \"VOTIEN", 74))
    
    def test_075(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme(""" "VOTIEN\\f" ""","Illegal escape in string: \"VOTIEN\\f", 75))
        
    #!!! 87 test yêu cầu code chấm sau
    def test_076(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("else for return func type struct interface string int float boolean const var continue break range nil true false", "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>", 76))

    def test_077(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=", "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>",77))

    def test_078(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 78))

    def test_079(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 79))

    def test_080(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 80))

    def test_081(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 81))

    def test_082(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 82))

    def test_083(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 83))

    def test_084(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 84))

    def test_085(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>",85))

    def test_086(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 86))

    def test_087(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 87))

    def test_088(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 88))

    def test_089(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 89))

    def test_090(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 90))

    def test_091(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 91))

    def test_092(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 92))

    def test_093(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "votien" """, "\"votien\",<EOF>", 93))

    def test_094(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r" """, "\"\\r\",<EOF>", 94))

    def test_095(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme(""" "\\r \\r \\r" """, "\"\\r \\r \\r\",<EOF>", 95))

    def test_096(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" ^ """, "ErrorToken ^", 96))

    def test_097(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 97))

    def test_098(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 98))

    def test_099(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 99))

    def test_100(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 100))
