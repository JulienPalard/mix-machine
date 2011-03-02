from word import *

class Registers:
    def __init__(self):
        self.rA = Word(0)
        self.rX = Word(0)
        self.rJ = Word(0)
        self.r = [Word(0) for _ in xrange(7)]

    def __getitem__(self, r):
        if r == 'A':
            return self.rA
        elif r == 'X':
            return self.rX
        elif r == 'J':
            return self.rJ
        else:
            return self.r[r]

    def __setitem__(self, x, value):
        if x == 'A':
            self.rA = Word(value)
        elif x == 'X':
            self.rX = Word(value)
        elif x == 'J':
            self.rJ = Word(value)
        else:
            self.r[x] = Word(value)
        #TODO: Hum, I broke this hook splitting this code in registers.py
        #old_value = self[item]
        #changed = old_value.word_list != self[item].word_list
        #if self.cpu_hook is not None and changed:
        #    self.cpu_hook(item, old_value, self[item])

