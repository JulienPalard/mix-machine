from vm_errors import *
from word_parser import *
from word import *
from opcodes import opcodes
from registers import Registers

class VMachine:
    MEMORY_SIZE = 4000
    # constants for locking
    # this cells are locked for write but you can read them
    W_LOCKED = 0
    # this cells are locked for read and write
    RW_LOCKED = 1

    def __getitem__(self, x):
        """Can raise exception"""
        return self.memory[x]

    def __setitem__(self, item, value):
        """Can raise exception"""
        old_value = self[item]
        # we are working with memory
        self.memory[item] = value
        if self.mem_hook is not None \
                and old_value.word_list != self.memory[item].word_list:
            self.mem_hook(item, old_value, self.memory[item])

    @staticmethod
    def check_mem_addr(addr):
        return 0 <= addr < VMachine.MEMORY_SIZE

    def cmp_memory(self, memory_dict):
        """Need for testing"""
        positive_zero = [+1, 0, 0, 0, 0, 0]
        if not isinstance(memory_dict, dict) or \
                any((i in memory_dict \
                         and self[i].word_list != memory_dict[i].word_list) \
                        or (i not in memory_dict \
                                and self[i].word_list != positive_zero)
                    for i in xrange(VMachine.MEMORY_SIZE)):
                return False
        else:
            return True

    def get_cur_word(self):
        return self[self.cur_addr]

    def set_memory(self, memory, reset):
        if isinstance(memory, list):
            self.memory = [Word(x) for x in memory]
            return
        if reset:
            self.memory = [Word() for _ in xrange(self.MEMORY_SIZE)]
        for addr, word in memory.items():
            # checking for correct input done in read_memory
            self[addr] = word

    def init_stuff(self, start_address):
        self.rA, self.rX, self.rJ = [Word() for _ in xrange(3)]
        self.r = [Word() for _ in xrange(7)]
        self.cf = 0
        self.of = False
        self.cur_addr = start_address
        self.halted = False

    def set_device(self, number, device_instance):
        if 0 <= number < MAX_BYTE:
            self.devices[number] = device_instance
            return True
        else:
            return False

    def is_readable(self, addr):
        return addr not in self.locked_cells[self.RW_LOCKED]

    def is_writeable(self, addr):
        return addr not in (self.locked_cells[self.W_LOCKED] \
                                | self.locked_cells[self.RW_LOCKED])

    def is_readable_set(self, _set):
        return len(_set & self.locked_cells[self.RW_LOCKED]) == 0

    def is_writeable_set(self, _set):
        return len(_set & (self.locked_cells[self.W_LOCKED] \
                                | self.locked_cells[self.RW_LOCKED])) == 0

    def lock_cells(self, mode, add=None, sub=None):
        assert((add is not None) ^ (sub is not None))
        if self.lock_hook is not None:
            old = set(self.locked_cells[mode])
        if add is not None:
            # add set to self.locked_cells[mode]
            self.locked_cells[mode] |= add
        else:
            # subtract set from self.locked_cells[mode]
            self.locked_cells[mode] -= sub
        if self.lock_hook is not None and self.locked_cells[mode] != old:
            self.lock_hook("rw" if mode == self.RW_LOCKED \
                               else "w", old, self.locked_cells[mode])

    def __init__(self, memory, start_address):
        self.errors = []
        self.registers = Registers(None)
        self.set_cpu_hook(None)
        self.set_mem_hook(None)
        self.set_lock_hook(None)
        self.set_op_hook(None)
        self.set_memory(memory, reset=True)
        self.init_stuff(start_address)
        self.devices = {}
        self.locked_cells = [set(), set()]
        self.cycles = 0

    def execute(self):
        # some common stuff
        if not self.is_readable(self.cur_addr):
            raise MemReadLockedError((self.cur_addr, self.cur_addr))
        current_word = self.get_cur_word()
        c = current_word[5]
        f = current_word[4]
        op = opcodes.get(c, opcodes.get((c,f), None))
        self.jump_to = None
        before_cycles = self.cycles
        if self.op_hook is not None:
            self.op_hook(op.__name__, current_word)
        op(self)
        if self.jump_to is None:
            self.cur_addr += 1
        else:
            self.cur_addr = self.jump_to
        return self.cycles - before_cycles

    def step(self):
        if not self.check_mem_addr(self.cur_addr):
            raise InvalidCurAddrError(self.cur_addr)
        cycles = self.execute()

        # refresh all plugged devices
        for dev in self.devices.values():
            # if device isn't busy returns None
            unlock = dev.refresh(cycles)
            if unlock is not None:
                # else returned (mode, limits) - mode in 'rw', \
                # limits = (left, right) - properies of unlocked memory part
                if unlock[0] == 'w':
                    mode = self.W_LOCKED
                elif unlock[0] == 'rw':
                    mode = self.RW_LOCKED
                else:
                    return  # ioc busy
                # unlock memory
                self.lock_cells(mode, sub=set(range(unlock[1][0], \
                                                        unlock[1][1] + 1)))

    def set_cpu_hook(self, hook):
        self.cpu_hook = hook
        self.registers.cpu_hook = hook

    def set_op_hook(self, hook):
        self.op_hook = hook

    def memory_changed(self, addr):
        if self.mem_hook is not None:
            self.mem_hook(addr, None, self[addr])

    def set_mem_hook(self, hook):
        self.mem_hook = hook

    def set_lock_hook(self, hook):
        self.lock_hook = hook
