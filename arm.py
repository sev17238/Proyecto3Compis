##################################
# DIEGO SEVILLA 17238
# COMPILADORES 
##################################
# arm.py
##################################
# Traduccion de codigo intermedio a arm
###################################

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
        arm_code += scope.name[0] + str(scope.id) + " TIMES " + str(int(scope.get_size()/4)) + " DB 0\n"
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
    arm_code += ".section .text\n.global start\n"
