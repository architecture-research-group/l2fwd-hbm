#!/bin/bash

# sudo /home/j152s822/Documents/pcm/build/bin/pcm-memory 1 -nc -csv=pkt-burst2048.csv -- \
sudo ./build/examples/dpdk-l2fwd -l 0-3 -n 4 -- -q 1 -p 1 –P