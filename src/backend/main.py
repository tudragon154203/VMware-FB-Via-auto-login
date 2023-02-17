from vm_app import VMApp
from config import Config
import argparse
from logger import Logger 

# Parser: Have one argument: config path
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--config-path", help="configuration file path. Default to ./config.json",
                            default="config.json")
args = parser.parse_args()

if __name__ == "__main__":
    config_file_path = args.config_path
    config = Config(file_path=config_file_path)
    config.load_config(config_file_path)
    config.save_config(config_file_path)
    logger = Logger.instance(__name__, config["monitor"]["log_path"])

    vm_app = VMApp(config, logger)
    vm_app.run()