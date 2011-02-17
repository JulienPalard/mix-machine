#!/bin/sh
python ../assembler/main.py "$1" "/tmp/$1.p" > /dev/null
python ../vm/main.py "/tmp/$1.p"
cat printer.out
