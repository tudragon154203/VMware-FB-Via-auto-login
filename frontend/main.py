# main.py
import sys
from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

engine.load(QUrl.fromLocalFile('main.qml'))

sys.exit(app.exec_())
