import sys
from read_memory import *
from virt_machine import *
from vm_errors import *
from device import *


class MixMachine:
    """
    MixMachine is an abstraction of the virt_machine, making it easyly usable
    in the Python's REPL like :

    >>> import mix_machine
    >>> m = mix_machine.MixMachine('/tmp/a.out')
    >>> m.debug()
    >>> m.step()
    enta : [+ 00 00 00 02 48]
    rA = [+ 00 00 00 00 00]
    >>> m.step()
    sta : [+ 00 00 00 05 24]
    memory[0] = + 00 00 00 00 00
    >>> print m.vmachine.cur_addr
    3002
    >>> m.vmachine.cur_addr = 3001
    >>> m.step()
    sta : [+ 00 00 00 05 24]
    memory[0] = + 00 00 00 00 00
    """

    printer_unit = 18
    terminal_unit = 19

    def __init__(self, filename):
        file_in = open(filename, "r")
        memory, start_address, errors = read_memory(file_in.readlines())
        if len(errors) > 0:
            self.print_errors(errors)
            raise Exception(ERR_SYNTAX[1])
        self.vmachine = VMachine(memory, start_address)
        self.out_file = open("printer.out", "w")
        self.in_file = open("terminal.in", "r")
        self.vmachine.set_device(self.printer_unit,
                                 FileDevice(mode="w", block_size=24 * 5,
                                            lock_time=24 * 2,
                                            file_object=self.out_file))
        self.vmachine.set_device(self.terminal_unit,
                                 FileDevice(mode="r", block_size=14 * 5,
                                            lock_time=14 * 2,
                                            file_object=self.in_file))

    def debug(self):
        self.vmachine.set_cpu_hook(self.cpu_hook)
        self.vmachine.set_mem_hook(self.mem_hook)
        self.vmachine.set_lock_hook(self.lock_hook)
        self.vmachine.set_op_hook(self.op_hook)

    def cpu_hook(self, item, old, new):
        print "%s = [%s]" % (str(item), str(new))

    def mem_hook(self, item, old, new):
        print "memory[%s] = %s" % (str(item), str(new))

    def lock_hook(self, item, old, new):
        print "LOCK[%s] %s -> %s" % (str(item), str(old), str(new))

    def op_hook(self, op, word):
        print "%s : [%s]" % (op, str(word))

    def step(self):
        try:
            self.vmachine.step()
        except VMError, error:
            print ERR_VM_RUN[1]
            self.print_error(None, error)
        if self.vmachine.halted:
            self.out_file.close()
            self.in_file.close()

    def run(self):
        try:
            while not self.vmachine.halted:
                self.vmachine.step()
        except VMError, error:
            print ERR_VM_RUN[1]
            self.print_error(None, error)
            return ERR_VM_RUN[0]

    def print_error(self, line, error):
        print "%s: %s" % (line if line is not None else 'GLOBAL', error)

    def print_errors(self, errors):
        for error in errors:
            self.print_error(error[0], error[1])
