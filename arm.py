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


def read_lines(inter):   
    arm_code_all = ""
    function_alocated_space = 0
    for line in inter:
        arm_code = ""
        parts = line.split(" ")

        # para funciones, etiquetas
        if len(parts) == 1:
            arm_code += parts[0] +"\n"
        if len(parts) == 2:
            # func end
            if parts[0] == "func" and parts[1] == "end":
                arm_code += "add sp, sp, #" + str(function_alocated_space)+'\n'
                function_alocated_space = 0
                arm_code += "bx lr\n"
            # Goto L#
            if parts[0] == "Goto":
                arm_code += "je " + parts[1]
        if len(parts) == 3:
            # func begin #
            if parts[0] == "func" and parts[1] == 'begin':
                memory_pos = re.findall('[0-9]+', parts[2])
                memory_pos = parts[2]
                function_alocated_space = memory_pos
                arm_code += "sub sp, sp, #"+memory_pos+"\n"

            # m#[#] = literal
            if parts[0] != "func" and parts[2].isnumeric():
                reg1 = REGISTERS.pop()
                right_side = str(2)

                left_side = parts[0]
                len_str = len(left_side)
                try:
                    b_index = left_side.index('[')
                except:
                    b_index = 0
                pos_brackets = len_str - b_index
                brackets_content = left_side[-pos_brackets:]

                memory_address = str(re.findall('[0-9]+', brackets_content)[0])

                arm_code += "mov " + reg1 + ", #" + right_side + "\n"
                arm_code += "str " + reg1 + ", [sp, #" + memory_address + "]\n"
                REGISTERS.append(reg1)
            # m#[#] = m#[#]
            else:
                pass
            # push param m#[#]
            if parts[0] == 'push':
                pass
            
        if len(parts) == 4:
            # para llamada a metodos
            if parts[2] == '_MCall':
                pass

        if len(parts) == 5:
            if parts[3] == "+":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[2] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[4] + "\n"
                arm_code += "add " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)
            
            if parts[3] == "-":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[2] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[4] + "\n"
                arm_code += "sub " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)

            if parts[3] == "*":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[2] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[4] + "\n"
                arm_code += "sub " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)

            if parts[3] == "<":
                pass

            if parts[3] == ">":
                pass

        arm_code_all += arm_code

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
