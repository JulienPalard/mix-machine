from errors import *

MAX_BYTE = 64

class Word:
  @staticmethod
  def sign(x):
    return 1 if x >= 0 else -1

  @staticmethod
  def from_dec(num):
    mask = MAX_BYTE - 1  # 1<<6 - 1
    u_num = abs(num)
    return [Word.sign(num)] + [ (u_num >> shift) & mask for shift in xrange(24, -1, -6) ]

  # or you can write word[:]
  def to_dec(self):
    return self.word_list[0] * reduce(lambda x,y: (x << 6) | y, self.word_list[1:], 0)

  @staticmethod
  def is_word_list(word_list):
    return  len(word_list) == 6\
            and word_list[0] in (1, -1)\
            and all([ 0 <= byte < MAX_BYTE for byte in word_list[1:6]])

  def __getitem__(self, x):
    return self.word_list[x]

  def __setitem__(self, x, value):
    self.word_list[x] = value

  def __getslice__(self, l, r):
    l = max(l, 0)
    r = min(r, 5)
    new = Word()
    if l == 0:
      new[0] = self[0]
    for i in xrange(r, max(l-1, 0), -1):
      new[5 - r + i] = self[i]
    return new.to_dec()

  def __setslice__(self, l, r, value):
    l = max(l, 0)
    r = min(r, 5)
    new = Word(value)
    if l == 0:
      self[0] = new[0]
    for i in xrange(r, max(l-1, 0), -1):
      self[i] = new[5 - r + i]

  def is_zero(self):
    return True if self[1:5] == 0 else False

  def __cmp__(self, cmp_word):
    if self.is_zero() and cmp_word.is_zero():
      return 0
    return 0 if all(self[i] == cmp_word[i] for i in xrange(0, 6)) else 1

  def __str__(word):
    return reduce(lambda x, y: "%s %02i" % (x, y), word.word_list[1:6], "+" if word[0] == 1 else "-")

  def __init__(self, obj = None):
    if isinstance(obj, list):
      self.word_list = obj
    elif isinstance(obj, int):
      self.word_list = self.from_dec(obj)
    else:
      self.word_list = [+1, 0, 0, 0, 0, 0]
