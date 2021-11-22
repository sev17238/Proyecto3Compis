##################################
# DIEGO SEVILLA 17238
# COMPILADORES 
##################################
# arm.py
##################################
# Traduccion de codigo intermedio a arm
###################################

import re

# $0x80 finalizar 
# Retorno en EAX

# .section .data

# .section .text
# .global _start

class register():
    def __init__(self, name):
        self.name = name
        self.available = True

    def change_available(self):
        self.available = not(self.available)

# REGS = ["%eax",
#     "%ebx",
#     "%ecx",
#     "%edx",
#     "%edi",
#     "%esi"
# ]

REGISTERS = ["R15", "R14", "R13", "R12", "R11", "R10", "R9", "R8", "R7", "R6", "R5", "R4", "R3", "R2", "R1", "R0"]

OPERATORS = ["+", "-", "*", "/", "%"]

TRUE_REGIS = []

MEMORY_FUNCTION_CONV = {
    0:  -4  ,
    4:  -8  ,
    8:  -12 ,
    12: -16 ,
    16: -20 ,
    20: -24 ,
    24: -28 ,
    28: -32 ,
    32: -36 ,
    36: -40 ,
    40: -44 ,
    44: -48 ,
    48: -52 ,
    52: -56 ,
    56: -60 ,
    60: -64 ,
}



def operationsFunction(first_operand,second_operand,operation,last_linee):
    arm_code = ''
    last_line = last_linee.split(' ')
    if first_operand.isnumeric(): 
        memory_address = first_operand
    elif re.search("^t.*[0-9]$", first_operand): #check if has pattern for t0 - t9:
        first_ = last_line[2]
        second_ = last_line[4]
        memory_address1 = getBracketsContent(first_)
        memory_address2 = getBracketsContent(second_)
        if memory_address1 > memory_address2:
            memory_address = memory_address1 + 4
        else:
            memory_address = memory_address2 + 4
    else:
        memory_address = getBracketsContent(first_operand)

    if second_operand.isnumeric(): 
        memory_address2 = second_operand
    elif re.search("^t.*[0-9]$", second_operand): #check if has pattern for t0 - t9:
        first_ = last_line[2]
        second_ = last_line[4]
        memory_address1 = getBracketsContent(first_)
        memory_address2 = getBracketsContent(second_)
        if memory_address1 > memory_address2:
            memory_address2 = memory_address1 + 4
        else:
            memory_address2 = memory_address2 + 4
    else:
        memory_address2 = getBracketsContent(second_operand)

    regi1 = REGISTERS.pop()
    regi2 = REGISTERS.pop()
    arm_code += "\tldr " + regi1 + ", [sp, #" + str(memory_address) + "]\n"
    arm_code += "\tldr " + regi2 + ", [sp, #" + str(memory_address2) + "]\n"

    if operation == 'add': arm_code += "\tadd " + regi1 + ", " + regi1 + ", " + regi2 + "\n"
    elif operation == 'sub': arm_code += "\tsub " + regi1 + ", " + regi1 + ", " + regi2 + "\n"
    elif operation == 'mul': arm_code += "\tmul " + regi1 + ", " + regi1 + ", " + regi2 + "\n"

    #!handle temporals like m#[#] = t#
    if memory_address > memory_address2:
        arm_code += "\tstr " + regi1 + ", [sp, #" + str(int(memory_address) + 4) + "]\n"
    else:
        arm_code += "\tstr " + regi1 + ", [sp, #" + str(int(memory_address2) + 4) + "]\n"

    #?if last function
        #arm_code += "\tmov " + regi1 + " " +  str(function_alocated_space-4) + "\n"

    REGISTERS.append(regi2)
    REGISTERS.append(regi1)

    return arm_code

def getMemoryAddressInsideFunction(allocated_memory,inter_memory):
    memory_address_to_use = int(allocated_memory) - (int(inter_memory)+4)
    return str(memory_address_to_use)

def getBracketsContent(abstract_inter_var):
    len_str = len(abstract_inter_var)
    try:
        b_index = abstract_inter_var.index('[')
    except:
        return False
    pos_brackets = len_str - b_index
    brackets_content = abstract_inter_var[-pos_brackets:]
    memory_address = str(re.findall('[0-9]+', brackets_content)[0])
    return int(memory_address)

def read_lines(inter):   
    armc = []
    arm_code_all = ""
    function_alocated_space = 0
    actual_temp = 0
    line_cnt = 0
    for line in inter:
        arm_code = ""
        parts = line.split(" ")

        # para funciones, etiquetas
        if len(parts) == 1:
            arm_code += parts[0] +"\n"
        elif len(parts) == 2:
            # func end
            if parts[0] == "func" and parts[1] == "end":
                arm_code += "\tadd sp, sp, #" + str(function_alocated_space)+'\n'
                function_alocated_space = 0
                arm_code += "\tbx lr\n"
            # Goto L#
            if parts[0] == "Goto":
                arm_code += "\tje " + parts[1]
        elif len(parts) == 3:
            # func begin #
            if parts[0] == "func" and parts[1] == 'begin':
                memory_pos = re.findall('[0-9]+', parts[2])
                memory_pos = parts[2]
                function_alocated_space = memory_pos
                arm_code += "\tsub sp, sp, #"+memory_pos+"\n"

            # m#[#] = literal
            elif parts[0] != "func" and parts[2].isnumeric():
                reg1 = REGISTERS.pop()
                right_side = parts[2]

                left_side = parts[0]
                memory_address = getBracketsContent(left_side)

                arm_code += "\tmov " + reg1 + ", #" + right_side + "\n"
                arm_code += "\tstr " + reg1 + ", [sp, #" + memory_address + "]\n"
                REGISTERS.append(reg1)
            # m#[#] = t#
            elif parts[0] != "func" and re.search("^t.*[0-9]$", parts[2]): #check if hast pattern for t0 - t9
                # !this is handled in if len(parts) == 5:
                continue
            
            # push param m#[#]
            elif parts[0] == 'push':
                continue

            # m#[#] = m#[#]
            else:
                continue
            
        elif len(parts) == 4:
            # para llamada a metodos
            if parts[2] == '_MCall':
                continue

        elif len(parts) == 5:
            if parts[3] == "+":
                #left_side = parts[0]
                first_operand = parts[2]
                second_operand = parts[4]


                '''if first_operand.isnumeric(): 
                    memory_address = first_operand
                else:
                    memory_address = getBracketsContent(first_operand)

                if second_operand.isnumeric(): 
                    memory_address2 = second_operand
                else:
                    memory_address2 = getBracketsContent(second_operand)

                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "\tldr " + regi1 + ", [sp, #" + memory_address + "]\n"
                arm_code += "\tldr " + regi2 + ", [sp, #" + memory_address2 + "]\n"

                arm_code += "\tadd " + regi1 + ", " + regi1 + ", " + regi2 + "\n"
                
                #!handle temporals like m#[#] = t#
                if memory_address > memory_address2:
                    arm_code += "\tstr " + regi1 + ", [sp, #" + str(int(memory_address) + 4) + "]\n"
                else:
                    arm_code += "\tstr " + regi1 + ", [sp, #" + str(int(memory_address2) + 4) + "]\n"

                #?if last function
                    #arm_code += "\tmov " + regi1 + " " +  str(function_alocated_space-4) + "\n"

                REGISTERS.append(regi2)
                REGISTERS.append(regi1)'''

                last_line = inter[line_cnt-1]
                arm_code += operationsFunction(first_operand,second_operand,'add',last_line)
            
            elif parts[3] == "-":
                first_operand = parts[2]
                second_operand = parts[4]

                last_line = inter[line_cnt-1]
                arm_code += operationsFunction(first_operand,second_operand,'sub',last_line)

            elif parts[3] == "*":
                first_operand = parts[2]
                second_operand = parts[4]

                last_line = inter[line_cnt-1]
                arm_code += operationsFunction(first_operand,second_operand,'mul',last_line)

            elif parts[3] == "<":
                continue

            elif parts[3] == ">":
                continue

        arm_code_all += arm_code
        line_cnt += 1
        armct = arm_code.replace("\t","")
        armc.append(armct.split("\n")[0])

    return arm_code_all


def data(inter):
    arm_code = ".section .data\n"
    for line in inter:
        if "func begin" in line:
            name = inter[inter.index(line)-1]
            parts = line.split(" ")
            number = parts[2]
            times = int(number) / 4
            arm_code += name.replace(":", "") + " TIMES " + str(int(times)) + " DB 0\n"
    return arm_code


def data2(scopes):
    arm_code = ".section .data\n"
    for sc in scopes:
        scope = scopes[sc]
        #arm_code += scope.name[0] + str(scope.id) + " TIMES " + str(int(scope.get_size()/4)) + " DB 0\n"
    return arm_code

def getReg(inter_expression):
    x = inter_expression[0]
    y = inter_expression[2]
    z = inter_expression[3]
    registers_to_use = []
    for i in REGISTERS:
        if x in REGISTERS[i]:
            pass
        else:
            registers_to_use.append(x)
        if y in REGISTERS[i]:
            pass
        else:
            registers_to_use.append(y)
        if z in REGISTERS[i]:
            pass
        else:
            registers_to_use.append(z)
    
    return registers_to_use



def to_arm(inter, scopes):
    # for regis in REGS:
    #     reg = register(regis)
    #     REGISTERS.append(reg)
    print("////////final code///////////")
    inter = inter.split("\n")
    num = 15
    # arm_code = data(inter)
    arm_code = data2(scopes)
    while num > 0:
        regi = register("R" + str(num))
        TRUE_REGIS.append(regi)
        num -= 1
    arm_code += ".section .text\n.global main\n"
    arm_code += read_lines(inter)
    print(arm_code)
