Program to open and close Virtual Machines (VMs)

Programming language: Python

Quickstart: python3 vm_app.py

Steps:

1. Scan all machines in folder .., create a list
   For each machine:
   2. Start virtual machine using "vmrun"
   3. Wait for t_running seconds
   4. close the virtual machine
   5. Wait for t_between_sessions seconds

Parameters:
t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook
t_between_sessions: time in seconds between two machine sessions

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
+ _take_screenshot(): take a screenshot of this VM

c> VMApp: scan the machines in hard disks for virtual machines (VMs), generate VirtualMachine and VMLogSessions
Attributes:

+ vm_root_dir: root directory of all vmware instances
+ keyword: search for 'keyword' in all VM's names and only run these VMs
+ t_between_sessions: time in seconds between two machine sessions
+ vm_log_session: list of VMLogSessions with found keywords

Method:

+ run(): _scan() to get list of .vmx files, then _create_sessions() to get list of VMLogSession. For each VMLogSession instance, call its run() method, wait for t_between_sessions seconds and call run() of the next one.
+ get_progress(): counts the number of VMLogSessions that have been completed

Private methods:

+ _scan(): scan all .vmx file in vm_root_dir recursively, look for those containing self.keyword. Return list of absolute paths of .vmx files
+ _create_sessions(vmx_paths): from list of .vmx files, create VMLogSession instances and put them in a list. Return list of VMLogSession

d> VMAppService: create VMApp instances in a predefined schedule
Deprecated, using cronjob of linux or windows Task Scheduler

e> VMMonitor: monitoring VMs. No attribute.
static method: get_running_vmx_paths(), return paths of running .vmx files using "vmrun list" command in a subprocesss
public method:

is_running(VirtualMachine): check if this virtual machine is running

f> Config: a python configuration class that uses json library
Data to save:

* "vm_root_dir": path of root folder of VMs
* "keyword": to seach for in '.vmx. files in vm_root_dir

+ t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook. Default to 60.
+ t_between_sessions: time in seconds between two machine sessions. Default to 5.
+ log_path: output logging path. Default to "../log.txt"
+ days_between_screenshots: time in days between two consecutive screenshots. Default to 3.
+ screenshot_dir: output screenshot path. Default to "../screenshots"
