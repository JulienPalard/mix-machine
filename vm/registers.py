from word import *

class Registers:
    def __init__(self, cpu_hook):
        self.cpu_hook = cpu_hook
        self.rA = Word()
        self.rX = Word()
        self.rJ = Word()
        self.r = [Word() for _ in xrange(7)]

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
        if self.cpu_hook is None:
            if x == 'A':
                self.rA = Word(value)
            elif x == 'X':
                self.rX = Word(value)
            elif x == 'J':
                self.rJ = Word(value)
            else:
                self.r[x] = Word(value)
        else:
            if x == 'A':
                old = self.rA
                self.rA = Word(value)
                self.cpu_hook('rA', old, self.rA)
            elif x == 'X':
                old = self.rX
                self.rX = Word(value)
                self.cpu_hook('rX', old, self.rX)
            elif x == 'J':
                old = self.rJ
                self.rJ = Word(value)
                self.cpu_hook('rJ', old, self.rJ)
            else:
                old = self.r[x]
                self.r[x] = Word(value)
                self.cpu_hook('r%d' % x, old, self.r[x])

