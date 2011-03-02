from word import *

class Registers:
    def __init__(self):
        self.rA = Word(0)
        self.rX = Word(0)
        self.rJ = Word(0)
        self.r = [Word(0) for _ in xrange(7)]

    def __getitem__(self, x):
        if isinstance(x, slice):
            left = x.stop if x.stop is not None else 0
            right = x.step if x.step is not None else 5
            return self.reg(x.start)[left:right]
        else:
            return self.reg(x)

    def __setitem__(self, x, value):
        if isinstance(x, slice):
            item = x.start
            left = x.stop if x.stop is not None else 0
            right = x.step if x.step is not None else 5
            self.reg(item)[left:right] = value
        else:
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

    def reg(self, r):
        if r == 'A':
            return self.rA
        elif r == 'X':
            return self.rX
        elif r == 'J':
            return self.rJ
        else:
            return self.r[r]

