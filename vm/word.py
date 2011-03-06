from vm_errors import *


MAX_BYTE = 64


class Word:
    @staticmethod
    def sign(x):
        return 1 if x >= 0 else -1

    @staticmethod
    def from_dec(num):
        mask = MAX_BYTE - 1  # 1<<6 - 1
        u_num = abs(num)
        # 24 = 6 * (5-1)
        return [Word.sign(num)] + [(u_num >> shift) & mask
                                   for shift in xrange(24, -1, -6)]

    @staticmethod
    def norm_2bytes(addr):
        return Word.sign(addr) * (abs(addr) % MAX_BYTE ** 2)

    def __int__(self):
        value = self.word_list[5] \
            | self.word_list[4] << 6 \
            | self.word_list[3] << 12 \
            | self.word_list[2] << 18 \
            | self.word_list[1] << 24

        return value if self.word_list[0] == 1 else -value

    @staticmethod
    def is_word_list(word_list):
        return  len(word_list) == 6 \
            and word_list[0] in (1, -1) \
            and all([0 <= byte < MAX_BYTE \
                         for byte in word_list[1:6]])

    def __getitem__(self, x):
        return self.word_list[x]

    def __setitem__(self, x, value):
        self.word_list[x] = value

    def __getslice__(self, l, r):
        new = Word()
        if l == 0:
            new.word_list[0] = self.word_list[0]
        start = max(l - 1, 0) + 1
        end = r + 1
        new.word_list[5 - r + start: 5 - r + end] = self.word_list[start:end]
        return new

    def __setslice__(self, l, r, value):
        word = Word(value)
        if l == 0:
            self.word_list[0] = word.word_list[0]
        start = max(l - 1, 0) + 1
        end = r + 1
        self.word_list[start:end] = word.word_list[5 - r + start: 5 - r + end]

    def is_zero(self):
        return self.word_list[1:] == ([0] * 5)

    def __cmp__(self, cmp_word):
        if self.is_zero() and cmp_word.is_zero():
            return 0
        return 0 if all(self[i] == cmp_word[i] for i in xrange(0, 6)) else 1

    def __str__(self):
        return reduce(lambda x, y: "%s %02i" % (x, y),
                      self.word_list[1:6], "+" if self[0] == 1 else "-")

    def addr_str(self):
        return "%s %04i %02i %02i %02i" \
            % tuple(["+" if self[0] == 1 else "-",
                     self[1] * MAX_BYTE + self[2]] \
                        + self.word_list[3:])

    def set(self, obj=None):
        if obj is None:
            self.word_list = [+1, 0, 0, 0, 0, 0]
        elif isinstance(obj, int) or isinstance(obj, long):
            self.word_list = self.from_dec(obj)
        elif isinstance(obj, Word):
            self.word_list = obj.word_list[:]
        elif isinstance(obj, list) or isinstance(obj, tuple):
            self.word_list = list(obj)

    def __init__(self, obj=None):
        self.set(obj)
