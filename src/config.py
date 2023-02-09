import json
from collections import UserDict

class Config(UserDict):
    """ A dictionary used for configuration
    Has save_config and load_config method
    """
    def __init__(self, vm_root_dir="..", keyword="ads", 
    t_running=60, t_between_sessions=5, 
    log_path="../log.txt", file_path = "config.json"):
        """
        Initialize Config class with default values for vm_root_dir, keyword, t_running, t_between_sessions and log_path
        Also record file_path of the json file
        """
        data = {
            "vm_root_dir": vm_root_dir,
            "keyword": keyword,
            "t_running": t_running,
            "t_between_sessions": t_between_sessions,
            "log_path": log_path
        }
        self.file_path = file_path
        super().__init__(data)

    def save_config(self, file_path=""):
        """
        Save the configuration data to a json file
        :param file_path: file path to save the json data. Default to self.file_path
        """
        if not file_path:
            file_path = self.file_path
            print(f"Save config: Empty file path, using self.file_path: {self.file_path}")

        with open(file_path, "w") as f:
            json.dump(self.data, f)
            print(f'Config saved to {file_path}')

    
    def load_config(self, file_path = None):
        """
        Load the configuration data from a json file
        :param file_path: file path to load the json data
        """
        try:
            with open(file_path, "r") as f:
                config_data = json.load(f)
                self.data = config_data
                print(f'Config loaded: {config_data}')
        except: #No file_path
            print("No config, using default value")
            return

if __name__ == "__main__":
    config = Config()
    config.save_config("config.json")
    config.load_config("config.json")