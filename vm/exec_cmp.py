# cmp* (c_code = 56..63)

# ALL DONE
from word_parser import *

def _cmp(reg):
    def __cmp(vmachine):
       vmachine["cycles"] += 2
       addr = WordParser.get_full_addr(vmachine, check_mix_addr=True)
       if not vmachine.is_readable(addr):
           raise MemReadLockedError((addr, addr))
       left, right = WordParser.get_field_spec(vmachine)
       vmachine["cf"] = cmp(int(vmachine.registers[reg][left:right]),
                            int(vmachine[addr:left:right]))
    return __cmp

cmpa = _cmp("A")
cmp1 = _cmp(1)
cmp2 = _cmp(2)
cmp3 = _cmp(3)
cmp4 = _cmp(4)
cmp5 = _cmp(5)
cmp6 = _cmp(6)
cmpx = _cmp("X")
