# backend.py
from PySide6.QtCore import QObject, Signal, Slot

class Backend(QObject):
    configFileChanged = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._config_file = ''

    @property
    def config_file(self):
        return self._config_file

    @config_file.setter
    def config_file(self, config_file):
        self._config_file = config_file
        self.configFileChanged.emit(self._config_file)

    @Slot()
    def run_program(self):
        print("Running program with config file:", self._config_file)
