from word import *

class Registers:
    def __init__(self):
        self.rA = Word(0)
        self.rX = Word(0)
        self.rJ = Word(0)
        self.r = [Word(0) for _ in xrange(7)]

    def __getitem__(self, x):
        if isinstance(x, slice):
            item = x.start
            left = x.stop if x.stop is not None else 0
            right = x.step if x.step is not None else 5
        else:
            item = x
            left = 0
            right = 5
        return self.reg(item)[left:right]

    def __setitem__(self, x, value):
        if isinstance(x, slice):
            item = x.start
            left = x.stop if x.stop is not None else 0
            right = x.step if x.step is not None else 5
        else:
            item = x
            left = 0
            right = 5
        self.reg(item)[left:right] = value
        #TODO: Hum, I broke this hook splitting this code in registers.py
        #old_value = self[item]
        #changed = old_value.word_list != self[item].word_list
        #if self.cpu_hook is not None and changed:
        #    self.cpu_hook(item, old_value, self[item])

    def reg(self, r):
        if isinstance(r, int):
            return self.r[r]
        else:
            if r == 'A':
                return self.rA
            elif r == 'X':
                return self.rX
            elif r == 'J':
                return self.rJ
        raise Exception("Unexisting register %s" % r)

    def set_reg(self, r, w):
        if isinstance(r, int):
            self.r[r] = Word(w)
        else:
            if r == 'A':
                self.rA = Word(w)
            elif r == 'X':
                self.rX = Word(w)
            elif r == 'J':
                self.rJ = Word(w)
        raise Exception("Unexisting register %s" % r)

