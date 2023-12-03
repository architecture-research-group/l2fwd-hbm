#!/bin/bash
sudo pqos -R
sudo pqos -e "llc:0=0x0001"
sudo pqos -a "llc:0=0-10"
gcc -O0 antagonist.c -o antagonist

PCM=/home/j152s822/Documents/pcm/build/bin/pcm-memory

sudo $PCM 1 -nc -csv=pcm.csv --
    ./antagonist