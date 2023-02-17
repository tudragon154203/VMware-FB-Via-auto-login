import json
from collections import UserDict
import pathlib

class Config(UserDict):
    """ A dictionary used for configuration
    Has save_config and load_config method
    """
    def __init__(self, vm_root_dir="..", keyword="ads", 
    t_running=60, t_between_sessions=5, 
    log_path="../log.txt", 
    days_between_screenshots = 3,
    screenshot_enable = True,
    screenshot_dir = "../screenshots",
    file_path = "config.json"):
        """
        Initialize Config class with default values:
        :param vm_root_dir: root directory of all vmware instances
        :param keyword: search for 'keyword' in all VM's names and only run these VMs
        :param t_between_sessions: time in seconds between two machine sessions. default to 5s
        :param screenshot_enable: do you enable taking screenshot. Default to True
        :param days_between_screenshots: time in seconds between two machine sessions. default to 5s
        :param screenshot_dir: output screenshot path. Default to "../screenshots"
        """
        data = {
            "vm_filter":{
                "vm_root_dir": pathlib.Path(vm_root_dir),
                "keyword": keyword
            },
            "runtime":{
                "t_running": t_running,
                "t_between_sessions": t_between_sessions
            },
            "monitor":{
                "log_path": pathlib.Path(log_path),
                "screenshot":{
                    "enable": screenshot_enable,
                    "days_between_screenshots": days_between_screenshots,
                    "screenshot_dir": pathlib.Path(screenshot_dir)      
                }
            }
        }
        self.file_path = pathlib.Path(file_path)
        super().__init__(data)

    def save_config(self, file_path=""):
        """
        Save the configuration data to a json file
        :param file_path: file path to save the json data. Default to self.file_path
        """
        if not file_path:
            file_path = self.file_path
            print(f"Save config: Empty file path, using self.file_path: {self.file_path}")
        else:
            file_path = pathlib.Path(file_path)

        data = self.data
        data["vm_filter"]["vm_root_dir"] = str(self.data["vm_filter"]["vm_root_dir"].as_posix())
        data["monitor"]["log_path"] = str(self.data["monitor"]["log_path"].as_posix())
        data["monitor"]["screenshot"]["screenshot_dir"] = str(self.data["monitor"]["screenshot"]["screenshot_dir"].as_posix())

        with open(file_path, "w") as f:
            json.dump(data, f,
                     sort_keys=False, indent=4)
            print(f'Config saved to {file_path}')

    
    def load_config(self, file_path = None):
        """
        Load the configuration data from a json file
        :param file_path: file path to load the json data
        """
        file_path = pathlib.Path(file_path) 
        try:
            with open(file_path, "r") as f:
                config_data = json.load(f)
                self.data = config_data

                # parse paths using pathlib
                self.data["vm_filter"]["vm_root_dir"] = pathlib.Path(config_data["vm_filter"]["vm_root_dir"])
                self.data["monitor"]["log_path"] = pathlib.Path(config_data["monitor"]["log_path"])
                self.data["monitor"]["screenshot"]["screenshot_dir"] = pathlib.Path(config_data["monitor"]["screenshot"]["screenshot_dir"])

                print(f'Config loaded: {config_data}')
        except: #No file_path
            print("No config, using default value")
            return

if __name__ == "__main__":
    config = Config()
    # config_file_path = "config.json"
    config_file_path = "src/backend/config.json"
    config.load_config(file_path = config_file_path)
    config.save_config(file_path = config_file_path)
