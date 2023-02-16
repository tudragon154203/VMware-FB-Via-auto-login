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
    days_between_snapshots = 3,
    snapshot_dir = "../snapshots",
    file_path = "config.json"):
        """
        Initialize Config class with default values for vm_root_dir, keyword, t_running, t_between_sessions and log_path
        """
        data = {
            "vm_root_dir": pathlib.Path(vm_root_dir),
            "keyword": keyword,
            "t_running": t_running,
            "t_between_sessions": t_between_sessions,
            "log_path": pathlib.Path(log_path),
            "days_between_snapshots": days_between_snapshots,
            "snapshot_dir": pathlib.Path(snapshot_dir)
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
        data["vm_root_dir"] = str(self.data["vm_root_dir"].as_posix())
        data["log_path"] = str(self.data["log_path"].as_posix())
        data["snapshot_dir"] = str(self.data["snapshot_dir"].as_posix())

        with open(file_path, "w") as f:
            json.dump(data, f)
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
                self.data["vm_root_dir"] = pathlib.Path(config_data["vm_root_dir"])
                self.data["log_path"] = pathlib.Path(config_data["log_path"])
                self.data["snapshot_dir"] = pathlib.Path(config_data["snapshot_dir"])

                print(f'Config loaded: {config_data}')
        except: #No file_path
            print("No config, using default value")
            return

if __name__ == "__main__":
    config = Config()
    config.load_config(file_path = "config.json")
    config.save_config(file_path = "config.json")
