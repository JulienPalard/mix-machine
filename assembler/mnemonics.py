# mnemonics.py

# File for creating dictionary with commands

class Cmd:
  def __init__(self, mnemonic, c_code = None, f_code = None):
    self.mnemonic = mnemonic
    self.c_code = c_code
    self.f_code = f_code
  
  def __str__(self):
    return "%s %i %i" % (self.mnemonic, self.c_code, self.f_code)

# commands dictionary with mnemonic as a key

__operands = {
"NOP" :   Cmd("NOP", 0, 0),
"ADD" :   Cmd("ADD", 1, 5),
"SUB" :   Cmd("SUB", 2, 5),
"MUL" :   Cmd("MUL", 3, 5),
"DIV" :   Cmd("DIV", 4, 5),
"NUM" :   Cmd("NUM", 5, 0),
"CHAR" :  Cmd("CHAR", 5, 1),
"HLT" :   Cmd("HLT", 5, 2),
"SLA" :   Cmd("SLA", 6, 0),
"SRA" :   Cmd("SRA", 6, 1),
"SLAX" :  Cmd("SLAX", 6, 2),
"SRAX" :  Cmd("SRAX", 6, 3),
"SLC" :   Cmd("SLC", 6, 4),
"SRC" :   Cmd("SRC", 6, 5),
"MOVE" :  Cmd("MOVE", 7, 1),
"LDA" :   Cmd("LDA", 8, 5),
"LD1" :   Cmd("LD1", 9, 5),
"LD2" :   Cmd("LD2", 10, 5),
"LD3" :   Cmd("LD3", 11, 5),
"LD4" :   Cmd("LD4", 12, 5),
"LD5" :   Cmd("LD5", 13, 5),
"LD6" :   Cmd("LD6", 14, 5),
"LDX" :   Cmd("LDX", 15, 5),
"LDAN" :  Cmd("LDAN", 16, 5),
"LD1N" :  Cmd("LD1N", 17, 5),
"LD2N" :  Cmd("LD2N", 18, 5),
"LD3N" :  Cmd("LD3N", 19, 5),
"LD4N" :  Cmd("LD4N", 20, 5),
"LD5N" :  Cmd("LD5N", 21, 5),
"LD6N" :  Cmd("LD6N", 22, 5),
"LDXN" :  Cmd("LDXN", 23, 5),
"STA" :   Cmd("STA", 24, 5),
"ST1" :   Cmd("ST1", 25, 5),
"ST2" :   Cmd("ST2", 26, 5),
"ST3" :   Cmd("ST3", 27, 5),
"ST4" :   Cmd("ST4", 28, 5),
"ST5" :   Cmd("ST5", 29, 5),
"ST6" :   Cmd("ST6", 30, 5),
"STX" :   Cmd("STX", 31, 5),
"STJ" :   Cmd("STJ", 32, 5),
"STZ" :   Cmd("STZ", 33, 5),
"JBUS" :  Cmd("JBUS", 34, 0),
"IOC" :   Cmd("IOC", 35, 0),
"IN" :    Cmd("IN", 36, 0),
"OUT" :   Cmd("OUT", 37, 0),
"JRED" :  Cmd("JRED", 38, 0),
"JMP" :   Cmd("JMP", 39, 0),
"JSJ" :   Cmd("JSJ", 39, 1),
"JOV" :   Cmd("JOV", 39, 2),
"JNOV" :  Cmd("JNOV", 39, 3),
"JL" :    Cmd("JL", 39, 4),
"JE" :    Cmd("JE", 39, 5),
"JG" :    Cmd("JG", 39, 6),
"JGE" :   Cmd("JGE", 39, 7),
"JNE" :   Cmd("JNE", 39, 8),
"JLE" :   Cmd("JLE", 39, 9),
"JAN" :   Cmd("JAN", 40, 0),
"JAZ" :   Cmd("JAZ", 40, 1),
"JAP" :   Cmd("JAP", 40, 2),
"JANN" :  Cmd("JANN", 40, 3),
"JANZ" :  Cmd("JANZ", 40, 4),
"JANP" :  Cmd("JANP", 40, 5),
"J1N" :   Cmd("J1N", 41, 0),
"J1Z" :   Cmd("J1Z", 41, 1),
"J1P" :   Cmd("J1P", 41, 2),
"J1NN" :  Cmd("J1NN", 41, 3),
"J1NZ" :  Cmd("J1NZ", 41, 4),
"JANP" :  Cmd("JANP", 41, 5),
"J2N" :   Cmd("J2N", 42, 0),
"J2Z" :   Cmd("J2Z", 42, 1),
"J2P" :   Cmd("J2P", 42, 2),
"J2NN" :  Cmd("J2NN", 42, 3),
"J2NZ" :  Cmd("J2NZ", 42, 4),
"J2NP" :  Cmd("J2NP", 42, 5),
"J3N" :   Cmd("J3N", 43, 0),
"J3Z" :   Cmd("J3Z", 43, 1),
"J3P" :   Cmd("J3P", 43, 2),
"J3NN" :  Cmd("J3NN", 43, 3),
"J3NZ" :  Cmd("J3NZ", 43, 4),
"J3NP" :  Cmd("J3NP", 43, 5),
"J4N" :   Cmd("J4N", 44, 0),
"J4Z" :   Cmd("J4Z", 44, 1),
"J4P" :   Cmd("J4P", 44, 2),
"J4NN" :  Cmd("J4NN", 44, 3),
"J4NZ" :  Cmd("J4NZ", 44, 4),
"J4NP" :  Cmd("J4NP", 44, 5),
"J5N" :   Cmd("J5N", 45, 0),
"J5Z" :   Cmd("J5Z", 45, 1),
"J5P" :   Cmd("J5P", 45, 2),
"J5NN" :  Cmd("J5NN", 45, 3),
"J5NZ" :  Cmd("J5NZ", 45, 4),
"J5NP" :  Cmd("J5NP", 45, 5),
"J6N" :   Cmd("J6N", 46, 0),
"J6Z" :   Cmd("J6Z", 46, 1),
"J6P" :   Cmd("J6P", 46, 2),
"J6NN" :  Cmd("J6NN", 46, 3),
"J6NZ" :  Cmd("J6NZ", 46, 4),
"J6NP" :  Cmd("J6NP", 46, 5),
"JXN" :   Cmd("JXN", 47, 0),
"JXZ" :   Cmd("JXZ", 47, 1),
"JXP" :   Cmd("JXP", 47, 2),
"JXNN" :  Cmd("JXNN", 47, 3),
"JXNZ" :  Cmd("JXNZ", 47, 4),
"JXNP" :  Cmd("JXNP", 47, 5),
"INCA" :  Cmd("INCA", 48, 0),
"DECA" :  Cmd("DECA", 48, 1),
"ENTA" :  Cmd("ENTA", 48, 2),
"ENNA" :  Cmd("ENNA", 48, 3),
"INC1" :  Cmd("INC1", 49, 0),
"DEC1" :  Cmd("DEC1", 49, 1),
"ENT1" :  Cmd("ENT1", 49, 2),
"ENN1" :  Cmd("ENN1", 49, 3),
"INC2" :  Cmd("INC2", 50, 0),
"DEC2" :  Cmd("DEC2", 50, 1),
"ENT2" :  Cmd("ENT2", 50, 2),
"ENN2" :  Cmd("ENN2", 50, 3),
"INC3" :  Cmd("INC3", 51, 0),
"DEC3" :  Cmd("DEC3", 51, 1),
"ENT3" :  Cmd("ENT3", 51, 2),
"ENN3" :  Cmd("ENN3", 51, 3),
"INC4" :  Cmd("INC4", 52, 0),
"DEC4" :  Cmd("DEC4", 52, 1),
"ENT4" :  Cmd("ENT4", 52, 2),
"ENN4" :  Cmd("ENN4", 52, 3),
"INC5" :  Cmd("INC5", 53, 0),
"DEC5" :  Cmd("DEC5", 53, 1),
"ENT5" :  Cmd("ENT5", 53, 2),
"ENN5" :  Cmd("ENN5", 53, 3),
"INC6" :  Cmd("INC6", 54, 0),
"DEC6" :  Cmd("DEC6", 54, 1),
"ENT6" :  Cmd("ENT6", 54, 2),
"ENN6" :  Cmd("ENN6", 54, 3),
"INCX" :  Cmd("INCX", 55, 0),
"DECX" :  Cmd("DECX", 55, 1),
"ENTX" :  Cmd("ENTX", 55, 2),
"ENNX" :  Cmd("ENNX", 55, 3),
"CMPA" :  Cmd("CMPA", 56, 5),
"CMP1" :  Cmd("CMP1", 57, 5),
"CMP2" :  Cmd("CMP2", 58, 5),
"CMP3" :  Cmd("CMP3", 59, 5),
"CMP4" :  Cmd("CMP4", 60, 5),
"CMP5" :  Cmd("CMP5", 61, 5),
"CMP6" :  Cmd("CMP6", 62, 5),
"CMPX" :  Cmd("CMPX", 63, 5)
}
__directives = ("EQU","ORIG","END","CON","ALF")


# real operands
__cmds = dict(operands)

# directives
for s in __directives:
	__cmds[s] = Cmd(s)



def is_valid_mnemonic(mnemonic):
  return mnemonic in __cmds

def must_have_operand(mnemonic):
  # FIXME
  return False
