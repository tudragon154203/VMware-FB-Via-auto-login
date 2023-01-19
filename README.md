Program to open and close Virtual Machines (VMs)

Programming language: Python

Steps:
1. Scan all machines in folder .., create a list
For each machine:
    2. Start virtual machine using "vmrun"
    3. Wait for t_running seconds
    4. close the virtual machine
    5. Wait for t_between_vm seconds

Parameters:
t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook
t_between_vm: time in seconds between two machine runs

Objects/Classes:
a> VirtualMachine => children: ads, page, vm, reference
+ name
+ vmx_file_path

b> VMLogSession: a log in and out session of a VirtualMachine, belongs to a VirtualMachine. 
Parameters:
+ virtual_machine: a VirtualMachine instance
+ t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook. Default to 180.
+ status: an enum of READY, RUNNING, WAITING, COMPLETED, ERROR, similar to the processes of tasks in an OS
+ created_at: time this session has been created
+ completed_at: : time this session has been completed
method:
+ run(): 
private methods:
+ _start_vm(): start the virtual machine
+ _wait(): wait for t_running seconds
+ _stop_vm(): stop the virtual machine

c> VMApp: scan the machines in hard disks, generate VirtualMachine and VMLogSessions
d> VMAppService: create VMApp instances in a predefined schedule