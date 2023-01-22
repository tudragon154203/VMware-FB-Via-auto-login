import json

class Config:
    def __init__(self, vm_root_dir="..", keyword="ads", 
    t_running=60, t_between_sessions=5, 
    log_path="../log.txt"):
        """
        Initialize Config class with default values for vm_root_dir, keyword, t_running, t_between_sessions and log_path
        """
        self.vm_root_dir = vm_root_dir
        self.keyword = keyword
        self.t_running = t_running
        self.t_between_sessions = t_between_sessions
        self.log_path = log_path

    def save_config(self, file_path):
        """
        Save the configuration data to a json file
        :param file_path: file path to save the json data
        """
        config_data = {
            "vm_root_dir": self.vm_root_dir,
            "keyword": self.keyword,
            "t_running": self.t_running,
            "t_between_sessions": self.t_between_sessions,
            "log_path": self.log_path
        }
        with open(file_path, "w") as f:
            json.dump(config_data, f)

    
    def load_config(self, file_path):
        """
        Load the configuration data from a json file
        :param file_path: file path to load the json data
        """
        with open(file_path, "r") as f:
            config_data = json.load(f)
            self.vm_root_dir = config_data["vm_root_dir"]
            self.keyword = config_data["keyword"]
            self.t_running = config_data["t_running"]
            self.t_between_sessions = config_data["t_between_sessions"]
            self.log_path = config_data["log_path"]

if __name__ == "__main__":
    config = Config()
    config.save_config("config.json")
    config.load_config("config.json")