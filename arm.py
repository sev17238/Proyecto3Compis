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


def read_line(line):
    arm_code = ""
    parts = line.split(" ")

    for part in parts:
        if len(part) > 0:
            #if part == "main:":
            #    arm_code += "_start:\n"
            if parts[0] == "func" and parts[1] == 'begin':
                memory_pos = re.findall('[0-9]+', parts[2])
                arm_code += "sub sp, sp, #"+str(memory_pos[0])+"\n"
                break
            if part[-1] == ":":
                arm_code += part +"\n"

            if part == "+":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[parts.index(part)-1] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[parts.index(part)+1] + "\n"
                arm_code += "add " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)
            
            if part == "-":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[parts.index(part)-1] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[parts.index(part)+1] + "\n"
                arm_code += "sub " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)

            if part == "*":
                regi1 = REGISTERS.pop()
                regi2 = REGISTERS.pop()
                arm_code += "mov " + regi1 + " " +  parts[parts.index(part)-1] + "\n"
                arm_code += "mov " + regi2 + " " +  parts[parts.index(part)+1] + "\n"
                arm_code += "sub " + regi1 + " " + regi2 + "\n"
                REGISTERS.append(regi2)

            if part == "=":
                reg1 = REGISTERS.pop()
                #arm_code += "mov " + parts[parts.index(part)-1] + " " + parts[parts.index(part) + 1] + "\n"
                right_side = str(parts[parts.index(part) + 1])

                left_side = parts[parts.index(part)-1]
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

            
            if part == "Goto":
                arm_code += "je " + parts[parts.index(part)+ 1]
 
    if parts[0] == "func":
        if "end" in parts[1]:
            arm_code += "bx lr\n"
        # arm_code += "PUBLIC _" +parts[1] + "\n"

    return arm_code


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
    for line in inter:
        arm_code += read_line(line)
    print(arm_code)
