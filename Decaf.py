##################################
# DIEGO SEVILLA 17238
# COMPILADORES 
##################################
# Decaf.py
##################################


from antlr4 import *
import antlr4
from DecafLexer import DecafLexer
from DecafListener import DecafListener
from DecafParser import DecafParser
from antlr4.tree.Trees import Trees
from DecafVisitor import DecafVisitor
import visitor as Visitor
import sistema_de_tipos as tables
import intermediate
import arm
import sys


program = open('z_int_code_tests/all.decaf', 'r+')
#program = open('z_last_tests/quicksort.decaf', 'r+')
#program = open('z_os_tests/if.decaf', 'r+')

text = program.read()
program.close()
text = antlr4.InputStream(text)
lexer = DecafLexer(text)
stream = CommonTokenStream(lexer)
parser = DecafParser(stream)
tree = parser.program()
printer = DecafListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)
#print(Trees.toStringTree(tree, None, parser))
visitonator = Visitor.MyDecafVisitor()
visitonator.visit(tree)
cnt = 0
for error in visitonator.ERRORS:
    print(error.problem, " in line ", error.line)
    cnt += 1
#print(visitonator.total_scopes)
#print(Visitor.ERRORS)

print()

if cnt == 0:
    print('Intermediate Code Generated! \n')
    inter = intermediate.Inter(visitonator.total_scopes)
    inter.visit(tree)
    print("_________________________________")
    print("---------------------------------")
    print(inter.line)

    arm.to_arm(inter.line, visitonator.total_scopes)
else:
    print('Check Your Code! Errors!')

print()