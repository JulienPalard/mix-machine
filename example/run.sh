#!/bin/sh
if [ -z "$1" ]
then
    echo 'Usage: ' $0 'source.mixal'
    exit 1
fi
>printer.out
>a.out
python ../assembler/main.py "$1" "a.out"
if [ ! -s a.out ]
then
    echo 'No assembly generated, exiting'
    exit 1
fi
echo "Compilation completed, running :"
python ../vm/main.py "a.out"
cat printer.out
