// spiral-chart.js

var option2 = {
    polar: {},
    tooltip: {
        show: true,
        formatter: function (params) {
            var angle = params.value[0];
            var radius = params.value[1];
            var z = params.value[2];
            return 'Angle: ' + angle.toFixed(2) + '°<br>Radius: ' + radius.toFixed(2) + '<br>Z: ' + z.toFixed(2);
        }
    },
    angleAxis: {
        type: 'value',
        startAngle: 0,
        splitNumber: 12
    },
    radiusAxis: {},
    series: [{
        type: 'line',
        data: (function () {
            var data = [];
            for (var i = 0; i <= 360 * 5; i++) {
                var angle = i;
                var radius = angle / 360 * 5;
                var z = angle / 180 * Math.PI;
                data.push([angle, radius, z]);
            }
            return data;
        })(),
        coordinateSystem: 'polar',
        symbolSize: 4,
        lineStyle: {
            color: 'blue'
        },
        itemStyle: {
            color: 'red'
        }
    }]
};
