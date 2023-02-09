#!/usr/bin/env bash
export DISPLAY=":0.0"

cd ~/SSD/VMware\ machines/VMware\ FB\ Via\ auto\ login/src 
vmware &
python3 vm_app.py --path config.json