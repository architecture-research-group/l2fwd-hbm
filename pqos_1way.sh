#!/bin/bash
sudo pqos -R
sudo pqos -e "llc:0=0x0001"
sudo pqos -a "llc:0=0-10"