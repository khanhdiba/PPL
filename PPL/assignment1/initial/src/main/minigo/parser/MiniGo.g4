//Dinh Ba Khanh - 2252323
grammar MiniGo;

@lexer::header {
from lexererr import *
#Dinh Ba Khanh - 2252323
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

def handleNewline(self):
    if self.preType in {
        self.ID, self.BIN, self.OCT, self.DEC, self.HEX, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STR_LIT, self.NIL,
        self.RETURN, self.CONTINUE, self.BREAK,
        self.RCB, self.RSB, self.RRB,
        self.INT, self.FLOAT, self.BOOLEAN, self.STRING
    }:
        self.type = self.SEMICOLON
        self.text = ";" 
    else:
        self.skip()
}

options{
    language = Python3;
}

//--------------------------------LEXER------------------------------//
//KEYWORDS
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';

//OPERATORS
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';

AND: '&&';
OR: '||';
NOT: '!';

ASSIGN: '=';
ASSIGN_OP: ':=';
ASSIGN_ADD: '+=';
ASSIGN_SUB: '-=';
ASSIGN_MUL: '*=';
ASSIGN_DIV: '/=';
ASSIGN_MOD: '%=';

DOT: '.';

//SEPARATOR
LRB: '(';
RRB: ')';

LCB: '{';
RCB: '}';

LSB: '[';
RSB: ']';

COMMA: ',';
SEMICOLON: ';';
COLON: ':';

//IDENTIFIERS
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//LITERAL
// int_lit: DEC | BIN | OCT | HEX;
DEC: [0-9] | [1-9][0-9]+;
BIN: [0] [Bb] [01]+;
OCT: [0] [Oo] [0-7]+;
HEX: [0] [Xx] [0-9A-Fa-f]+;


fragment DIGIT: [0-9]+;
fragment EXP: [Ee] [+-]? DIGIT;
FLOAT_LIT: DIGIT [.] [0-9]* EXP?;

fragment ESCAPE_SEQUENCE:  '\\' [ntr"\\];
fragment CHAR_LIT: ~[\\"\n\t\r] | ESCAPE_SEQUENCE;
STR_LIT: '"' CHAR_LIT* '"';


// bool_lit: TRUE | FALSE;

// nil_lit: NIL;

//COMMENT, NEWLINE, WHITE SPACE

SINGLE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_COMMENT: '/*' (MULTI_COMMENT |.)*? '*/' -> skip;
NEWLINE: ('\r\n' | '\n'){ self.handleNewline() };
WS: [ \t\f\r]+ -> skip;

//ERROR
ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' CHAR_LIT* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[0:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[0:-1])
    else:
        raise UncloseString(self.text[0:])
};

fragment ILLEGAL_CHAR: '\\' ~[ntr"\\];
ILLEGAL_ESCAPE: '"' CHAR_LIT* ILLEGAL_CHAR {
    raise IllegalEscape(self.text[0:])
};

//-----------------------PARSER-----------------------//
// program: list_expr;
program: list_declare EOF;
// program: (CONST ID ASSIGN expr SEMICOLON) EOF;      //task 1 assg 2
list_declare: declared list_declare | declared ;

//LITERALS
int_lit: DEC | BIN | OCT | HEX ;
literal:
    int_lit
    | FLOAT_LIT
    | STR_LIT
    | TRUE
    | FALSE
    | NIL
    | array_literal
    | struct_literal;

//RECHECK IF ARRAY LITERAL INSIDE BRACKETS CAN NULLABLE?
array_literal: array_init array_type LCB list_array_index RCB;
array_type: INT | FLOAT | BOOLEAN | STRING | ID;
array_init: LSB (int_lit | ID) RSB array_init?;     //this is array dimension, accecpt [const_val], [0x12], [0b101], [0o454]
array_index:
    int_lit
    | FLOAT_LIT
    | STR_LIT
    | TRUE
    | FALSE
    | NIL
    | ID            //just add on H14/02 4:40pm
    | struct_literal
    | LCB list_array_index RCB; //index here is a {1,2,3}, {1,a,c},...

list_array_index: array_index COMMA list_array_index | array_index ;

//just fix here 13/02 3:12pm
struct_literal: ID LCB list_element  RCB;
list_element: ID COLON expr COMMA list_element | ID COLON expr | ;

//EXPRESSION
list_expr: expr COMMA list_expr | expr ;
expr: expr OR expr1 | expr1;
expr1: expr1 AND expr2 | expr2;
expr2: expr2 log_op expr3 | expr3;
expr3: expr3 add_op expr4 | expr4;
expr4: expr4 mul_op expr5 | expr5;
expr5: una_op expr5 | expr6;
expr6: expr6 LSB expr RSB | expr6 DOT (ID | func_call) | expr7;
expr7: literal | ID | LRB expr RRB | func_call ;

//expr2
log_op: (EQUAL | NOT_EQUAL | LT | LTE | GT | GTE) ;
//expr3
add_op: (ADD | SUB);
//expr4
mul_op: (MUL | DIV | MOD);
//expr5
una_op: (SUB | NOT | ADD);

parameter: expr COMMA parameter | expr;
func_call: ID LRB parameter? RRB;

//DECLARATION
declared:
    var_declared
    | const_declared
    | func_declared
    | method_declared
    | struct_declared
    | interface_declared;

dec_type: array_init? INT | array_init? FLOAT | array_init? BOOLEAN | array_init? STRING | array_init? ID;
// array_init_type: LSB DEC RSB array_init?;
// var declaration //
var_declared: var_full | var_type | var_init;
// var x int = 1 ;
var_full: VAR ID dec_type (ASSIGN expr) ignore;
// var x int ;
var_type: VAR ID dec_type ignore;
//var x = 1;
var_init: VAR ID (ASSIGN expr) ignore;


// const declaration //
const_declared: CONST ID ASSIGN expr ignore;

// function declaration //
func_declared: FUNC ID para dec_type? body_block ignore;

// method declaration //
method_declared: FUNC method_struct_name ID para dec_type? body_block ignore;
method_struct_name: (LRB ID ID RRB) ;


// struct declaration //
struct_declared: TYPE ID STRUCT struct_body ignore;

struct_body: (LCB list_struct_declared RCB) ;
list_struct_declared: struct_index list_struct_declared | struct_index ;
struct_index: (ID dec_type ignore) ;

// interface declartion //
interface_declared: TYPE ID INTERFACE interface_body ignore;

interface_body: (LCB list_interface_declared RCB) ;
list_interface_declared: line_inter list_interface_declared | line_inter;
line_inter: ID para2 dec_type? ignore;

inter_para: list_id dec_type COMMA inter_para | list_id dec_type;
list_id: ID COMMA list_id | ID;

// for both function and method//
para: LRB inter_para? RRB ;

inter_para2: list_id dec_type COMMA inter_para2 | list_id dec_type;
para2: LRB inter_para2? RRB ;
//STATEMENT
list_statement: statement list_statement | statement;
statement:
    (
        declared_statement
        | assign_statement
        | if_statement
        | for_statement
        | break_statement
        | continue_statement
        | call_statement
        | return_statement
    );

// declared statement //
declared_statement: var_declared | const_declared ;


// assign statement //
assign_operator: ASSIGN_ADD | ASSIGN_DIV | ASSIGN_MOD | ASSIGN_MUL | ASSIGN_OP | ASSIGN_SUB;
assign_statement: scalar_var_rec assign_operator expr ignore ;

scalar_var: (ID | ID array_init_sca);
scalar_var_rec: scalar_var_rec DOT scalar_var | scalar_var;     //this has other alias name is left-hand-side (lhs)
array_init_sca: array_init_sca LSB expr RSB | LSB expr RSB;
// a.b.c.d.e.df.fd, a[2].b.c[2].d.r[1][2][3]

// if statement //
if_statement: IF (LRB expr RRB) body_block else_if_statement_rec? else_statement? ignore;
else_if_statement: ELSE IF (LRB expr RRB) body_block;
else_if_statement_rec: else_if_statement else_if_statement_rec | else_if_statement;
else_statement: ELSE body_block;

// for statement //
for_statement: (for_cond | for_3var | for_range) body_block ignore;
for_3var: FOR f3v_init SEMICOLON expr SEMICOLON f3v_modi;
f3v_init: (ID assign_operator expr) | (VAR ID dec_type? ASSIGN expr);
f3v_modi: ID assign_operator expr;

for_cond: FOR expr;
for_range: FOR ID COMMA ID ASSIGN_OP RANGE expr;

// break, call, continue, return //
break_statement:  BREAK ignore;
continue_statement:  CONTINUE ignore;
call_statement:  scalar_var_rec LRB list_expr? RRB ignore ;
return_statement: RETURN expr? ignore;

// end of stmt, decl NOTE: CHECK IF NOT USE NEWLINE
ignore: SEMICOLON | NEWLINE ;

// body scope
body_block: LCB list_statement RCB;
// ignore: SEMICOLON ;

// ---------------- PASER ----------------------- //

