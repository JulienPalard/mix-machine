# ld* (c_code = 8..23)

# ALL DONE

from word_parser import *


def _ld(reg, sign=1):
    def __ld(vmachine):
        vmachine["cycles"] += 2
        # src - can be cell with address [-1, 0, 0] =(2dec)= 0
        src = vmachine[WordParser.get_full_addr(vmachine, check_mix_addr=True)]
        # dst - rREG
        left, right = WordParser.get_field_spec(vmachine)
        # result will be loaded to reg
        result = src[max(1, left):right]
        result[0] = sign * (src[0] if left == 0 else +1)
        word = vmachine.registers[reg]
        word.set(result)
        if isinstance(reg, int) and word[1:3] != Word():
            word[1:3] = 0
    return __ld

lda = _ld("A")
ld1 = _ld(1)
ld2 = _ld(2)
ld3 = _ld(3)
ld4 = _ld(4)
ld5 = _ld(5)
ld6 = _ld(6)
ldx = _ld("X")

ldan = _ld("A", -1)
ld1n = _ld(1, -1)
ld2n = _ld(2, -1)
ld3n = _ld(3, -1)
ld4n = _ld(4, -1)
ld5n = _ld(5, -1)
ld6n = _ld(6, -1)
ldxn = _ld("X", -1)
