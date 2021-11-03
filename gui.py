##################################
# DIEGO SEVILLA 17238
# COMPILADORES 
##################################
# gui.py
##################################

from flask import Flask, render_template, request, session
from antlr4 import *
import antlr4
from DecafLexer import DecafLexer
from DecafListener import DecafListener
from DecafParser import DecafParser
from antlr4.tree.Trees import Trees
from DecafVisitor import DecafVisitor
import visitor as Visitor
import sistema_de_tipos as tables
import sys
import intermediate as inter

app  = Flask(__name__)
app.secret_key = "compis:D"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#session.get no truena

# inicio
print("start everything")


#program = open('z_int_code_tests/all.decaf', 'r+')
#program = open('z_semantic_tests/param.decaf', 'r+')
# text = program.read()
# program.close()
# text = antlr4.InputStream(text)
# lexer = DecafLexer(text)
# stream = CommonTokenStream(lexer)
# parser = DecafParser(stream)
# tree = parser.program()
# printer = DecafListener()
# walker = ParseTreeWalker()
# walker.walk(printer, tree)
# #print(Trees.toStringTree(tree, None, parser))
# visitonator = Visitor.MyDecafVisitor()
# visitonator.visit(tree)



@app.route('/')
def home():
    errors = []
    return render_template("home.html")

@app.route('/', methods = ["POST"])
def get_code():
    errors = []
    code = ""
    code = request.form["codigo"]
    session.code = code
    print("errores", errors)
    if code!= " ":
        text = antlr4.InputStream(code)
        lexer = DecafLexer(text)
        stream = CommonTokenStream(lexer)
        parser = DecafParser(stream)
        tree = parser.program()
        printer = DecafListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        visitonator = Visitor.MyDecafVisitor()
        visitonator.visit(tree)
        errors = visitonator.ERRORS
        if len(errors) > 0:
            intercode = ""
        else:
            intermedio = inter.Inter(visitonator.total_scopes)
            intermedio.visit(tree)
            intercode = intermedio.line.split("\n")
    else:
        errors = []
    return render_template("home.html", errors = errors, code = code, intercode=intercode)




if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug = True)