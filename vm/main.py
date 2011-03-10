import sys
from read_memory import *
from virt_machine import *
from vm_errors import *
from device import *
from mix_machine import MixMachine


def main():
    if len(sys.argv) != 2:
        print ERR_INVALID_ARGS[1]
        return ERR_INVALID_ARGS[0]
    machine = MixMachine(sys.argv[1])
    machine.run()

if __name__ == '__main__':
    main()
