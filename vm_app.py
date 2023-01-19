import os
import time
from virtual_machine import VirtualMachine
from vm_log_session import VMLogSession

class VMApp:
    """
    Initialize VMApp class with vm_root_dir, keyword and t_between_sessions
    :param vm_root_dir: root directory of all vmware instances
    :param keyword: search for 'keyword' in all VM's names and only run these VMs
    :param t_between_sessions: time in seconds between two machine sessions. default to 90s 
    Should be greater thatn VMLogSession.t_running to avoid CPU overload

    :attr vm_log_sessions - list of log sessions


    Method:
    + run(): _scan() to get list of .vmx files, then _create_sessions() to get list of VMLogSession. For each VMLogSession instance, call its run() method, wait for t_between_sessions seconds and call run() of the next one.
    + get_progress(): counts the number of VMLogSessions that have been completed

    Private methods:
    + _scan(): scan all .vmx file in vm_root_dir recursively, look for those containing self.keyword. Return list of absolute paths of .vmx files
    + _create_sessions(vmx_paths): from list of .vmx files, create VMLogSession instances and put them in a list. Return list of VMLogSession 
    """
    def __init__(self, vm_root_dir, keyword = "ads", t_between_sessions=90):
        self.vm_root_dir = vm_root_dir
        self.keyword = keyword
        self.t_between_sessions = t_between_sessions
        self.vm_log_sessions = []

    def run(self):
        """
        _scan() to get list of .vmx files, 
        then _create_sessions() to get list of VMLogSession. 
        For each VMLogSession instance, call its run() method, 
        wait for t_between_sessions seconds and call run() of the next one.
        """
        vmx_paths = self._scan()
        self.vm_log_sessions = self._create_sessions(vmx_paths)
        length = len(self.vm_log_sessions)

        for session in self.vm_log_sessions:
            session.run()
            time.sleep(self.t_between_sessions)
            print(f"{self.get_progress()}/{length} sessions completed")

    def _scan(self):
        """
        scan all .vmx file in vm_root_dir recursively, 
        look for those containing self.keyword. 
        Return list of absolute paths of .vmx files
        """
        vmx_paths = []
        for root, dirs, files in os.walk(self.vm_root_dir):
            for file in files:
                if file.endswith(".vmx"):
                    path = os.path.join(root, file)
                    with open(path, "r") as f:
                        for line in f:
                            if "displayName" in line and self.keyword in line:
                                vmx_paths.append(path)
        return vmx_paths

    def _create_sessions(self, vmx_paths):
        """
        from list of .vmx files, create VMLogSession instances and put them in a list. 
        Return list of VMLogSession
        """
        vm_log_sessions = []
        for path in vmx_paths:
            vm_name = path.split("/")[-1]
            vm = VirtualMachine(name=vm_name, vmx_file_path=path)
            log_session = VMLogSession(virtual_machine=vm)
            vm_log_sessions.append(log_session)
        return vm_log_sessions

    def get_progress(self):
        """
        Counts the number of VMLogSessions that have been completed
        :return: number of completed sessions
        """
        completed_sessions = 0
        for session in self.vm_log_sessions:
            if session.status == VMLogSession.Status.COMPLETED:
                completed_sessions += 1
        return completed_sessions

if __name__ == "__main__":
    vm_app = VMApp("..")
    vm_app.run()