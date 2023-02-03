// main.qml
import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("VMware Via Auto Log-in")

    Column {
        TextField {
            id: configFileField
            text: backend.config_file
            placeholderText: "Enter config file path"
        }
        Button {
            text: "Run Program"
            onClicked: backend.run_program()
        }
    }

    Component.onCompleted: {
        backend.configFileChanged.connect(configFileField, "setText")
    }
}
