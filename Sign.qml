import QtQuick 2.0

import QtQuick.Particles 2.0

Item {
    id: sign

    width: 315
    height: 365
    property var signArea: []
    property var strokes: []
    property var currentStroke: []
    property int lineWidth: 5

    property url source:  ""


    Behavior on source {
        NumberAnimation {
            target: sign
            property: "opacity"
            duration: 1000
            from:0
            to:1
            easing.type: Easing.InOutQuad
        }
    }

    onSourceChanged: {
        reset();
    }

    property alias canvas: canvas

    property bool withParticles: true
    property color particlesColor: onSign ? "green" : "red"
    property bool preventWritingOutsideArea: true

    property bool onSign: false

    onOnSignChanged: {
        if (!onSign) {
            console.log("Touch outside the sign area");
        }
    }

    function reset() {

        strokes = [];
        canvas.requestPaint();
    }


    function isOnSign(pt){
        var x = pt.x/width;
        var y = pt.y/height;

        // Implementation by Jonas Raoni Soares Silva
        //@ http://jsfromhell.com/math/is-point-in-poly [rev. #0]
        for(var c = false, i = -1, l = signArea.length, j = l - 1; ++i < l; j = i)
            ((signArea[i].y <= y && y < signArea[j].y) || (signArea[j].y <= y && y < signArea[i].y))
                    && (x < (signArea[j].x - signArea[i].x) * (y - signArea[i].y) / (signArea[j].y - signArea[i].y) + signArea[i].x)
                    && (c = !c);
        return c;
    }

    Image {
        id: signImage
        anchors.fill: parent
        source: parent.source
        opacity: 0.8
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        //hoverEnabled: true
        onPositionChanged: {
            currentStroke.push(Qt.point(mouse.x,mouse.y));
            canvas.requestPaint();

            onSign = isOnSign(Qt.point(mouse.x,mouse.y));
        }

        onReleased: {

            if (currentStroke.length == 0) return;

            // Add the stroke to the log
            // (hand-made serialization because JSON.stringify does not know about Qt.point)
            var res = "[";
            for (var i=0; i < currentStroke.length; i++) {
                res += "(" + (currentStroke[i].x/sign.width).toFixed(2) + "," + (currentStroke[i].y/sign.height).toFixed(2) + "),";
            }
            res = res.slice(0, res.length-1);
            res += "]"

            console.log(res)



            strokes.push(currentStroke);
            currentStroke = [];


        }
    }

       Canvas {
        id: canvas
        antialiasing: true
        opacity: 1
        property real alpha: 0.8

        property bool showArea: false

        property color currentPathColor: "#001122"

        anchors.fill: parent

        onPaint: {
            var i = 0;
            var j = 0;
            var ctx = canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.globalAlpha = canvas.alpha;

            if (showArea) {
                ctx.lineWidth = 3;

                ctx.beginPath();
                ctx.strokeStyle = "#00BBCC";

                for (j = 0; j < sign.signArea.length; j++)
                {
                    ctx.lineTo(sign.signArea[j].x * sign.width, sign.signArea[j].y * sign.height);
                }
                ctx.stroke();

            }


            ctx.lineWidth = sign.lineWidth;
            ctx.lineJoin = "round"
            ctx.lineCap="round";

            ctx.beginPath();
            ctx.strokeStyle = canvas.currentPathColor;

            for (j = 0; j < sign.currentStroke.length; j++)
            {
                var point = sign.currentStroke[j];

                if(!sign.preventWritingOutsideArea || isOnSign(point)) {
                    ctx.lineTo(sign.currentStroke[j].x, sign.currentStroke[j].y);

                }
                else {
                    ctx.stroke();
                    ctx.beginPath();
                }
            }
            ctx.stroke();

            for (i = 0; i < sign.strokes.length; i++) {
                ctx.beginPath();
                for (j = 0; j < sign.strokes[i].length; j++)
                {
                    var point = sign.strokes[i][j];

                    if(!sign.preventWritingOutsideArea || isOnSign(point)) {
                        ctx.lineTo(sign.strokes[i][j].x, sign.strokes[i][j].y);

                    }
                    else {
                        ctx.stroke();
                        ctx.beginPath();
                    }
                }
                ctx.stroke();
            }
        }

    }


    ParticleSystem { id: sys1 }
    ImageParticle {
        system: sys1
        source: "qrc:/pics/particleA.png"
        color: particlesColor
        alpha: 0
        /*
        SequentialAnimation on color {
            loops: Animation.Infinite
            ColorAnimation {
                from: "cyan"
                to: "magenta"
                duration: 1000
            }
            ColorAnimation {
                from: "magenta"
                to: "blue"
                duration: 2000
            }
            ColorAnimation {
                from: "blue"
                to: "violet"
                duration: 2000
            }
            ColorAnimation {
                from: "violet"
                to: "cyan"
                duration: 2000
            }
        }
        */
        colorVariation: 0.3
    }
    //! [0]
    Emitter {
        id: trailsNormal
        system: sys1

        emitRate: 10
        lifeSpan: 2000

        enabled: sign.withParticles && mouseArea.pressed
        y: mouseArea.pressed ? mouseArea.mouseY : 0
        x: mouseArea.pressed ? mouseArea.mouseX : 0

        velocity: PointDirection {xVariation: 4; yVariation: 4;}
        acceleration: PointDirection {xVariation: 10; yVariation: 10;}
        //velocityFromMovement: 8

        size: sign.lineWidth * 1.3
        sizeVariation: size/2
    }

}

