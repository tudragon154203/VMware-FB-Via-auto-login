from enum import Enum
from virtual_machine import VirtualMachine
from vm_monitor import VMMonitor
import time
import subprocess
import pathlib
from logger import Logger 
from datetime import date 

class VMLogSession:

    class Status(Enum):
        READY = "ready"
        RUNNING = "running"
        WAITING = "waiting"
        COMPLETED = "completed"
        ERROR = "error"

    """ a log in and out session of a VirtualMachine. Attributes:
    :param virtual_machine: a VirtualMachine instance
    :param config: passed from app

    :attr status: an enum of READY, RUNNING, WAITING, COMPLETED, ERROR, similar to the processes of tasks in an OS
    :attr created_at: time this session has been created
    :attr completed_at: : time this session has been completed
    :attr logger: singleton instance of app's logger

    Method:
    + run(): start a virtual machine, wait for some time. Take a screenshot if ordered.

    Private methods:
    + _start_vm(): start the virtual machine, using vmrun bash script
    + _wait(): wait for t_running seconds
    + _stop_vm(): stop the virtual machine, also use vmrun"""
    def __init__(self, virtual_machine, config):
        self.virtual_machine = virtual_machine
        self.config = config

        # inner attr
        self.status = self.Status.READY
        self.created_at = time.time()
        self.completed_at = None
        self.logger = Logger.instance()

    def run(self):
        try:
            self._start_vm()
            self._wait()
            if self._is_today_screenshot_day():
                self._take_screenshot()             
            self._stop_vm()
            self.completed_at = time.time()
        except Exception as e:
            self.status = self.Status.ERROR
            raise e
        
    def _is_today_screenshot_day(self):
        """Decide whether or not to take screen shot. 
        Depend on config and today's date
        Return: bool"""
        if not self.config["monitor"]["screenshot"]["enable"]:
            return False
        else:
            today = date.today()
            anchor_date = date.min
            difference = (today - anchor_date).days
            # print(f"date difference: {difference}")
            if difference % self.config["monitor"]["screenshot"]["days_between_screenshots"] == 0:
                self.logger.log(f"Date check: Today's screenshot day! ({today})")
                return True
            else:
                self.logger.log(f"Date check: Today's NOT screenshot day! ({today})")
                return False

    def _start_vm(self):
        # Code to start the virtual machine
        # vmrun_start_command = "vmrun start " + shlex.quote(self.virtual_machine.vmx_file_path) 
        abs_path = self.get_vm_abs_path()
        vmrun_start_command = "vmrun start " +  '"' + abs_path +  '"'
        self.logger.log(vmrun_start_command)
        subprocess.run(vmrun_start_command, shell=True)

        if VMMonitor.is_running(self.virtual_machine):
            self.status = self.Status.RUNNING
            self.logger.log(f'{self.virtual_machine.get_name()} has started successfully')
        else:
            self.status = self.Status.ERROR
            self.logger.error(f'{self.virtual_machine.get_name()} has failed to start')
        

    def _wait(self):
        time.sleep(self.config["runtime"]["t_running"])

    def _stop_vm(self):
        # Code to stop the virtual machine
        # vmrun_stop_command = "vmrun stop " + shlex.quote(self.virtual_machine.vmx_file_path) 
        abs_path = self.get_vm_abs_path()
        vmrun_stop_command = "vmrun stop " +  '"' + abs_path +  '"'
        self.logger.log(vmrun_stop_command)
        subprocess.run(vmrun_stop_command, shell=True)

        if not VMMonitor.is_running(self.virtual_machine):
            self.status = self.Status.COMPLETED
            self.logger.log(f'{self.virtual_machine.get_name()} has stopped successfully')
        else:
            self.status = self.Status.ERROR
            self.logger.error(f'{self.virtual_machine.get_name()} has failed to stop')

    def _take_screenshot(self):
        # print("Taking screenshot...")
        abs_path = self.get_vm_abs_path()
        username = self.config["monitor"]["guest_credentials"]["username"]
        password = self.config["monitor"]["guest_credentials"]["password"]
        output_img_path = pathlib.Path(self.config["monitor"]["screenshot"]["screenshot_dir"]) / self.virtual_machine.get_name()
        output_img_path = str(output_img_path) + ".jpg"

        vmrun_capturescreen_command = f"vmrun -T ws -gu '{username}' -gp '{password}' captureScreen '{abs_path}' '{output_img_path}'"

        # print("output_img_path", output_img_path)
        # print("vmrun_capturescreen_command", vmrun_capturescreen_command)
        
        self.logger.log(f"Taking screenshot into {output_img_path}, using log-in credentials {username} - {password}")
        # self.logger.log(vmrun_capturescreen_command)
        subprocess.run(vmrun_capturescreen_command, shell=True)

    # Getters
    def get_status(self):
        return self.status

    def get_created_at(self):
        return self.created_at

    def get_completed_at(self):
        return self.completed_at

    def get_vm_abs_path(self):
        return str(self.virtual_machine.vmx_file_path.resolve())

if __name__ == "__main__":
    vm = VirtualMachine("ads 1", "/home/tudragon/SSD/VMware machines/2023.01.17_ads_001/2023.01.17_ads_001.vmx")
    # self.logger.log(vm.vmx_file_path)
    vm_log_session = VMLogSession(vm)
    vm_log_session.run()