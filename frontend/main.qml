// main.qml
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("VMware Via Auto Log-in")
    Material.theme: Material.Dark

    Column {
        TextField {
            id: configFileField
            text: backend.config_file
            height: 30
            placeholderText: "Enter config file path"
        }
        Button {
            width: 200
            height: 50
            text: "Run"
            background: Rectangle{
                color: "green"
            }
            onClicked: backend.run_program()

        }
    }

    Component.onCompleted: {
        backend.configFileChanged.connect(configFileField, "setText")
    }
}
