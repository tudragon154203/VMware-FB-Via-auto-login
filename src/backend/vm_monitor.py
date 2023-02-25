import subprocess
import time
from backend.virtual_machine import VirtualMachine


class VMMonitor:
    """Helper functions to monitor VMs"""

    @staticmethod
    def _get_running_vmx_paths():
        """
        Get the paths of running .vmx files using the "vmrun list" command in a subprocess
        :return: list of paths of running .vmx files
        """
        vmrun_list = subprocess.run(["vmrun", "list"], stdout=subprocess.PIPE, universal_newlines=True)
        vmx_paths = [path for path in vmrun_list.stdout.split("\n") if path.endswith(".vmx")]
        return vmx_paths

    @staticmethod
    def is_running(virtual_machine):
        """
        Check if the given VirtualMachine instance is running.
        Sleep 1: delay the execuion for vmrun commands to take effect
        :param virtual_machine: VirtualMachine instance
        :return: True if the VirtualMachine is running, False otherwise
        """
        time.sleep(1)
        running_vmx_paths = VMMonitor._get_running_vmx_paths()
        # vmx_name = virtual_machine.vmx_file_path.split("/")[-1]
        vmx_name = virtual_machine.vmx_file_path.stem
        joined_path = " ".join(running_vmx_paths)
        return vmx_name in joined_path


if __name__ == "__main__":
    vm = VirtualMachine("ads 1", "/home/tudragon/SSD/VMware machines/2023.01.17_ads_001/2023.01.17_ads_001.vmx")
    is_running = VMMonitor.is_running(vm)
    print(is_running)
