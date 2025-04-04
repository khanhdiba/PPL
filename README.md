<h3>This is one of the hardest courses I studied at HCMUT</h3>
<h1>Principle of Programming Language</h1>

<h3>Assignment 1</h3>
<b>Testcase Grade: Lexer(100/100), Parser(98/100)</b><br>
<b>Harmony Grade: Lexer(10.0/10.0), Parser(10.0/10.0)</b><br>
<b>Time need: a day (Reading materials) + half day (coding lexer and parser) + ~half day (fixing bug)</b><br>
<b>Cover Topics: Lexical Analysis and Syntax Analysis</b><br>
Well, this is not a hard assignment, study this makes me feel of becoming a Linguistics student, not Computer Science :D
There are 2 parts in this assignment.

<b>Lexer</b>: Well, to be honest, this is just like a list of initializations, we have to define keywords, separators, literals, ... Not hard, however, there are some trickies:
<ul>
    <li>Int Literals: well, there are 4 types of IntLit in this assignment, so be careful.</li>
    <li>String Literals: Unlike Mr Duy, String of Dr Phung include 2 quotes so this is a legal string lit: "Hello" not Hello.</li>
    <li>Automated Semicolon: well, this is trickiest part of Lexer, we have to program in the Lexer class to define it, however, you can do it yourself, be confident.</li>
</ul>
<b>Parser</b>: Well, after a list of initialization, we have to do the grammar, this part is not hard, however, this was a war of 2 teams: "Nullable Block" and "At least a statement Block".<br>
<p align="center"><img src="meme1.png" style="display: block; margin: auto;"></p>
<ul>
    <li>Literals and Expressions: this part not hard, however you have to becareful in array literals, you can split it into many parsers, it can help you to easily handle the problem</li>
    <li>Declarations: This part is very easy, but try to split into many parsers, do not do in one line. It makes your code clean and easier to debug</li>
    <li>Statements: Well, nothing to say, it likes Declarations, but remember that, the program is list of declarations, <b>NOT</b> list of statement</li>
</ul>
Well, I will write sample of parser here for you easily imagine. Assumes that, all uppercases are Lexer and lowercases are parsers. this is just sample, not relevant to this assignment, maybe this is Python:<br>
<p margin-left="50%">
<code>
    if_full_stmt: if_stmt elif_stmt? else_stmt? ;
    if_stmt: IF expression COLON list_stmt ;
    elif_stmt: ELIF expression COLON list_stmt ;
    else_stmt: ELSE list_stmt ;
</code>
</p>

<h3>Assignment 2</h3>
<b>Testcase Grade: 94/100</b><br>
<b>Harmony Grade: 7.5/10.0</b><br>
<b>Time need: a week (Reading materials) + ~half day (coding and fixing bug)</b><br>
<b>Cover Topics: OOP, FP (for your coding skills) and AST (learning how to build AST)</b><br>

Unlike the first Assignment, this assignment is just to build the <b>Abstract Syntax Tree</b>, this is the <b>EASIEST ASSIGNMENT</b> in this course, so try to get the highest as you can.<br>
But there are some issues while doing this assignment:
<ul>
    <li>Try to use Recursion lieu of using Loop, it makes your code looks professionally</li>
    <li>If you use <b>EBNF</b> in your ANTLR code, try to make them to <b>BNF</b>, it would be easier to do.</li>
    <li>Using <code>self.visit(ctx.A())</code>, don't call <code>self.visitA(...)</code></li>
</ul>
So this is the easiest assignment, so try all that you can.
<h3>Midterm</h3>

<h3>Assignment 3</h3>
<b>Testcase Grade: /100</b><br>
<b>Harmony Grade: /10.0</b><br>
<b>Time need: a week (Reading materials) + ~1.5 week (coding and fixing bug)</b><br>
<b>Cover Topics: Name and Type</b><br>
This is the <b>HARDEST ASSIGNMENT</b>, nothing to say, in this assignment will have 3 parts:
<ul>
    <li>Redeclared Error</li>
    <li>Undeclared Error</li>
    <li>Type Mismatch</li>
</ul>
There are some tricks to do this assignment easier:
<ul>
    <li>Try to use FP, it will make your code shorter.</li>
    <li>With Declaration, you should return Symbol object or List (Based on your style).</li>
    <li>With Expression, you should return object type, it can help you to easier handle.</li>
    <li>with your environment object, it's freestyle, my recommendation is to use 2d List, the leftmost will be localmost and rightmost will be the globalmost, but you can swap the sides (Python support access the last value of list using list[-1]).</li>
    <li>If your assignment have some type of declarations that have lifetime from the beginning to the ending of program (do not care where is your declaration) --> visit more than one time in your program --> make your assignment shorter.</li>

</ul>
<a href="https://imgflip.com/i/9pp3vf"><img src="https://i.imgflip.com/9pp3vf.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>
<a href="https://imgflip.com/i/9pp463"><img src="https://i.imgflip.com/9pp463.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>
<a href="https://imgflip.com/i/9pp474"><img src="https://i.imgflip.com/9pp474.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator">from Imgflip Meme Generator</a></div>
<h3>Assignment 4</h3>
