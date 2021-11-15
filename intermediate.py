##################################
# DIEGO SEVILLA 17238
# COMPILADORES 
##################################
# intermediate.py
##################################

from DecafVisitor import DecafVisitor

DEFAULT_TYPES = {
    'int': 4,
    'boolean': 1,
    'char': 1,
}

class Inter(DecafVisitor):

    def __init__(self, scopes):
        DecafVisitor.__init__(self)
        self.tree = None
        #self.og_registers = ["t0", "t1","t2", "t3", "t4", "t5", "t6", "t7", "t8","t9","t10","t11", "t12","t13", "t14", "t15", "t16", "t17", "t18", "t19","t20","t21"]
        self.og_registers = ["t0", "t1","t2", "t3", "t4", "t5", "t6", "t7", "t8","t9","t10"]
        self.registers = self.og_registers[::-1]
        self.line = ""
        self.label = 0
        self.scope_ids = 0
        self.scope_actual = ["global"]
        self.scopes = scopes
        self.cumulative = 0

    def visitProgram(self, ctx):
        self.visitChildren(ctx)
        return 0
    
    def visitMethodDeclaration(self, ctx):
        name = ctx.ID().getText()
        self.scope_ids +=1
        self.scope_actual.append(name)
        start = name +": \n"
        actual = self.scopes[self.scope_actual[-1]]
        start += "func begin " + str(actual.get_size())  + "\n"
        self.line += start
        self.visitChildren(ctx)
        end = "func end \n"
        self.line += end
        self.scope_actual.pop()
        return 0
    
    def visitStmnt_return(self,ctx):
        if ctx.expression:
            register = self.visit(ctx.expression())
            self.line += "Return " + str(register) + "\n"
            if register in self.og_registers:
                self.registers.append(register)
        return 0

    def visitMethodCall(self, ctx):
        method = ctx.ID().getText()
        if ctx.arg() :
            for arg in ctx.arg():
                param = self.visit(arg)
                self.line += "push param " + str(param) + "\n"
                if param in self.og_registers:
                    self.registers.append(param)
        register = self.registers.pop()
        self.line += register + " = _MCall " + method + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        #self.visitChildren(ctx)'''
        return register
        #return 0

    def visitExpr_par(self, ctx):
        return self.visit(ctx.expression())

    def visitWhileScope(self, ctx):
        self.scope_ids += 1
        self.scope_actual.append("while" + str(self.scope_ids))
        start_label = "L" + str(self.label)
        while_line = start_label + ":\n"
        self.label += 1
        self.line += while_line
        register = self.visit(ctx.expression())
        true_label = "L" + str(self.label)
        self.label += 1
        while_cont1 = "IfZ " + register + " Goto " + true_label +" \n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += while_cont1
        self.line += "Goto " + "L_END_WHILE" + "\n"
        self.line += true_label + ":\n"
        self.visit(ctx.block())
        while_loop = "Goto " + start_label + " \n"
        self.line += while_loop
        self.line += "L_END_WHILE" + "\n"
        self.scope_actual.pop()
        return 0

    def visitIfScope(self, ctx):
        self.scope_ids += 1
        name = "if" + str(self.scope_ids)
        self.scope_actual.append(name)
        register = self.visit(ctx.expression())
        salto = "L" + str(self.label)
        self.label += 1
        if_line = "IfZ " + register + " Goto " + salto + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += if_line
        self.line += "Goto " + "L" + str(self.label) + "\n"
        self.line += salto + ": \n"
        self.visit(ctx.block1)
        end = ""
        if ctx.block2:
            #end_line = salto + ": \n"
            end = "L_END_IF"
            self.line += "Goto " + end + "\n"
            elsee = "L" + str(self.label)
            self.line += elsee + ":\n"
            self.visit(ctx.block2)
            self.label += 1
        else:
            end_line = "L" + str(self.label) + ": \n"
            self.line += end_line
        if len(end) > 0:
            self.line += end + "\n"
        self.scope_actual.pop()
        return 0

    def visitExpr_arith_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        operation = register + " = " + str(left) + " " + ctx.p_arith_op().getText()+ " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += operation + "\n"
        return register

    def visitExpr_minus(self, ctx):
        expp = self.visit(ctx.expression())
        sign = 'minus'
        register = self.registers.pop()
        operation = register + " = " + sign + " " + str(expp) 
        if expp in self.og_registers:
            self.registers.append(expp)
        self.line += operation + "\n"
        return register

    def visitExpr_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop() #se hace pop del registro o temporale en el tope
        operation = register + " = " + str(left) + " " + ctx.arith_op().getText() + " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += operation + "\n"
        return register

    def visitExpr_rel_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        operation = register + " = " + left +" " + ctx.rel_op().getText()+ " " + right
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += operation + "\n"
        return register
    
    def visitExpr_eq_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        operation = register + " = " + left + " "+ctx.eq_op().getText()+ " " + right
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += operation + "\n"
        return register

    def visitExpr_cond_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        operation = register + " = " + left +" " +ctx.cond_op().getText()+ " " + right
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += operation + "\n"
        return register

    def visitExpr_literal(self, ctx):
        return self.visitChildren(ctx)

    def visitStmnt_equal(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        equal = str(left) + " = " + str(right) + "\n"
        if right in self.og_registers:
            self.registers.append(right)
        self.line += equal
        return left
    
    def visitLiteral(self, ctx):
        val = self.visitChildren(ctx)
        return val[1]
    
    def visitInt_literal(self, ctx):
        num = ctx.NUM()
        return ("int", (num.getText()))
    
    def visitChar_literal(self, ctx):
        char = ctx.CHAR()
        return ("char", char.getText())
    
    def visitBool_literal(self, ctx):
        boolean = ctx.getText()
        if boolean == 'true':
            boolean = "1"
        else:
            boolean = "0"
        return ("boolean", boolean)
    
    def visitLocation(self, ctx, parent = None):
        """visitante de locacion

        Args:
            ctx (obj): la estructura del nodo en cuestion
            parent (obj, optional): [description]. Defaults to None.

        Returns:
            variable: el valor de la locacion
        """
        name = ctx.ID().getText()
        offset = 0

        for scope in self.scope_actual[::-1]:
            actualScope = self.scopes[scope]
            if symbol := actualScope.get_symbol(name):
                break

        #sumamos el offset de todos los simbolos anteriores hasta llegar al actual
        for symbol in actualScope.symbols:
            if symbol.name == name:
                break
            else:
                if symbol.type in DEFAULT_TYPES:
                    offset += DEFAULT_TYPES[symbol.type]
                else:
                    offset += actualScope.get_instance_size(symbol.type.replace('struct', "")) * symbol.reps

        # CASOS DE ASIGNACIONES A POSICIONES EN ARREGLOS Y MAS
        if ctx.expression() != None:
            resp = self.visit(ctx.expression())
            try:
                expr_actual = ctx.expression().getText()
                
                #En esta parte se realiza la multiplicacion del tamaño del tipo por la posicion a la que se 
                #esta asignando dentro de un arreglo.
                if symbol.type in DEFAULT_TYPES:
                    offset += DEFAULT_TYPES[symbol.type] * int(expr_actual)
                    
                    ##Pasos explicitos --------------------
                    localOffset = 0
                    repsArray = []
                    # s es el numero de variable encontrado en el ambito actual. Ej. La 3ra variable encontrada
                    # en main() antes de la asignacion al arreglo en cuestion.
                    for s in range(0,len(actualScope.symbols)):
                        sym = actualScope.symbols[s]
                        repsArray.append(int(sym.reps))
                        if sym.name == name:
                            repsArray.pop()
                            resultt = 0
                            for rep in repsArray:
                                resultt += rep*4
                            localOffset = resultt
                            break
                                
                    register = self.registers.pop()
                    self.line += register + ' = ' + str(DEFAULT_TYPES[symbol.type]) + ' * '+ str(expr_actual) + "\n"
                    registerNext = self.registers.pop()
                    self.line += registerNext + ' = ' + str(localOffset) + ' + '+ register + "\n"

                    sName = actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + registerNext + "]"
                    return value
                    ##END Pasos explicitos --------------------
                else:
                    sym_type = symbol.type.replace("struct", "")
                    offset += actualScope.get_instance_size(sym_type) * int(expr_actual)

                    ##Pasos explicitos --------------------
                    register = self.registers.pop()
                    self.line += register + ' = ' + '0' + ' + '+ str(offset) + "\n"
                    sName = actualScope.name[0] + str(actualScope.id)
                    value  = sName + "[" + register + "]"
                    return value
                    ##END Pasos explicitos --------------------
            except Exception as e:
                #print(e)
                register = self.registers.pop()
                if symbol.type in DEFAULT_TYPES:
                    self.line += register + " = " + resp + " * " + str(DEFAULT_TYPES[symbol.type]) + "\n"
                else:
                    sym_type = symbol.type.replace("struct", "")
                    self.line += register + " = " + resp + " * " + str(actualScope.get_instance_size(sym_type)) + "\n"
                offset = register

        
        # CASOS DE ASIGNACIONES A STRUCTS
        # Se revisan los dot locations y se busca en cada struct para calcular el offset
        elif ctx.location() != None:
            loc = ctx.location().getText()
            locc = loc.split('.')
            two = False
            offsets = {}
            if len(locc) > 1:
                two = True
            # se recorre la cantidad de locaciones x.y.z
            for e in range(0,len(locc)):
                ref = locc[e]
                #se recorren los instantiables del diccionairio de scopes
                for scp, inst in self.scopes.items():
                    strucs = inst.get_structs()
                    #se recorren los structs
                    for struc in strucs:
                        atts = struc.get_sub_attributes()
                        #se recorren las variables dentro del struct
                        for i in range(0,len(atts)):
                            att = atts[i]
                            if ref == att.name:
                                #simplemente se revisa que numero de variable es dentro del struct para 
                                # multiplicar el numero de variable por el tamaño del tipo.
                                if i > 0:
                                    offsets[e] = i * 4
                                    #offset += i * 4
                                    break
                                elif i == 0:
                                    offsets[e] = i
                                    break
            
            localOffset = 0
            repsArray = []
            # s es el numero de variable encontrado en el ambito actual. Ej. La 3ra variable encontrada
            # en main() antes de la asignacion al struct en cuestion.
            for s in range(0,len(actualScope.symbols)):
                sym = actualScope.symbols[s]
                repsArray.append(int(sym.reps))
                if sym.name == name:
                    repsArray.pop()
                    resultt = 0
                    for rep in repsArray:
                        resultt += rep*4
                    localOffset = resultt
                    break

            register = self.registers.pop()
            if two:
                #case when there are two dot locations for the moment
                if len(offsets) > 1: 
                    self.line += register + " = " + str(offsets.get(0)) + " + " + str(offsets.get(1)) + "\n"
                elif len(offsets) == 1: 
                    keyss = []
                    for i in offsets.keys():
                        keyss.append(i)
                    if keyss[0] == 0:
                        self.line += register + " = " + str(0) + " + " + str(offsets.get(0)) + "\n"
                    elif keyss[0] == 1:
                        self.line += register + " = " + str(offsets.get(0)) + " + " + str(0) + "\n"
                else: 
                    self.line += register + " = " + str(0) + " + " + str(0) + "\n"

                register_next = self.registers.pop()  
                self.line += register_next + " = " + str(localOffset) + " + " + register + "\n"
                sName = actualScope.name[0] + str(actualScope.id)
                value  = sName + "[" + register_next + "]"
                return value
            else:
                #case when there is only one dot location
                try: 
                    self.line += register + " = " + str(localOffset) + " + " + str(offsets.get(0)) + "\n"
                except: 
                    self.line += register + " = " + str(localOffset) + " + " + str(0) + "\n"

                sName = actualScope.name[0] + str(actualScope.id)
                value  = sName + "[" + register + "]"
                return value

        sName = actualScope.name[0] + str(actualScope.id)
        value  = sName + "[" + str(offset) + "]"
        return value
