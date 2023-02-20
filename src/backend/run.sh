#!/usr/bin/env bash
export DISPLAY=":0.0"

cd ~/SSD/VMware\ machines/VMware\ FB\ Via\ auto\ login/src/backend
vmware &
python3 main.py 