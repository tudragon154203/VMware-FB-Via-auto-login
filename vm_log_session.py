from enum import Enum
from virtual_machine import VirtualMachine
import time

class VMLogSession:

    class Status(Enum):
        READY = "ready"
        RUNNING = "running"
        WAITING = "waiting"
        COMPLETED = "completed"
        ERROR = "error"

    """ a log in and out session of a VirtualMachine. Parameters:
    + virtual_machine: a VirtualMachine instance
    + t_running: time in seconds between start and stop a virtual machine. Should be enough for VM to boot and go into Facebook. Default to 180.
    + status: an enum of READY, RUNNING, WAITING, COMPLETED, ERROR, similar to the processes of tasks in an OS
    + created_at: time this session has been created
    + completed_at: : time this session has been completed"""
    def __init__(self, virtual_machine, t_running=180):
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
            self.status = self.Status.COMPLETED
            self.completed_at = time.time()
        except Exception as e:
            self.status = self.Status.ERROR
            raise e

    def _start_vm(self):
        self.status = self.Status.RUNNING
        # Code to start the virtual machine
        print(f'{self.virtual_machine.name} has been started')

    def _wait(self):
        self.status = self.Status.WAITING
        time.sleep(self.t_running)

    def _stop_vm(self):
        # Code to stop the virtual machine
        print(f'{self.virtual_machine.name} has been stopped')

if __name__ == "__main__":
    vm = VirtualMachine("ads 1", "/home/tudragon/SSD/VMware machines/2023.01.17_ads_001/2023.01.17_ads_001.vmx")
    print(vm.vmx_file_path)