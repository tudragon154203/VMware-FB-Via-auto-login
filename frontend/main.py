# main.py
import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    engine.load(QUrl.fromLocalFile('main.qml'))
    if not engine.rootContext():
        sys.exit(-1)

    try:
        sys.exit(app.exec_())
    except:
        pass
