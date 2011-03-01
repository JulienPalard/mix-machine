#!/bin/sh
if [ -z "$1" ]
then
    echo 'Usage: ' $0 'source.mixal'
    exit 1
fi
python ../assembler/main.py "$1" "/tmp/$1.p" > /dev/null && \
python ../vm/main.py "/tmp/$1.p" && \
cat printer.out
