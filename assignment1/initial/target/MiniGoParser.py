# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u02a9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u009c\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u00a8\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\b\u00b6\n\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u00be\n\b\3\b\7\b\u00c1\n\b\f\b\16\b\u00c4\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00d2\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00d9\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00ea\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00f1\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\7\16\u00f9\n\16\f\16\16\16\u00fc")
        buf.write("\13\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u0104\n\17\f")
        buf.write("\17\16\17\u0107\13\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\7\20\u0110\n\20\f\20\16\20\u0113\13\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\7\21\u011c\n\21\f\21\16\21\u011f")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u0128\n")
        buf.write("\22\f\22\16\22\u012b\13\22\3\23\3\23\3\23\3\23\5\23\u0131")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u013f\n\24\7\24\u0141\n\24\f\24\16\24")
        buf.write("\u0144\13\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u014d")
        buf.write("\n\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u015c\n\32\3\33\3\33\3\33\5\33\u0161")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u016b")
        buf.write("\n\34\3\35\5\35\u016e\n\35\3\35\3\35\5\35\u0172\n\35\3")
        buf.write("\35\3\35\5\35\u0176\n\35\3\35\3\35\5\35\u017a\n\35\3\35")
        buf.write("\3\35\5\35\u017e\n\35\3\35\5\35\u0181\n\35\3\36\3\36\3")
        buf.write("\36\5\36\u0186\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\5#\u01a6\n#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\5$\u01b0\n$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u01c8\n(\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\5,\u01dc")
        buf.write("\n,\3-\3-\3-\5-\u01e1\n-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\5.\u01ed\n.\3/\3/\3/\3/\5/\u01f3\n/\3\60\3\60\5\60\u01f7")
        buf.write("\n\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0203\n\61\3\62\3\62\5\62\u0207\n\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\63\5\63\u020f\n\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\5\64\u0219\n\64\3\65\3\65\5\65\u021d")
        buf.write("\n\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\58\u0229")
        buf.write("\n8\39\39\39\39\39\39\79\u0231\n9\f9\169\u0234\139\3:")
        buf.write("\3:\3:\3:\3:\3:\3:\3:\3:\3:\7:\u0240\n:\f:\16:\u0243\13")
        buf.write(":\3;\3;\3;\3;\3;\3;\3;\5;\u024c\n;\3;\5;\u024f\n;\3;\3")
        buf.write(";\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\5=\u025f\n=\3>\3")
        buf.write(">\3>\3?\3?\3?\5?\u0267\n?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("@\3A\3A\3A\3A\3A\3A\3A\5A\u027a\nA\3A\3A\5A\u027e\nA\3")
        buf.write("B\3B\3B\3B\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\5G\u0298\nG\3G\3G\3G\3H\3H\5H\u029f\n")
        buf.write("H\3H\3H\3I\3I\3J\3J\3J\3J\3J\2\13\16\32\34\36 \"&prK\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\n\3\2\67")
        buf.write(":\4\2\13\16\66\66\3\2\34!\3\2\27\30\3\2\31\33\4\2\27\30")
        buf.write("$$\3\2&+\4\2\64\64??\2\u02b3\2\u0094\3\2\2\2\4\u009b\3")
        buf.write("\2\2\2\6\u009d\3\2\2\2\b\u00a7\3\2\2\2\n\u00a9\3\2\2\2")
        buf.write("\f\u00af\3\2\2\2\16\u00b1\3\2\2\2\20\u00d1\3\2\2\2\22")
        buf.write("\u00d8\3\2\2\2\24\u00da\3\2\2\2\26\u00e9\3\2\2\2\30\u00f0")
        buf.write("\3\2\2\2\32\u00f2\3\2\2\2\34\u00fd\3\2\2\2\36\u0108\3")
        buf.write("\2\2\2 \u0114\3\2\2\2\"\u0120\3\2\2\2$\u0130\3\2\2\2&")
        buf.write("\u0132\3\2\2\2(\u014c\3\2\2\2*\u014e\3\2\2\2,\u0150\3")
        buf.write("\2\2\2.\u0152\3\2\2\2\60\u0154\3\2\2\2\62\u015b\3\2\2")
        buf.write("\2\64\u015d\3\2\2\2\66\u016a\3\2\2\28\u0180\3\2\2\2:\u0185")
        buf.write("\3\2\2\2<\u0187\3\2\2\2>\u018f\3\2\2\2@\u0194\3\2\2\2")
        buf.write("B\u019b\3\2\2\2D\u01a1\3\2\2\2F\u01aa\3\2\2\2H\u01b4\3")
        buf.write("\2\2\2J\u01b9\3\2\2\2L\u01bf\3\2\2\2N\u01c7\3\2\2\2P\u01c9")
        buf.write("\3\2\2\2R\u01cd\3\2\2\2T\u01d3\3\2\2\2V\u01db\3\2\2\2")
        buf.write("X\u01dd\3\2\2\2Z\u01ec\3\2\2\2\\\u01f2\3\2\2\2^\u01f4")
        buf.write("\3\2\2\2`\u0202\3\2\2\2b\u0204\3\2\2\2d\u020e\3\2\2\2")
        buf.write("f\u0218\3\2\2\2h\u021c\3\2\2\2j\u021e\3\2\2\2l\u0220\3")
        buf.write("\2\2\2n\u0228\3\2\2\2p\u022a\3\2\2\2r\u0235\3\2\2\2t\u0244")
        buf.write("\3\2\2\2v\u0252\3\2\2\2x\u025e\3\2\2\2z\u0260\3\2\2\2")
        buf.write("|\u0266\3\2\2\2~\u026b\3\2\2\2\u0080\u027d\3\2\2\2\u0082")
        buf.write("\u027f\3\2\2\2\u0084\u0283\3\2\2\2\u0086\u0286\3\2\2\2")
        buf.write("\u0088\u028e\3\2\2\2\u008a\u0291\3\2\2\2\u008c\u0294\3")
        buf.write("\2\2\2\u008e\u029c\3\2\2\2\u0090\u02a2\3\2\2\2\u0092\u02a4")
        buf.write("\3\2\2\2\u0094\u0095\5\4\3\2\u0095\u0096\7\2\2\3\u0096")
        buf.write("\3\3\2\2\2\u0097\u0098\5\66\34\2\u0098\u0099\5\4\3\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u009c\5\66\34\2\u009b\u0097\3\2\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009c\5\3\2\2\2\u009d\u009e\t\2")
        buf.write("\2\2\u009e\7\3\2\2\2\u009f\u00a8\5\6\4\2\u00a0\u00a8\7")
        buf.write(";\2\2\u00a1\u00a8\7<\2\2\u00a2\u00a8\7\25\2\2\u00a3\u00a8")
        buf.write("\7\26\2\2\u00a4\u00a8\7\24\2\2\u00a5\u00a8\5\n\6\2\u00a6")
        buf.write("\u00a8\5\24\13\2\u00a7\u009f\3\2\2\2\u00a7\u00a0\3\2\2")
        buf.write("\2\u00a7\u00a1\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7\u00a3")
        buf.write("\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\t\3\2\2\2\u00a9\u00aa\5\16\b\2\u00aa")
        buf.write("\u00ab\5\f\7\2\u00ab\u00ac\7/\2\2\u00ac\u00ad\5\22\n\2")
        buf.write("\u00ad\u00ae\7\60\2\2\u00ae\13\3\2\2\2\u00af\u00b0\t\3")
        buf.write("\2\2\u00b0\r\3\2\2\2\u00b1\u00b2\b\b\1\2\u00b2\u00b5\7")
        buf.write("\61\2\2\u00b3\u00b6\5\6\4\2\u00b4\u00b6\7\66\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b8\7\62\2\2\u00b8\u00c2\3\2\2\2\u00b9\u00ba")
        buf.write("\f\4\2\2\u00ba\u00bd\7\61\2\2\u00bb\u00be\5\6\4\2\u00bc")
        buf.write("\u00be\7\66\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\7\62\2\2\u00c0\u00b9")
        buf.write("\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\17\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5")
        buf.write("\u00d2\5\6\4\2\u00c6\u00d2\7;\2\2\u00c7\u00d2\7<\2\2\u00c8")
        buf.write("\u00d2\7\25\2\2\u00c9\u00d2\7\26\2\2\u00ca\u00d2\7\24")
        buf.write("\2\2\u00cb\u00d2\7\66\2\2\u00cc\u00d2\5\24\13\2\u00cd")
        buf.write("\u00ce\7/\2\2\u00ce\u00cf\5\22\n\2\u00cf\u00d0\7\60\2")
        buf.write("\2\u00d0\u00d2\3\2\2\2\u00d1\u00c5\3\2\2\2\u00d1\u00c6")
        buf.write("\3\2\2\2\u00d1\u00c7\3\2\2\2\u00d1\u00c8\3\2\2\2\u00d1")
        buf.write("\u00c9\3\2\2\2\u00d1\u00ca\3\2\2\2\u00d1\u00cb\3\2\2\2")
        buf.write("\u00d1\u00cc\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d2\21\3\2")
        buf.write("\2\2\u00d3\u00d4\5\20\t\2\u00d4\u00d5\7\63\2\2\u00d5\u00d6")
        buf.write("\5\22\n\2\u00d6\u00d9\3\2\2\2\u00d7\u00d9\5\20\t\2\u00d8")
        buf.write("\u00d3\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\23\3\2\2\2\u00da")
        buf.write("\u00db\7\66\2\2\u00db\u00dc\7/\2\2\u00dc\u00dd\5\26\f")
        buf.write("\2\u00dd\u00de\7\60\2\2\u00de\25\3\2\2\2\u00df\u00e0\7")
        buf.write("\66\2\2\u00e0\u00e1\7\65\2\2\u00e1\u00e2\5\32\16\2\u00e2")
        buf.write("\u00e3\7\63\2\2\u00e3\u00e4\5\26\f\2\u00e4\u00ea\3\2\2")
        buf.write("\2\u00e5\u00e6\7\66\2\2\u00e6\u00e7\7\65\2\2\u00e7\u00ea")
        buf.write("\5\32\16\2\u00e8\u00ea\3\2\2\2\u00e9\u00df\3\2\2\2\u00e9")
        buf.write("\u00e5\3\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\27\3\2\2\2\u00eb")
        buf.write("\u00ec\5\32\16\2\u00ec\u00ed\7\63\2\2\u00ed\u00ee\5\30")
        buf.write("\r\2\u00ee\u00f1\3\2\2\2\u00ef\u00f1\5\32\16\2\u00f0\u00eb")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\31\3\2\2\2\u00f2\u00f3")
        buf.write("\b\16\1\2\u00f3\u00f4\5\34\17\2\u00f4\u00fa\3\2\2\2\u00f5")
        buf.write("\u00f6\f\4\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f9\5\34\17")
        buf.write("\2\u00f8\u00f5\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\33\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\b\17\1\2\u00fe\u00ff\5\36\20\2\u00ff")
        buf.write("\u0105\3\2\2\2\u0100\u0101\f\4\2\2\u0101\u0102\7\"\2\2")
        buf.write("\u0102\u0104\5\36\20\2\u0103\u0100\3\2\2\2\u0104\u0107")
        buf.write("\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\35\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\b\20\1\2\u0109")
        buf.write("\u010a\5 \21\2\u010a\u0111\3\2\2\2\u010b\u010c\f\4\2\2")
        buf.write("\u010c\u010d\5*\26\2\u010d\u010e\5 \21\2\u010e\u0110\3")
        buf.write("\2\2\2\u010f\u010b\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\37\3\2\2\2\u0113\u0111")
        buf.write("\3\2\2\2\u0114\u0115\b\21\1\2\u0115\u0116\5\"\22\2\u0116")
        buf.write("\u011d\3\2\2\2\u0117\u0118\f\4\2\2\u0118\u0119\5,\27\2")
        buf.write("\u0119\u011a\5\"\22\2\u011a\u011c\3\2\2\2\u011b\u0117")
        buf.write("\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e!\3\2\2\2\u011f\u011d\3\2\2\2\u0120")
        buf.write("\u0121\b\22\1\2\u0121\u0122\5$\23\2\u0122\u0129\3\2\2")
        buf.write("\2\u0123\u0124\f\4\2\2\u0124\u0125\5.\30\2\u0125\u0126")
        buf.write("\5$\23\2\u0126\u0128\3\2\2\2\u0127\u0123\3\2\2\2\u0128")
        buf.write("\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a#\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\5\60\31")
        buf.write("\2\u012d\u012e\5$\23\2\u012e\u0131\3\2\2\2\u012f\u0131")
        buf.write("\5&\24\2\u0130\u012c\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("%\3\2\2\2\u0132\u0133\b\24\1\2\u0133\u0134\5(\25\2\u0134")
        buf.write("\u0142\3\2\2\2\u0135\u0136\f\5\2\2\u0136\u0137\7\61\2")
        buf.write("\2\u0137\u0138\5\32\16\2\u0138\u0139\7\62\2\2\u0139\u0141")
        buf.write("\3\2\2\2\u013a\u013b\f\4\2\2\u013b\u013e\7,\2\2\u013c")
        buf.write("\u013f\7\66\2\2\u013d\u013f\5\64\33\2\u013e\u013c\3\2")
        buf.write("\2\2\u013e\u013d\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u0135")
        buf.write("\3\2\2\2\u0140\u013a\3\2\2\2\u0141\u0144\3\2\2\2\u0142")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\'\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u014d\5\b\5\2\u0146\u014d\7\66\2")
        buf.write("\2\u0147\u0148\7-\2\2\u0148\u0149\5\32\16\2\u0149\u014a")
        buf.write("\7.\2\2\u014a\u014d\3\2\2\2\u014b\u014d\5\64\33\2\u014c")
        buf.write("\u0145\3\2\2\2\u014c\u0146\3\2\2\2\u014c\u0147\3\2\2\2")
        buf.write("\u014c\u014b\3\2\2\2\u014d)\3\2\2\2\u014e\u014f\t\4\2")
        buf.write("\2\u014f+\3\2\2\2\u0150\u0151\t\5\2\2\u0151-\3\2\2\2\u0152")
        buf.write("\u0153\t\6\2\2\u0153/\3\2\2\2\u0154\u0155\t\7\2\2\u0155")
        buf.write("\61\3\2\2\2\u0156\u0157\5\32\16\2\u0157\u0158\7\63\2\2")
        buf.write("\u0158\u0159\5\62\32\2\u0159\u015c\3\2\2\2\u015a\u015c")
        buf.write("\5\32\16\2\u015b\u0156\3\2\2\2\u015b\u015a\3\2\2\2\u015c")
        buf.write("\63\3\2\2\2\u015d\u015e\7\66\2\2\u015e\u0160\7-\2\2\u015f")
        buf.write("\u0161\5\62\32\2\u0160\u015f\3\2\2\2\u0160\u0161\3\2\2")
        buf.write("\2\u0161\u0162\3\2\2\2\u0162\u0163\7.\2\2\u0163\65\3\2")
        buf.write("\2\2\u0164\u016b\5:\36\2\u0165\u016b\5B\"\2\u0166\u016b")
        buf.write("\5D#\2\u0167\u016b\5F$\2\u0168\u016b\5J&\2\u0169\u016b")
        buf.write("\5R*\2\u016a\u0164\3\2\2\2\u016a\u0165\3\2\2\2\u016a\u0166")
        buf.write("\3\2\2\2\u016a\u0167\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u0169\3\2\2\2\u016b\67\3\2\2\2\u016c\u016e\5\16\b\2\u016d")
        buf.write("\u016c\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0181\7\f\2\2\u0170\u0172\5\16\b\2\u0171\u0170")
        buf.write("\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0181\7\r\2\2\u0174\u0176\5\16\b\2\u0175\u0174\3\2\2")
        buf.write("\2\u0175\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0181")
        buf.write("\7\16\2\2\u0178\u017a\5\16\b\2\u0179\u0178\3\2\2\2\u0179")
        buf.write("\u017a\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0181\7\13\2")
        buf.write("\2\u017c\u017e\5\16\b\2\u017d\u017c\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\7\66\2\2\u0180")
        buf.write("\u016d\3\2\2\2\u0180\u0171\3\2\2\2\u0180\u0175\3\2\2\2")
        buf.write("\u0180\u0179\3\2\2\2\u0180\u017d\3\2\2\2\u01819\3\2\2")
        buf.write("\2\u0182\u0186\5<\37\2\u0183\u0186\5> \2\u0184\u0186\5")
        buf.write("@!\2\u0185\u0182\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0184")
        buf.write("\3\2\2\2\u0186;\3\2\2\2\u0187\u0188\7\20\2\2\u0188\u0189")
        buf.write("\7\66\2\2\u0189\u018a\58\35\2\u018a\u018b\7%\2\2\u018b")
        buf.write("\u018c\5\32\16\2\u018c\u018d\3\2\2\2\u018d\u018e\5\u0090")
        buf.write("I\2\u018e=\3\2\2\2\u018f\u0190\7\20\2\2\u0190\u0191\7")
        buf.write("\66\2\2\u0191\u0192\58\35\2\u0192\u0193\5\u0090I\2\u0193")
        buf.write("?\3\2\2\2\u0194\u0195\7\20\2\2\u0195\u0196\7\66\2\2\u0196")
        buf.write("\u0197\7%\2\2\u0197\u0198\5\32\16\2\u0198\u0199\3\2\2")
        buf.write("\2\u0199\u019a\5\u0090I\2\u019aA\3\2\2\2\u019b\u019c\7")
        buf.write("\17\2\2\u019c\u019d\7\66\2\2\u019d\u019e\7%\2\2\u019e")
        buf.write("\u019f\5\32\16\2\u019f\u01a0\5\u0090I\2\u01a0C\3\2\2\2")
        buf.write("\u01a1\u01a2\7\7\2\2\u01a2\u01a3\7\66\2\2\u01a3\u01a5")
        buf.write("\5^\60\2\u01a4\u01a6\58\35\2\u01a5\u01a4\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\5\u0092")
        buf.write("J\2\u01a8\u01a9\5\u0090I\2\u01a9E\3\2\2\2\u01aa\u01ab")
        buf.write("\7\7\2\2\u01ab\u01ac\5H%\2\u01ac\u01ad\7\66\2\2\u01ad")
        buf.write("\u01af\5^\60\2\u01ae\u01b0\58\35\2\u01af\u01ae\3\2\2\2")
        buf.write("\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\5")
        buf.write("\u0092J\2\u01b2\u01b3\5\u0090I\2\u01b3G\3\2\2\2\u01b4")
        buf.write("\u01b5\7-\2\2\u01b5\u01b6\7\66\2\2\u01b6\u01b7\7\66\2")
        buf.write("\2\u01b7\u01b8\7.\2\2\u01b8I\3\2\2\2\u01b9\u01ba\7\b\2")
        buf.write("\2\u01ba\u01bb\7\66\2\2\u01bb\u01bc\7\t\2\2\u01bc\u01bd")
        buf.write("\5L\'\2\u01bd\u01be\5\u0090I\2\u01beK\3\2\2\2\u01bf\u01c0")
        buf.write("\7/\2\2\u01c0\u01c1\5N(\2\u01c1\u01c2\7\60\2\2\u01c2M")
        buf.write("\3\2\2\2\u01c3\u01c4\5P)\2\u01c4\u01c5\5N(\2\u01c5\u01c8")
        buf.write("\3\2\2\2\u01c6\u01c8\5P)\2\u01c7\u01c3\3\2\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8O\3\2\2\2\u01c9\u01ca\7\66\2\2\u01ca\u01cb")
        buf.write("\58\35\2\u01cb\u01cc\5\u0090I\2\u01ccQ\3\2\2\2\u01cd\u01ce")
        buf.write("\7\b\2\2\u01ce\u01cf\7\66\2\2\u01cf\u01d0\7\n\2\2\u01d0")
        buf.write("\u01d1\5T+\2\u01d1\u01d2\5\u0090I\2\u01d2S\3\2\2\2\u01d3")
        buf.write("\u01d4\7/\2\2\u01d4\u01d5\5V,\2\u01d5\u01d6\7\60\2\2\u01d6")
        buf.write("U\3\2\2\2\u01d7\u01d8\5X-\2\u01d8\u01d9\5V,\2\u01d9\u01dc")
        buf.write("\3\2\2\2\u01da\u01dc\5X-\2\u01db\u01d7\3\2\2\2\u01db\u01da")
        buf.write("\3\2\2\2\u01dcW\3\2\2\2\u01dd\u01de\7\66\2\2\u01de\u01e0")
        buf.write("\5b\62\2\u01df\u01e1\58\35\2\u01e0\u01df\3\2\2\2\u01e0")
        buf.write("\u01e1\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\5\u0090")
        buf.write("I\2\u01e3Y\3\2\2\2\u01e4\u01e5\5\\/\2\u01e5\u01e6\58\35")
        buf.write("\2\u01e6\u01e7\7\63\2\2\u01e7\u01e8\5Z.\2\u01e8\u01ed")
        buf.write("\3\2\2\2\u01e9\u01ea\5\\/\2\u01ea\u01eb\58\35\2\u01eb")
        buf.write("\u01ed\3\2\2\2\u01ec\u01e4\3\2\2\2\u01ec\u01e9\3\2\2\2")
        buf.write("\u01ed[\3\2\2\2\u01ee\u01ef\7\66\2\2\u01ef\u01f0\7\63")
        buf.write("\2\2\u01f0\u01f3\5\\/\2\u01f1\u01f3\7\66\2\2\u01f2\u01ee")
        buf.write("\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3]\3\2\2\2\u01f4\u01f6")
        buf.write("\7-\2\2\u01f5\u01f7\5Z.\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\7.\2\2\u01f9")
        buf.write("_\3\2\2\2\u01fa\u01fb\5\\/\2\u01fb\u01fc\58\35\2\u01fc")
        buf.write("\u01fd\7\63\2\2\u01fd\u01fe\5`\61\2\u01fe\u0203\3\2\2")
        buf.write("\2\u01ff\u0200\5\\/\2\u0200\u0201\58\35\2\u0201\u0203")
        buf.write("\3\2\2\2\u0202\u01fa\3\2\2\2\u0202\u01ff\3\2\2\2\u0203")
        buf.write("a\3\2\2\2\u0204\u0206\7-\2\2\u0205\u0207\5`\61\2\u0206")
        buf.write("\u0205\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u0209\7.\2\2\u0209c\3\2\2\2\u020a\u020b\5f\64\2")
        buf.write("\u020b\u020c\5d\63\2\u020c\u020f\3\2\2\2\u020d\u020f\5")
        buf.write("f\64\2\u020e\u020a\3\2\2\2\u020e\u020d\3\2\2\2\u020fe")
        buf.write("\3\2\2\2\u0210\u0219\5h\65\2\u0211\u0219\5l\67\2\u0212")
        buf.write("\u0219\5t;\2\u0213\u0219\5|?\2\u0214\u0219\5\u0088E\2")
        buf.write("\u0215\u0219\5\u008aF\2\u0216\u0219\5\u008cG\2\u0217\u0219")
        buf.write("\5\u008eH\2\u0218\u0210\3\2\2\2\u0218\u0211\3\2\2\2\u0218")
        buf.write("\u0212\3\2\2\2\u0218\u0213\3\2\2\2\u0218\u0214\3\2\2\2")
        buf.write("\u0218\u0215\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0217\3")
        buf.write("\2\2\2\u0219g\3\2\2\2\u021a\u021d\5:\36\2\u021b\u021d")
        buf.write("\5B\"\2\u021c\u021a\3\2\2\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("i\3\2\2\2\u021e\u021f\t\b\2\2\u021fk\3\2\2\2\u0220\u0221")
        buf.write("\5p9\2\u0221\u0222\5j\66\2\u0222\u0223\5\32\16\2\u0223")
        buf.write("\u0224\5\u0090I\2\u0224m\3\2\2\2\u0225\u0229\7\66\2\2")
        buf.write("\u0226\u0227\7\66\2\2\u0227\u0229\5r:\2\u0228\u0225\3")
        buf.write("\2\2\2\u0228\u0226\3\2\2\2\u0229o\3\2\2\2\u022a\u022b")
        buf.write("\b9\1\2\u022b\u022c\5n8\2\u022c\u0232\3\2\2\2\u022d\u022e")
        buf.write("\f\4\2\2\u022e\u022f\7,\2\2\u022f\u0231\5n8\2\u0230\u022d")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233q\3\2\2\2\u0234\u0232\3\2\2\2\u0235")
        buf.write("\u0236\b:\1\2\u0236\u0237\7\61\2\2\u0237\u0238\5\32\16")
        buf.write("\2\u0238\u0239\7\62\2\2\u0239\u0241\3\2\2\2\u023a\u023b")
        buf.write("\f\4\2\2\u023b\u023c\7\61\2\2\u023c\u023d\5\32\16\2\u023d")
        buf.write("\u023e\7\62\2\2\u023e\u0240\3\2\2\2\u023f\u023a\3\2\2")
        buf.write("\2\u0240\u0243\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242s\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245")
        buf.write("\7\3\2\2\u0245\u0246\7-\2\2\u0246\u0247\5\32\16\2\u0247")
        buf.write("\u0248\7.\2\2\u0248\u0249\3\2\2\2\u0249\u024b\5\u0092")
        buf.write("J\2\u024a\u024c\5x=\2\u024b\u024a\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024f\5z>\2\u024e\u024d")
        buf.write("\3\2\2\2\u024e\u024f\3\2\2\2\u024f\u0250\3\2\2\2\u0250")
        buf.write("\u0251\5\u0090I\2\u0251u\3\2\2\2\u0252\u0253\7\4\2\2\u0253")
        buf.write("\u0254\7\3\2\2\u0254\u0255\7-\2\2\u0255\u0256\5\32\16")
        buf.write("\2\u0256\u0257\7.\2\2\u0257\u0258\3\2\2\2\u0258\u0259")
        buf.write("\5\u0092J\2\u0259w\3\2\2\2\u025a\u025b\5v<\2\u025b\u025c")
        buf.write("\5x=\2\u025c\u025f\3\2\2\2\u025d\u025f\5v<\2\u025e\u025a")
        buf.write("\3\2\2\2\u025e\u025d\3\2\2\2\u025fy\3\2\2\2\u0260\u0261")
        buf.write("\7\4\2\2\u0261\u0262\5\u0092J\2\u0262{\3\2\2\2\u0263\u0267")
        buf.write("\5\u0084C\2\u0264\u0267\5~@\2\u0265\u0267\5\u0086D\2\u0266")
        buf.write("\u0263\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0265\3\2\2\2")
        buf.write("\u0267\u0268\3\2\2\2\u0268\u0269\5\u0092J\2\u0269\u026a")
        buf.write("\5\u0090I\2\u026a}\3\2\2\2\u026b\u026c\7\5\2\2\u026c\u026d")
        buf.write("\5\u0080A\2\u026d\u026e\7\64\2\2\u026e\u026f\5\32\16\2")
        buf.write("\u026f\u0270\7\64\2\2\u0270\u0271\5\u0082B\2\u0271\177")
        buf.write("\3\2\2\2\u0272\u0273\7\66\2\2\u0273\u0274\5j\66\2\u0274")
        buf.write("\u0275\5\32\16\2\u0275\u027e\3\2\2\2\u0276\u0277\7\20")
        buf.write("\2\2\u0277\u0279\7\66\2\2\u0278\u027a\58\35\2\u0279\u0278")
        buf.write("\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u027b\3\2\2\2\u027b")
        buf.write("\u027c\7%\2\2\u027c\u027e\5\32\16\2\u027d\u0272\3\2\2")
        buf.write("\2\u027d\u0276\3\2\2\2\u027e\u0081\3\2\2\2\u027f\u0280")
        buf.write("\7\66\2\2\u0280\u0281\5j\66\2\u0281\u0282\5\32\16\2\u0282")
        buf.write("\u0083\3\2\2\2\u0283\u0284\7\5\2\2\u0284\u0285\5\32\16")
        buf.write("\2\u0285\u0085\3\2\2\2\u0286\u0287\7\5\2\2\u0287\u0288")
        buf.write("\7\66\2\2\u0288\u0289\7\63\2\2\u0289\u028a\7\66\2\2\u028a")
        buf.write("\u028b\7&\2\2\u028b\u028c\7\23\2\2\u028c\u028d\5\32\16")
        buf.write("\2\u028d\u0087\3\2\2\2\u028e\u028f\7\22\2\2\u028f\u0290")
        buf.write("\5\u0090I\2\u0290\u0089\3\2\2\2\u0291\u0292\7\21\2\2\u0292")
        buf.write("\u0293\5\u0090I\2\u0293\u008b\3\2\2\2\u0294\u0295\5p9")
        buf.write("\2\u0295\u0297\7-\2\2\u0296\u0298\5\30\r\2\u0297\u0296")
        buf.write("\3\2\2\2\u0297\u0298\3\2\2\2\u0298\u0299\3\2\2\2\u0299")
        buf.write("\u029a\7.\2\2\u029a\u029b\5\u0090I\2\u029b\u008d\3\2\2")
        buf.write("\2\u029c\u029e\7\6\2\2\u029d\u029f\5\32\16\2\u029e\u029d")
        buf.write("\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u02a0\3\2\2\2\u02a0")
        buf.write("\u02a1\5\u0090I\2\u02a1\u008f\3\2\2\2\u02a2\u02a3\t\t")
        buf.write("\2\2\u02a3\u0091\3\2\2\2\u02a4\u02a5\7/\2\2\u02a5\u02a6")
        buf.write("\5d\63\2\u02a6\u02a7\7\60\2\2\u02a7\u0093\3\2\2\2\67\u009b")
        buf.write("\u00a7\u00b5\u00bd\u00c2\u00d1\u00d8\u00e9\u00f0\u00fa")
        buf.write("\u0105\u0111\u011d\u0129\u0130\u013e\u0140\u0142\u014c")
        buf.write("\u015b\u0160\u016a\u016d\u0171\u0175\u0179\u017d\u0180")
        buf.write("\u0185\u01a5\u01af\u01c7\u01db\u01e0\u01ec\u01f2\u01f6")
        buf.write("\u0202\u0206\u020e\u0218\u021c\u0228\u0232\u0241\u024b")
        buf.write("\u024e\u025e\u0266\u0279\u027d\u0297\u029e")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQUAL", "NOT_EQUAL", "LT", "GT", "LTE", "GTE", 
                      "AND", "OR", "NOT", "ASSIGN", "ASSIGN_OP", "ASSIGN_ADD", 
                      "ASSIGN_SUB", "ASSIGN_MUL", "ASSIGN_DIV", "ASSIGN_MOD", 
                      "DOT", "LRB", "RRB", "LCB", "RCB", "LSB", "RSB", "COMMA", 
                      "SEMICOLON", "COLON", "ID", "DEC", "BIN", "OCT", "HEX", 
                      "FLOAT_LIT", "STR_LIT", "SINGLE_COMMENT", "MULTI_COMMENT", 
                      "NEWLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_declare = 1
    RULE_int_lit = 2
    RULE_literal = 3
    RULE_array_literal = 4
    RULE_array_type = 5
    RULE_array_init = 6
    RULE_array_index = 7
    RULE_list_array_index = 8
    RULE_struct_literal = 9
    RULE_list_element = 10
    RULE_list_expr = 11
    RULE_expr = 12
    RULE_expr1 = 13
    RULE_expr2 = 14
    RULE_expr3 = 15
    RULE_expr4 = 16
    RULE_expr5 = 17
    RULE_expr6 = 18
    RULE_expr7 = 19
    RULE_log_op = 20
    RULE_add_op = 21
    RULE_mul_op = 22
    RULE_una_op = 23
    RULE_parameter = 24
    RULE_func_call = 25
    RULE_declared = 26
    RULE_dec_type = 27
    RULE_var_declared = 28
    RULE_var_full = 29
    RULE_var_type = 30
    RULE_var_init = 31
    RULE_const_declared = 32
    RULE_func_declared = 33
    RULE_method_declared = 34
    RULE_method_struct_name = 35
    RULE_struct_declared = 36
    RULE_struct_body = 37
    RULE_list_struct_declared = 38
    RULE_struct_index = 39
    RULE_interface_declared = 40
    RULE_interface_body = 41
    RULE_list_interface_declared = 42
    RULE_line_inter = 43
    RULE_inter_para = 44
    RULE_list_id = 45
    RULE_para = 46
    RULE_inter_para2 = 47
    RULE_para2 = 48
    RULE_list_statement = 49
    RULE_statement = 50
    RULE_declared_statement = 51
    RULE_assign_operator = 52
    RULE_assign_statement = 53
    RULE_scalar_var = 54
    RULE_scalar_var_rec = 55
    RULE_array_init_sca = 56
    RULE_if_statement = 57
    RULE_else_if_statement = 58
    RULE_else_if_statement_rec = 59
    RULE_else_statement = 60
    RULE_for_statement = 61
    RULE_for_3var = 62
    RULE_f3v_init = 63
    RULE_f3v_modi = 64
    RULE_for_cond = 65
    RULE_for_range = 66
    RULE_break_statement = 67
    RULE_continue_statement = 68
    RULE_call_statement = 69
    RULE_return_statement = 70
    RULE_ignore = 71
    RULE_body_block = 72

    ruleNames =  [ "program", "list_declare", "int_lit", "literal", "array_literal", 
                   "array_type", "array_init", "array_index", "list_array_index", 
                   "struct_literal", "list_element", "list_expr", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "log_op", "add_op", "mul_op", "una_op", "parameter", 
                   "func_call", "declared", "dec_type", "var_declared", 
                   "var_full", "var_type", "var_init", "const_declared", 
                   "func_declared", "method_declared", "method_struct_name", 
                   "struct_declared", "struct_body", "list_struct_declared", 
                   "struct_index", "interface_declared", "interface_body", 
                   "list_interface_declared", "line_inter", "inter_para", 
                   "list_id", "para", "inter_para2", "para2", "list_statement", 
                   "statement", "declared_statement", "assign_operator", 
                   "assign_statement", "scalar_var", "scalar_var_rec", "array_init_sca", 
                   "if_statement", "else_if_statement", "else_if_statement_rec", 
                   "else_statement", "for_statement", "for_3var", "f3v_init", 
                   "f3v_modi", "for_cond", "for_range", "break_statement", 
                   "continue_statement", "call_statement", "return_statement", 
                   "ignore", "body_block" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOLEAN=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQUAL=26
    NOT_EQUAL=27
    LT=28
    GT=29
    LTE=30
    GTE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ASSIGN_OP=36
    ASSIGN_ADD=37
    ASSIGN_SUB=38
    ASSIGN_MUL=39
    ASSIGN_DIV=40
    ASSIGN_MOD=41
    DOT=42
    LRB=43
    RRB=44
    LCB=45
    RCB=46
    LSB=47
    RSB=48
    COMMA=49
    SEMICOLON=50
    COLON=51
    ID=52
    DEC=53
    BIN=54
    OCT=55
    HEX=56
    FLOAT_LIT=57
    STR_LIT=58
    SINGLE_COMMENT=59
    MULTI_COMMENT=60
    NEWLINE=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declare(self):
            return self.getTypedRuleContext(MiniGoParser.List_declareContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.list_declare()
            self.state = 147
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared(self):
            return self.getTypedRuleContext(MiniGoParser.DeclaredContext,0)


        def list_declare(self):
            return self.getTypedRuleContext(MiniGoParser.List_declareContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declare" ):
                return visitor.visitList_declare(self)
            else:
                return visitor.visitChildren(self)




    def list_declare(self):

        localctx = MiniGoParser.List_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_declare)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.declared()
                self.state = 150
                self.list_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC(self):
            return self.getToken(MiniGoParser.DEC, 0)

        def BIN(self):
            return self.getToken(MiniGoParser.BIN, 0)

        def OCT(self):
            return self.getToken(MiniGoParser.OCT, 0)

        def HEX(self):
            return self.getToken(MiniGoParser.HEX, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_int_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)




    def int_lit(self):

        localctx = MiniGoParser.Int_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_int_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.DEC) | (1 << MiniGoParser.BIN) | (1 << MiniGoParser.OCT) | (1 << MiniGoParser.HEX))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.int_lit()
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(MiniGoParser.STR_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.match(MiniGoParser.NIL)
                pass
            elif token in [MiniGoParser.LSB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.struct_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.array_init(0)
            self.state = 168
            self.array_type()
            self.state = 169
            self.match(MiniGoParser.LCB)
            self.state = 170
            self.list_array_index()
            self.state = 171
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)



    def array_init(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Array_initContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_array_init, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MiniGoParser.LSB)
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                self.state = 177
                self.int_lit()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 178
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self.match(MiniGoParser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Array_initContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_init)
                    self.state = 183
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 184
                    self.match(MiniGoParser.LSB)
                    self.state = 187
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX]:
                        self.state = 185
                        self.int_lit()
                        pass
                    elif token in [MiniGoParser.ID]:
                        self.state = 186
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 189
                    self.match(MiniGoParser.RSB) 
                self.state = 194
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Int_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STR_LIT(self):
            return self.getToken(MiniGoParser.STR_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_index)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.int_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.match(MiniGoParser.STR_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 198
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 199
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 200
                self.match(MiniGoParser.NIL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 201
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 202
                self.struct_literal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 203
                self.match(MiniGoParser.LCB)
                self.state = 204
                self.list_array_index()
                self.state = 205
                self.match(MiniGoParser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_index(self):
            return self.getTypedRuleContext(MiniGoParser.Array_indexContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_array_index(self):
            return self.getTypedRuleContext(MiniGoParser.List_array_indexContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_array_index" ):
                return visitor.visitList_array_index(self)
            else:
                return visitor.visitChildren(self)




    def list_array_index(self):

        localctx = MiniGoParser.List_array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_list_array_index)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.array_index()
                self.state = 210
                self.match(MiniGoParser.COMMA)
                self.state = 211
                self.list_array_index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.array_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MiniGoParser.ID)
            self.state = 217
            self.match(MiniGoParser.LCB)
            self.state = 218
            self.list_element()
            self.state = 219
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_element(self):
            return self.getTypedRuleContext(MiniGoParser.List_elementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_element" ):
                return visitor.visitList_element(self)
            else:
                return visitor.visitChildren(self)




    def list_element(self):

        localctx = MiniGoParser.List_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_element)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MiniGoParser.ID)
                self.state = 222
                self.match(MiniGoParser.COLON)
                self.state = 223
                self.expr(0)
                self.state = 224
                self.match(MiniGoParser.COMMA)
                self.state = 225
                self.list_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(MiniGoParser.ID)
                self.state = 228
                self.match(MiniGoParser.COLON)
                self.state = 229
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = MiniGoParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_expr)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.expr(0)
                self.state = 234
                self.match(MiniGoParser.COMMA)
                self.state = 235
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    self.match(MiniGoParser.OR)
                    self.state = 245
                    self.expr1(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    self.match(MiniGoParser.AND)
                    self.state = 256
                    self.expr2(0) 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def log_op(self):
            return self.getTypedRuleContext(MiniGoParser.Log_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 265
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 266
                    self.log_op()
                    self.state = 267
                    self.expr3(0) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def add_op(self):
            return self.getTypedRuleContext(MiniGoParser.Add_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    self.add_op()
                    self.state = 279
                    self.expr4(0) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def mul_op(self):
            return self.getTypedRuleContext(MiniGoParser.Mul_opContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    self.mul_op()
                    self.state = 291
                    self.expr5() 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def una_op(self):
            return self.getTypedRuleContext(MiniGoParser.Una_opContext,0)


        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr5)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ADD, MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.una_op()
                self.state = 299
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LRB, MiniGoParser.LSB, MiniGoParser.ID, MiniGoParser.DEC, MiniGoParser.BIN, MiniGoParser.OCT, MiniGoParser.HEX, MiniGoParser.FLOAT_LIT, MiniGoParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 318
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 307
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 308
                        self.match(MiniGoParser.LSB)
                        self.state = 309
                        self.expr(0)
                        self.state = 310
                        self.match(MiniGoParser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 312
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 313
                        self.match(MiniGoParser.DOT)
                        self.state = 316
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                        if la_ == 1:
                            self.state = 314
                            self.match(MiniGoParser.ID)
                            pass

                        elif la_ == 2:
                            self.state = 315
                            self.func_call()
                            pass


                        pass

             
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr7)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(MiniGoParser.LRB)
                self.state = 326
                self.expr(0)
                self.state = 327
                self.match(MiniGoParser.RRB)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Log_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LTE(self):
            return self.getToken(MiniGoParser.LTE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GTE(self):
            return self.getToken(MiniGoParser.GTE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_log_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog_op" ):
                return visitor.visitLog_op(self)
            else:
                return visitor.visitChildren(self)




    def log_op(self):

        localctx = MiniGoParser.Log_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_log_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.LTE) | (1 << MiniGoParser.GTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_add_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_op" ):
                return visitor.visitAdd_op(self)
            else:
                return visitor.visitChildren(self)




    def add_op(self):

        localctx = MiniGoParser.Add_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_add_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mul_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_mul_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_op" ):
                return visitor.visitMul_op(self)
            else:
                return visitor.visitChildren(self)




    def mul_op(self):

        localctx = MiniGoParser.Mul_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mul_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Una_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_una_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUna_op" ):
                return visitor.visitUna_op(self)
            else:
                return visitor.visitChildren(self)




    def una_op(self):

        localctx = MiniGoParser.Una_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_una_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parameter)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.expr(0)
                self.state = 341
                self.match(MiniGoParser.COMMA)
                self.state = 342
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MiniGoParser.ID)
            self.state = 348
            self.match(MiniGoParser.LRB)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ADD) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LRB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC) | (1 << MiniGoParser.BIN) | (1 << MiniGoParser.OCT) | (1 << MiniGoParser.HEX) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 349
                self.parameter()


            self.state = 352
            self.match(MiniGoParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaredContext,0)


        def const_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaredContext,0)


        def func_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declaredContext,0)


        def method_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Method_declaredContext,0)


        def struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declaredContext,0)


        def interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared" ):
                return visitor.visitDeclared(self)
            else:
                return visitor.visitChildren(self)




    def declared(self):

        localctx = MiniGoParser.DeclaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_declared)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.var_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.const_declared()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.func_declared()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.method_declared()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.struct_declared()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 359
                self.interface_declared()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dec_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def array_init(self):
            return self.getTypedRuleContext(MiniGoParser.Array_initContext,0)


        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dec_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec_type" ):
                return visitor.visitDec_type(self)
            else:
                return visitor.visitChildren(self)




    def dec_type(self):

        localctx = MiniGoParser.Dec_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dec_type)
        self._la = 0 # Token type
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 362
                    self.array_init(0)


                self.state = 365
                self.match(MiniGoParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 366
                    self.array_init(0)


                self.state = 369
                self.match(MiniGoParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 370
                    self.array_init(0)


                self.state = 373
                self.match(MiniGoParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 374
                    self.array_init(0)


                self.state = 377
                self.match(MiniGoParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.LSB:
                    self.state = 378
                    self.array_init(0)


                self.state = 381
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_full(self):
            return self.getTypedRuleContext(MiniGoParser.Var_fullContext,0)


        def var_type(self):
            return self.getTypedRuleContext(MiniGoParser.Var_typeContext,0)


        def var_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declared" ):
                return visitor.visitVar_declared(self)
            else:
                return visitor.visitChildren(self)




    def var_declared(self):

        localctx = MiniGoParser.Var_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_var_declared)
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.var_full()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.var_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.var_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_fullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_full

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_full" ):
                return visitor.visitVar_full(self)
            else:
                return visitor.visitChildren(self)




    def var_full(self):

        localctx = MiniGoParser.Var_fullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_var_full)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(MiniGoParser.VAR)
            self.state = 390
            self.match(MiniGoParser.ID)
            self.state = 391
            self.dec_type()

            self.state = 392
            self.match(MiniGoParser.ASSIGN)
            self.state = 393
            self.expr(0)
            self.state = 395
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = MiniGoParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(MiniGoParser.VAR)
            self.state = 398
            self.match(MiniGoParser.ID)
            self.state = 399
            self.dec_type()
            self.state = 400
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_init" ):
                return visitor.visitVar_init(self)
            else:
                return visitor.visitChildren(self)




    def var_init(self):

        localctx = MiniGoParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(MiniGoParser.VAR)
            self.state = 403
            self.match(MiniGoParser.ID)

            self.state = 404
            self.match(MiniGoParser.ASSIGN)
            self.state = 405
            self.expr(0)
            self.state = 407
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_declared" ):
                return visitor.visitConst_declared(self)
            else:
                return visitor.visitChildren(self)




    def const_declared(self):

        localctx = MiniGoParser.Const_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_const_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MiniGoParser.CONST)
            self.state = 410
            self.match(MiniGoParser.ID)
            self.state = 411
            self.match(MiniGoParser.ASSIGN)
            self.state = 412
            self.expr(0)
            self.state = 413
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declared" ):
                return visitor.visitFunc_declared(self)
            else:
                return visitor.visitChildren(self)




    def func_declared(self):

        localctx = MiniGoParser.Func_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.FUNC)
            self.state = 416
            self.match(MiniGoParser.ID)
            self.state = 417
            self.para()
            self.state = 419
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 418
                self.dec_type()


            self.state = 421
            self.body_block()
            self.state = 422
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def method_struct_name(self):
            return self.getTypedRuleContext(MiniGoParser.Method_struct_nameContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def para(self):
            return self.getTypedRuleContext(MiniGoParser.ParaContext,0)


        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declared" ):
                return visitor.visitMethod_declared(self)
            else:
                return visitor.visitChildren(self)




    def method_declared(self):

        localctx = MiniGoParser.Method_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_method_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(MiniGoParser.FUNC)
            self.state = 425
            self.method_struct_name()
            self.state = 426
            self.match(MiniGoParser.ID)
            self.state = 427
            self.para()
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 428
                self.dec_type()


            self.state = 431
            self.body_block()
            self.state = 432
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_struct_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_struct_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_struct_name" ):
                return visitor.visitMethod_struct_name(self)
            else:
                return visitor.visitChildren(self)




    def method_struct_name(self):

        localctx = MiniGoParser.Method_struct_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_method_struct_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(MiniGoParser.LRB)
            self.state = 435
            self.match(MiniGoParser.ID)
            self.state = 436
            self.match(MiniGoParser.ID)
            self.state = 437
            self.match(MiniGoParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def struct_body(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_bodyContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declared" ):
                return visitor.visitStruct_declared(self)
            else:
                return visitor.visitChildren(self)




    def struct_declared(self):

        localctx = MiniGoParser.Struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_struct_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MiniGoParser.TYPE)
            self.state = 440
            self.match(MiniGoParser.ID)
            self.state = 441
            self.match(MiniGoParser.STRUCT)
            self.state = 442
            self.struct_body()
            self.state = 443
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_declaredContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_body" ):
                return visitor.visitStruct_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_body(self):

        localctx = MiniGoParser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_struct_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(MiniGoParser.LCB)
            self.state = 446
            self.list_struct_declared()
            self.state = 447
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_struct_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_index(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_indexContext,0)


        def list_struct_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_struct_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_struct_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_struct_declared" ):
                return visitor.visitList_struct_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_struct_declared(self):

        localctx = MiniGoParser.List_struct_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_struct_declared)
        try:
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.struct_index()
                self.state = 450
                self.list_struct_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.struct_index()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_index" ):
                return visitor.visitStruct_index(self)
            else:
                return visitor.visitChildren(self)




    def struct_index(self):

        localctx = MiniGoParser.Struct_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_struct_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(MiniGoParser.ID)
            self.state = 456
            self.dec_type()
            self.state = 457
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def interface_body(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_bodyContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declared" ):
                return visitor.visitInterface_declared(self)
            else:
                return visitor.visitChildren(self)




    def interface_declared(self):

        localctx = MiniGoParser.Interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_interface_declared)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(MiniGoParser.TYPE)
            self.state = 460
            self.match(MiniGoParser.ID)
            self.state = 461
            self.match(MiniGoParser.INTERFACE)
            self.state = 462
            self.interface_body()
            self.state = 463
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_declaredContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_body" ):
                return visitor.visitInterface_body(self)
            else:
                return visitor.visitChildren(self)




    def interface_body(self):

        localctx = MiniGoParser.Interface_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_interface_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(MiniGoParser.LCB)
            self.state = 466
            self.list_interface_declared()
            self.state = 467
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_interface_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line_inter(self):
            return self.getTypedRuleContext(MiniGoParser.Line_interContext,0)


        def list_interface_declared(self):
            return self.getTypedRuleContext(MiniGoParser.List_interface_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_interface_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_interface_declared" ):
                return visitor.visitList_interface_declared(self)
            else:
                return visitor.visitChildren(self)




    def list_interface_declared(self):

        localctx = MiniGoParser.List_interface_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_list_interface_declared)
        try:
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.line_inter()
                self.state = 470
                self.list_interface_declared()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
                self.line_inter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_interContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def para2(self):
            return self.getTypedRuleContext(MiniGoParser.Para2Context,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_line_inter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_inter" ):
                return visitor.visitLine_inter(self)
            else:
                return visitor.visitChildren(self)




    def line_inter(self):

        localctx = MiniGoParser.Line_interContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_line_inter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(MiniGoParser.ID)
            self.state = 476
            self.para2()
            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                self.state = 477
                self.dec_type()


            self.state = 480
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inter_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id(self):
            return self.getTypedRuleContext(MiniGoParser.List_idContext,0)


        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def inter_para(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inter_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInter_para" ):
                return visitor.visitInter_para(self)
            else:
                return visitor.visitChildren(self)




    def inter_para(self):

        localctx = MiniGoParser.Inter_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_inter_para)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.list_id()
                self.state = 483
                self.dec_type()
                self.state = 484
                self.match(MiniGoParser.COMMA)
                self.state = 485
                self.inter_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.list_id()
                self.state = 488
                self.dec_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_id(self):
            return self.getTypedRuleContext(MiniGoParser.List_idContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_id" ):
                return visitor.visitList_id(self)
            else:
                return visitor.visitChildren(self)




    def list_id(self):

        localctx = MiniGoParser.List_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_id)
        try:
            self.state = 496
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(MiniGoParser.ID)
                self.state = 493
                self.match(MiniGoParser.COMMA)
                self.state = 494
                self.list_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def inter_para(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_paraContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MiniGoParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(MiniGoParser.LRB)
            self.state = 500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 499
                self.inter_para()


            self.state = 502
            self.match(MiniGoParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inter_para2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_id(self):
            return self.getTypedRuleContext(MiniGoParser.List_idContext,0)


        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def inter_para2(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_para2Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_inter_para2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInter_para2" ):
                return visitor.visitInter_para2(self)
            else:
                return visitor.visitChildren(self)




    def inter_para2(self):

        localctx = MiniGoParser.Inter_para2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_inter_para2)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 504
                self.list_id()
                self.state = 505
                self.dec_type()
                self.state = 506
                self.match(MiniGoParser.COMMA)
                self.state = 507
                self.inter_para2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
                self.list_id()
                self.state = 510
                self.dec_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def inter_para2(self):
            return self.getTypedRuleContext(MiniGoParser.Inter_para2Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_para2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara2" ):
                return visitor.visitPara2(self)
            else:
                return visitor.visitChildren(self)




    def para2(self):

        localctx = MiniGoParser.Para2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_para2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(MiniGoParser.LRB)
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 515
                self.inter_para2()


            self.state = 518
            self.match(MiniGoParser.RRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_list_statement)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.statement()
                self.state = 521
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declared_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Declared_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 526
                self.declared_statement()
                pass

            elif la_ == 2:
                self.state = 527
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 528
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 529
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 530
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 531
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 532
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 533
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declared_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Var_declaredContext,0)


        def const_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Const_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declared_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclared_statement" ):
                return visitor.visitDeclared_statement(self)
            else:
                return visitor.visitChildren(self)




    def declared_statement(self):

        localctx = MiniGoParser.Declared_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_declared_statement)
        try:
            self.state = 538
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.var_declared()
                pass
            elif token in [MiniGoParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 537
                self.const_declared()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_ADD(self):
            return self.getToken(MiniGoParser.ASSIGN_ADD, 0)

        def ASSIGN_DIV(self):
            return self.getToken(MiniGoParser.ASSIGN_DIV, 0)

        def ASSIGN_MOD(self):
            return self.getToken(MiniGoParser.ASSIGN_MOD, 0)

        def ASSIGN_MUL(self):
            return self.getToken(MiniGoParser.ASSIGN_MUL, 0)

        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def ASSIGN_SUB(self):
            return self.getToken(MiniGoParser.ASSIGN_SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_operator" ):
                return visitor.visitAssign_operator(self)
            else:
                return visitor.visitChildren(self)




    def assign_operator(self):

        localctx = MiniGoParser.Assign_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_assign_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN_OP) | (1 << MiniGoParser.ASSIGN_ADD) | (1 << MiniGoParser.ASSIGN_SUB) | (1 << MiniGoParser.ASSIGN_MUL) | (1 << MiniGoParser.ASSIGN_DIV) | (1 << MiniGoParser.ASSIGN_MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var_rec(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_var_recContext,0)


        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.scalar_var_rec(0)
            self.state = 543
            self.assign_operator()
            self.state = 544
            self.expr(0)
            self.state = 545
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_init_sca(self):
            return self.getTypedRuleContext(MiniGoParser.Array_init_scaContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = MiniGoParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 547
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 548
                self.match(MiniGoParser.ID)
                self.state = 549
                self.array_init_sca(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_var_recContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_varContext,0)


        def scalar_var_rec(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_var_recContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_scalar_var_rec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var_rec" ):
                return visitor.visitScalar_var_rec(self)
            else:
                return visitor.visitChildren(self)



    def scalar_var_rec(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Scalar_var_recContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_scalar_var_rec, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.scalar_var()
            self._ctx.stop = self._input.LT(-1)
            self.state = 560
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Scalar_var_recContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_scalar_var_rec)
                    self.state = 555
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 556
                    self.match(MiniGoParser.DOT)
                    self.state = 557
                    self.scalar_var() 
                self.state = 562
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Array_init_scaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MiniGoParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MiniGoParser.RSB, 0)

        def array_init_sca(self):
            return self.getTypedRuleContext(MiniGoParser.Array_init_scaContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_init_sca

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init_sca" ):
                return visitor.visitArray_init_sca(self)
            else:
                return visitor.visitChildren(self)



    def array_init_sca(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Array_init_scaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_array_init_sca, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.match(MiniGoParser.LSB)
            self.state = 565
            self.expr(0)
            self.state = 566
            self.match(MiniGoParser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 575
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Array_init_scaContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_array_init_sca)
                    self.state = 568
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 569
                    self.match(MiniGoParser.LSB)
                    self.state = 570
                    self.expr(0)
                    self.state = 571
                    self.match(MiniGoParser.RSB) 
                self.state = 577
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def else_if_statement_rec(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statement_recContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(MiniGoParser.IF)

            self.state = 579
            self.match(MiniGoParser.LRB)
            self.state = 580
            self.expr(0)
            self.state = 581
            self.match(MiniGoParser.RRB)
            self.state = 583
            self.body_block()
            self.state = 585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 584
                self.else_if_statement_rec()


            self.state = 588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 587
                self.else_statement()


            self.state = 590
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = MiniGoParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_else_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.match(MiniGoParser.ELSE)
            self.state = 593
            self.match(MiniGoParser.IF)

            self.state = 594
            self.match(MiniGoParser.LRB)
            self.state = 595
            self.expr(0)
            self.state = 596
            self.match(MiniGoParser.RRB)
            self.state = 598
            self.body_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statement_recContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def else_if_statement_rec(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statement_recContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement_rec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement_rec" ):
                return visitor.visitElse_if_statement_rec(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement_rec(self):

        localctx = MiniGoParser.Else_if_statement_recContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_else_if_statement_rec)
        try:
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.else_if_statement()
                self.state = 601
                self.else_if_statement_rec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.else_if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(MiniGoParser.ELSE)
            self.state = 607
            self.body_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body_block(self):
            return self.getTypedRuleContext(MiniGoParser.Body_blockContext,0)


        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def for_cond(self):
            return self.getTypedRuleContext(MiniGoParser.For_condContext,0)


        def for_3var(self):
            return self.getTypedRuleContext(MiniGoParser.For_3varContext,0)


        def for_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 609
                self.for_cond()
                pass

            elif la_ == 2:
                self.state = 610
                self.for_3var()
                pass

            elif la_ == 3:
                self.state = 611
                self.for_range()
                pass


            self.state = 614
            self.body_block()
            self.state = 615
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_3varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def f3v_init(self):
            return self.getTypedRuleContext(MiniGoParser.F3v_initContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def f3v_modi(self):
            return self.getTypedRuleContext(MiniGoParser.F3v_modiContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_3var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_3var" ):
                return visitor.visitFor_3var(self)
            else:
                return visitor.visitChildren(self)




    def for_3var(self):

        localctx = MiniGoParser.For_3varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_3var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(MiniGoParser.FOR)
            self.state = 618
            self.f3v_init()
            self.state = 619
            self.match(MiniGoParser.SEMICOLON)
            self.state = 620
            self.expr(0)
            self.state = 621
            self.match(MiniGoParser.SEMICOLON)
            self.state = 622
            self.f3v_modi()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F3v_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def dec_type(self):
            return self.getTypedRuleContext(MiniGoParser.Dec_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_f3v_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF3v_init" ):
                return visitor.visitF3v_init(self)
            else:
                return visitor.visitChildren(self)




    def f3v_init(self):

        localctx = MiniGoParser.F3v_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_f3v_init)
        self._la = 0 # Token type
        try:
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.match(MiniGoParser.ID)
                self.state = 625
                self.assign_operator()
                self.state = 626
                self.expr(0)
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 628
                self.match(MiniGoParser.VAR)
                self.state = 629
                self.match(MiniGoParser.ID)
                self.state = 631
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID))) != 0):
                    self.state = 630
                    self.dec_type()


                self.state = 633
                self.match(MiniGoParser.ASSIGN)
                self.state = 634
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F3v_modiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assign_operator(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_operatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_f3v_modi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF3v_modi" ):
                return visitor.visitF3v_modi(self)
            else:
                return visitor.visitChildren(self)




    def f3v_modi(self):

        localctx = MiniGoParser.F3v_modiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_f3v_modi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(MiniGoParser.ID)
            self.state = 638
            self.assign_operator()
            self.state = 639
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_cond" ):
                return visitor.visitFor_cond(self)
            else:
                return visitor.visitChildren(self)




    def for_cond(self):

        localctx = MiniGoParser.For_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_for_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(MiniGoParser.FOR)
            self.state = 642
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_range" ):
                return visitor.visitFor_range(self)
            else:
                return visitor.visitChildren(self)




    def for_range(self):

        localctx = MiniGoParser.For_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_for_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.match(MiniGoParser.FOR)
            self.state = 645
            self.match(MiniGoParser.ID)
            self.state = 646
            self.match(MiniGoParser.COMMA)
            self.state = 647
            self.match(MiniGoParser.ID)
            self.state = 648
            self.match(MiniGoParser.ASSIGN_OP)
            self.state = 649
            self.match(MiniGoParser.RANGE)
            self.state = 650
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(MiniGoParser.BREAK)
            self.state = 653
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 655
            self.match(MiniGoParser.CONTINUE)
            self.state = 656
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var_rec(self):
            return self.getTypedRuleContext(MiniGoParser.Scalar_var_recContext,0)


        def LRB(self):
            return self.getToken(MiniGoParser.LRB, 0)

        def RRB(self):
            return self.getToken(MiniGoParser.RRB, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(MiniGoParser.List_exprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            self.scalar_var_rec(0)
            self.state = 659
            self.match(MiniGoParser.LRB)
            self.state = 661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ADD) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LRB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC) | (1 << MiniGoParser.BIN) | (1 << MiniGoParser.OCT) | (1 << MiniGoParser.HEX) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 660
                self.list_expr()


            self.state = 663
            self.match(MiniGoParser.RRB)
            self.state = 664
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(MiniGoParser.IgnoreContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(MiniGoParser.RETURN)
            self.state = 668
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.ADD) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LRB) | (1 << MiniGoParser.LSB) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.DEC) | (1 << MiniGoParser.BIN) | (1 << MiniGoParser.OCT) | (1 << MiniGoParser.HEX) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STR_LIT))) != 0):
                self.state = 667
                self.expr(0)


            self.state = 670
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = MiniGoParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NEWLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MiniGoParser.LCB, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RCB(self):
            return self.getToken(MiniGoParser.RCB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_body_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_block" ):
                return visitor.visitBody_block(self)
            else:
                return visitor.visitChildren(self)




    def body_block(self):

        localctx = MiniGoParser.Body_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_body_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 674
            self.match(MiniGoParser.LCB)
            self.state = 675
            self.list_statement()
            self.state = 676
            self.match(MiniGoParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.array_init_sempred
        self._predicates[12] = self.expr_sempred
        self._predicates[13] = self.expr1_sempred
        self._predicates[14] = self.expr2_sempred
        self._predicates[15] = self.expr3_sempred
        self._predicates[16] = self.expr4_sempred
        self._predicates[18] = self.expr6_sempred
        self._predicates[55] = self.scalar_var_rec_sempred
        self._predicates[56] = self.array_init_sca_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def array_init_sempred(self, localctx:Array_initContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def scalar_var_rec_sempred(self, localctx:Scalar_var_recContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def array_init_sca_sempred(self, localctx:Array_init_scaContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




