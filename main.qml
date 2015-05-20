import QtQuick 2.4
import QtQuick.Window 2.2

Window {
    visible: true
    visibility: "FullScreen"

    MainForm {
        focus: true
        anchors.fill: parent

        property int stateIdx: 0

        nextButton.onPressed: {
            stateIdx += 1;

            state = states[stateIdx].name;
            console.log("State: " + state)

            if (stateIdx == states.length - 1) {
                nextButton.visible=false;
            }
        }

        clearButton.onPressed: {
            console.log("Clearing");
            sign.reset();
        }

        Keys.onEscapePressed: {
            Qt.quit();
        }

        Component.onCompleted: {
            state = states[0].name;
            console.log("Starting now")
            console.log("State: " + state)
        }

    }
}
