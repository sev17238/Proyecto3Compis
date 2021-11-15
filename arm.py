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