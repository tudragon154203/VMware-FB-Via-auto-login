#!/usr/bin/env bash
#export PATH=/home/tudragon/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
export DISPLAY=":0.0"

cd ~/SSD/VMware\ machines/VMware\ FB\ Via\ auto\ login/src/backend
vmware &
python3 main.py 

