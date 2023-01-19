from enum import Enum
from virtual_machine import VirtualMachine
import time
import subprocess
import shlex

class VMLogSession:

    class Status(Enum):
        READY = "ready"
        RUNNING = "running"
        WAITING = "waiting"
        COMPLETED = "completed"
        ERROR = "error"

    """ a log in and out session of a VirtualMachine. Attributes:
    :param virtual_machine: a VirtualMachine instance
    :param t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook.
    Through experment, it takes 50s to complete, so set default = 60 for some room
    :attr status: an enum of READY, RUNNING, WAITING, COMPLETED, ERROR, similar to the processes of tasks in an OS
    :attr created_at: time this session has been created
    :attr completed_at: : time this session has been completed

    Method:
    + run(): 

    Private methods:
    + _start_vm(): start the virtual machine, using vmrun bash script
    + _wait(): wait for t_running seconds
    + _stop_vm(): stop the virtual machine, also use vmrun"""
    def __init__(self, virtual_machine, t_running=60):
        self.virtual_machine = virtual_machine
        self.t_running = t_running
        self.status = self.Status.READY
        self.created_at = time.time()
        self.completed_at = None

    def run(self):
        try:
            self._start_vm()
            self._wait()
            self._stop_vm()
            self.completed_at = time.time()
        except Exception as e:
            self.status = self.Status.ERROR
            raise e

    def _start_vm(self):
        # Code to start the virtual machine
        vmrun_start_command = "vmrun start " + shlex.quote(self.virtual_machine.vmx_file_path) + " nogui"
        print(vmrun_start_command)
        subprocess.run(vmrun_start_command, shell=True)

        self.status = self.Status.RUNNING
        print(f'{self.virtual_machine.name} has started at {time.asctime( time.localtime(time.time()) )}')
        

    def _wait(self):
        time.sleep(self.t_running)

    def _stop_vm(self):
        # Code to stop the virtual machine
        vmrun_stop_command = "vmrun stop " + shlex.quote(self.virtual_machine.vmx_file_path) + " nogui"
        print(vmrun_stop_command)
        subprocess.run(vmrun_stop_command, shell=True)

        self.status = self.Status.COMPLETED
        print(f'{self.virtual_machine.name} has stopped at {time.asctime( time.localtime(time.time()) )}')

    # Getters
    def get_status(self):
        return self.status

    def get_created_at(self):
        return self.created_at

    def get_completed_at(self):
        return self.completed_at

if __name__ == "__main__":
    vm = VirtualMachine("ads 1", "/home/tudragon/SSD/VMware machines/2023.01.17_ads_001/2023.01.17_ads_001.vmx")
    # print(vm.vmx_file_path)
    vm_log_session = VMLogSession(vm)
    vm_log_session.run()