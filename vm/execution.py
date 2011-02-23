from vm_errors import *
import exec_all
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from opcodes import opcodes

def execute(vmachine):
    # some common stuff
    if not vmachine.is_readable(vmachine.cur_addr):
        raise MemReadLockedError((vmachine.cur_addr, vmachine.cur_addr))
    current_word = vmachine.get_cur_word()
    c = current_word[5]
    f = current_word[4]
    op = opcodes.get(c, opcodes.get((c,f), None))
    vmachine.jump_to = None
    before_cycles = vmachine["cycles"]
    op(vmachine)
    if vmachine.jump_to is None:
        vmachine["cur_addr"] += 1
    else:
        vmachine["cur_addr"] = vmachine.jump_to
    
    return vmachine["cycles"] - before_cycles
