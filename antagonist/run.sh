#!/bin/bash

gcc -O0 antagonist.c -o antagonist

PCM=/home/j152s822/Documents/pcm/build/bin/pcm-memory

# sudo $PCM 1 -nc -csv=pcm.csv -- \
./antagonist