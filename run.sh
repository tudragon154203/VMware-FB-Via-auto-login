#!/usr/bin/env bash
# Add this into crontab -e
cd ~/SSD/VMware\ machines/src 
vmware -n &
python3 vm_app.py 
#echo $PATH > log_path.txt


