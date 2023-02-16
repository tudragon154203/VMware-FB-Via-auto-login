import os
import time
from config import Config
from virtual_machine import VirtualMachine
from vm_log_session import VMLogSession
from logger import Logger 
import argparse

class VMApp:
    """
    Initialize VMApp class with vm_root_dir, keyword and t_between_sessions
    In self.config:
    :param vm_root_dir: root directory of all vmware instances
    :param keyword: search for 'keyword' in all VM's names and only run these VMs
    :param t_between_sessions: time in seconds between two machine sessions. default to 5s
    Should be greater thatn VMLogSession.t_running to avoid CPU overload

    :attr vm_log_sessions - list of log sessions
    :attr logger - log messages into "../log


    Method:
    + run(): _scan() to get list of .vmx files, then _create_sessions() to get list of VMLogSession. For each VMLogSession instance, call its run() method, wait for t_between_sessions seconds and call run() of the next one.
    + get_progress(): counts the number of VMLogSessions that have been completed

    Private methods:
    + _scan(): scan all .vmx file in vm_root_dir recursively, look for those containing self.keyword. Return list of absolute paths of .vmx files
    + _create_sessions(vmx_paths): from list of .vmx files, create VMLogSession instances and put them in a list. Return list of VMLogSession 
    """
    def __init__(self, config):
        self.vm_root_dir = config["vm_root_dir"]
        self.keyword = config["keyword"]
        self.t_between_sessions = config["t_between_sessions"]
        self.t_running = config["t_running"]
        self.vm_log_sessions = []
        self.logger = Logger.instance(__name__, config["log_path"])
        config.save_config(config.file_path)

    def run(self):
        """
        _scan() to get list of .vmx files, 
        then _create_sessions() to get list of VMLogSession. 
        For each VMLogSession instance, call its run() method, 
        wait for t_between_sessions seconds and call run() of the next one.
        """
        self.logger.log("New VMApp instance started")
        vmx_paths = self._scan()
        print("Found virtual machine paths:", vmx_paths)
        self.vm_log_sessions = self._create_sessions(vmx_paths)
        length = len(self.vm_log_sessions)

        for session in self.vm_log_sessions:
            session.run()
            time.sleep(self.t_between_sessions)
            self.logger.log(f"{self.get_progress()}/{length} sessions completed")

    # def _scan(self):
    #     """
    #     scan all .vmx file in vm_root_dir recursively, 
    #     look for those containing self.keyword. 
    #     Return list of absolute paths of .vmx files (unsorted)
    #     """
    #     vmx_paths = []
    #     for root, dirs, files in os.walk(self.vm_root_dir):
    #         for file in files:
    #             if file.endswith(".vmx"):
    #                 path = os.path.join(root, file)
    #                 with open(path, "r") as f:
    #                     for line in f:
    #                         if "displayName" in line and self.keyword in line:
    #                             vmx_paths.append(path)
    #     return vmx_paths
    
    def _scan(self):
        """
        scan all .vmx file in vm_root_dir recursively, 
        look for those containing self.keyword. 
        Return list of absolute paths of .vmx files (unsorted)
        """
        vmx_paths = []
        for p in self.vm_root_dir.rglob("*"):
            if p.is_file() and p.suffix == ".vmx" and self.keyword in str(p):
                vmx_paths.append(p)
        return vmx_paths

    def _create_sessions(self, vmx_paths):
        """
        from list of .vmx files, create VMLogSession instances and put them in a list. 
        Return list of VMLogSession (sorted a-z by path)
        """
        vm_log_sessions = []
        for path in sorted(vmx_paths):
            # vm_name = path.split("/")[-1]
            vm_name = path.stem
            vm = VirtualMachine(name=vm_name, vmx_file_path=path)
            log_session = VMLogSession(virtual_machine=vm, t_running = self.t_running)
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

# Parser: Have one argument: config path
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--config-path", help="configuration file path. Default to ./config.json",
                            default="config.json")
args = parser.parse_args()

if __name__ == "__main__":
    config_file_path = args.config_path
    config = Config(file_path=config_file_path)
    config.load_config(config_file_path)
    vm_app = VMApp(config)
    vm_app.run()