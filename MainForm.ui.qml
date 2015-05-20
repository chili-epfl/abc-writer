import QtQuick 2.3

Rectangle {
    id: rectangle1

    //width: parent.width
    //height: parent.height
    width: 1600
    height: width * 10/16
    color: "#000000"

    property alias nextButton: nextButton
    property alias clearButton: clearButton

    property alias sign:sign

    Image {
        id: background
        anchors.fill: parent
        source: "pics/background.jpg"

        Sign {
            id: sign
            width: parent.width * 0.6
            height: width * 365/315
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter

            lineWidth: width * 0.05


        }
    }

    Rectangle {
        id: clear
        width: 100
        height: 100
        color: "#1f306e"
        border.color: "#800b276f"
        radius: 50
        border.width: 5
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.topMargin: 50
        anchors.rightMargin: 50
        opacity: 1

        MouseArea {
            id: clearButton
            anchors.fill: parent
            opacity: 0
        }
    }

    Rectangle {
        id: next
        width: 100
        height: 100
        color: "#fa6f0a"
        radius: 50
        border.width: 5
        border.color: "#80fa2005"
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.topMargin: -114
        anchors.bottomMargin: 50
        anchors.leftMargin: -124
        anchors.rightMargin: 50
        opacity: 1
        visible: nextButton.visible

        MouseArea {
            id: nextButton
            anchors.fill: parent
            opacity: 0
        }
    }
    states: [
        State {
            name: "num5-outset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/5-outset.svg"
                particlesColor: sign.onSign ? "green" : "red"
                preventWritingOutsideArea: true
                signArea: [Qt.point(0.6916010498687664,0.2446351931330472),Qt.point(0.6640419947506562,0.2145922746781116),Qt.point(0.3123359580052493,0.21351931330472104),Qt.point(0.2847769028871391,0.2349785407725322),Qt.point(0.2979002624671916,0.3605150214592275),Qt.point(0.28608923884514437,0.4957081545064378),Qt.point(0.31758530183727035,0.5182403433476395),Qt.point(0.38188976377952755,0.4871244635193133),Qt.point(0.5170603674540682,0.4688841201716738),Qt.point(0.6286089238845144,0.5150214592274678),Qt.point(0.6614173228346457,0.6115879828326181),Qt.point(0.6062992125984252,0.6856223175965666),Qt.point(0.5183727034120735,0.721030042918455),Qt.point(0.4146981627296588,0.7060085836909872),Qt.point(0.3569553805774278,0.6566523605150214),Qt.point(0.3359580052493438,0.5901287553648069),Qt.point(0.2874015748031496,0.5686695278969958),Qt.point(0.2572178477690289,0.6051502145922747),Qt.point(0.28346456692913385,0.6824034334763949),Qt.point(0.37270341207349084,0.759656652360515),Qt.point(0.48556430446194226,0.7864806866952789),Qt.point(0.5984251968503937,0.7650214592274678),Qt.point(0.699475065616798,0.6952789699570815),Qt.point(0.7388451443569554,0.592274678111588),Qt.point(0.7139107611548556,0.5),Qt.point(0.6233595800524935,0.43240343347639487),Qt.point(0.5196850393700787,0.40450643776824036),Qt.point(0.4343832020997375,0.40879828326180256),Qt.point(0.3700787401574803,0.4216738197424893),Qt.point(0.36351706036745407,0.2832618025751073),Qt.point(0.6640419947506562,0.2757510729613734)]
            }
        },
        State {
            name: "num5-nooutset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/5-nooutset.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }
        },
        State {
            name: "num5-wire"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/5-wire.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }

        },
        State {
            name: "num8-outset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/8-outset.svg"
                particlesColor: sign.onSign ? "green" : "red"
                preventWritingOutsideArea: true
                signArea: [Qt.point(0.594488188976378,0.47532188841201717),Qt.point(0.6824146981627297,0.398068669527897),Qt.point(0.6732283464566929,0.315450643776824),Qt.point(0.6128608923884514,0.25),Qt.point(0.505249343832021,0.21888412017167383),Qt.point(0.3648293963254593,0.24892703862660945),Qt.point(0.3031496062992126,0.33047210300429186),Qt.point(0.32020997375328086,0.41952789699570814),Qt.point(0.38320209973753283,0.47854077253218885),Qt.point(0.2979002624671916,0.5450643776824035),Qt.point(0.27034120734908135,0.6373390557939914),Qt.point(0.3228346456692913,0.721030042918455),Qt.point(0.4251968503937008,0.7682403433476395),Qt.point(0.5616797900262467,0.76931330472103),Qt.point(0.6640419947506562,0.7221030042918455),Qt.point(0.7178477690288714,0.6351931330472103),Qt.point(0.6968503937007874,0.5418454935622318)]
            }
        },
        State {
            name: "num8-nooutset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/8-nooutset.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }
        },
        State {
            name: "num8-wire"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/8-wire.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }

        },
        State {
            name: "h-outset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/h-outset.svg"
                particlesColor: sign.onSign ? "green" : "red"
                preventWritingOutsideArea: true
                signArea: [Qt.point(0.421259842519685,0.7972103004291845),Qt.point(0.4238845144356955,0.7027896995708155),Qt.point(0.49081364829396323,0.6126609442060086),Qt.point(0.5275590551181102,0.628755364806867),Qt.point(0.5485564304461942,0.778969957081545),Qt.point(0.6023622047244095,0.8068669527896996),Qt.point(0.6811023622047244,0.7607296137339056),Qt.point(0.7230971128608924,0.6824034334763949),Qt.point(0.6916010498687664,0.6695278969957081),Qt.point(0.610236220472441,0.7628755364806867),Qt.point(0.5879265091863517,0.7542918454935622),Qt.point(0.5813648293963255,0.6158798283261803),Qt.point(0.5236220472440944,0.5708154506437768),Qt.point(0.589238845144357,0.40879828326180256),Qt.point(0.5813648293963255,0.30364806866952787),Qt.point(0.5236220472440944,0.2167381974248927),Qt.point(0.45931758530183725,0.2113733905579399),Qt.point(0.39763779527559057,0.286480686695279),Qt.point(0.3753280839895013,0.4270386266094421),Qt.point(0.37926509186351703,0.796137339055794)]
            }
        },
        State {
            name: "h-nooutset"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/h-nooutset.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }
        },
        State {
            name: "h-wire"
            PropertyChanges {
                target: sign
                source: "qrc:/pics/h-wire.svg"
                particlesColor: "yellow"
                preventWritingOutsideArea: false
            }

        }

    ]
}
