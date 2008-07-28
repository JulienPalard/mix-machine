import unittest
import copy

_initial_regs_values = {
  'A': [+1, 11, 22, 33, 44, 55],
  'X': [-1, 22, 33, 44, 55, 11],
  'I1': [+1, 0, 0, 0, 10, 20],
  'I2': [-1, 0, 0, 0, 22, 33],
  'I3': [+1, 0, 0, 0, 63, 25],
  'I4': [-1, 0, 0, 0, 14, 7],
  'I5': [+1, 0, 0, 0, 23, 8],
  'I6': [-1, 0, 0, 0, 46, 51],
  'J':  [+1, 0, 0, 0, 37, 14],
  'CA': 0,
  'CF': 0,
  'OF': 0,
  'HLT': 0,
}

class VM3BaseTestCase(unittest.TestCase):
  @staticmethod
  def set_vm_class(klass):
    VM3BaseTestCase.vm_class = klass
  
  def setUp(self):
    self.vm = VM3BaseTestCase.vm_class()
  
  def init_vm(self, regs = {}, memory = {}):
    ctx = {}

    # fill memory
    for adr in xrange(4000):
      ctx[adr] = memory.get(adr, self.initial_memory_value(adr))

    # fill regs
    ctx.update(_initial_regs_values)
    ctx.update(regs)

    self.ctx_before = copy.copy(ctx)

    self.vm.load(ctx)

  def exec1(self, regs = {}, memory = {}, startadr = 0):
    self.init_vm(regs, memory)

    self.cycles = self.vm.execute(at=startadr)

    self.ctx_after = self.vm.state()
    self.ctx_diff = self.do_diff()

    return self.ctx_diff

  def do_diff(self):
    diff = {}

    self.assertEqual(sorted(self.ctx_before.keys()), sorted(self.ctx_after.keys()))

    for k, v in self.ctx_after.iteritems():
      if v != self.ctx_before[k]:
        diff[k] = v

    return diff

  @staticmethod
  def initial_memory_value(adr):
    num = hash(str(adr)) % (64**5)
    
    # stolen from VM2 Word
    mask = 63
    u_num = abs(num)

    sign = +1 if adr % 2 == 0 else -1

    return [sign] + [ (u_num >> shift) & mask for shift in xrange(24, -1, -6) ] # 24 = 6 * (5-1)
