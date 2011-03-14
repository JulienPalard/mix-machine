# st* (c_code = 24..33)
# ALL DONE

from word_parser import *


def _st(vmachine, reg):
    vmachine.cycles += 2
    src = Word() if reg == "Z" else vmachine.registers[reg]
    # dst - vmachine[addr]
    addr = WordParser.get_full_addr(vmachine, check_mix_addr=True)
    if not vmachine.is_writeable(addr):
        raise MemReadLockedError((addr, addr))
    left, right = WordParser.get_field_spec(vmachine)
    vmachine[addr][max(1, left):right] = src[1:5]
    if left == 0:
        vmachine[addr][0:0] = src[0]
    vmachine.memory_changed(addr)


def sta(vmachine):
    _st(vmachine, "A")


def st1(vmachine):
    _st(vmachine, 1)

def st2(vmachine):
    _st(vmachine, 2)


def st3(vmachine):
    _st(vmachine, 3)


def st4(vmachine):
    _st(vmachine, 4)


def st5(vmachine):
    _st(vmachine, 5)


def st6(vmachine):
    _st(vmachine, 6)


def stx(vmachine):
    _st(vmachine, "X")


def stj(vmachine):
    _st(vmachine, "J")


def stz(vmachine):
    _st(vmachine, "Z")
