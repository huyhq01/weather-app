const LABEL_UNITS = {
    "Nhiệt độ": "°C",
    "Độ ẩm": "%"
}
const weatherChart = new Chart(document.getElementById("weatherChart"), {
    data: {
        datasets: [
            {
                type: 'line',
                label: 'Nhiệt độ',
                borderColor: 'red',
                tension: 0.3,
                fill: false
            },
            {
                type: 'line',
                label: 'Độ ẩm',
                borderColor: 'DeepSkyBlue',
                tension: 0.3,
                fill: false
            }
        ]
    },
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        plugins: {
            tooltip: {
                callbacks: {
                    title: function (ctx) {
                        return ctx[0].label + " giờ";
                    },
                    label: function (ctx) {
                        return null;
                    },
                }
            }, title: {
                display: true,
                font: {
                    size: 20,
                    weight: 'bold'
                }
            }
        }
    }
});


export function updateChart(data) {
    weatherChart.data.labels = data.map(item => item.hour)
    weatherChart.data.datasets[0].data = data.map(item => item.temperature_2m)
    weatherChart.data.datasets[1].data = data.map(item => item.relative_humidity_2m)
    weatherChart.data.weatherDescription = data.map(item => item.description)
    weatherChart.data.precipitation_probability = data.map(item => item.precipitation_probability)
    weatherChart.data.wind_speed_10m = data.map(item => item.wind_speed_10m)
    weatherChart.options.plugins.tooltip.callbacks.footer = function (ctx) {
        let hour = ctx[0].dataIndex;
        let chartData = ctx[0].chart.data;

        let temp = chartData.datasets[0].data[hour];
        let humidity = chartData.datasets[1].data[hour];
        let desc = chartData.weatherDescription[hour];
        let precip = chartData.precipitation_probability[hour];
        let wind = chartData.wind_speed_10m[hour];

        return [
            `Nhiệt độ: ${temp} °C`,
            `Độ ẩm: ${humidity} %`,
            `Xác suất mưa: ${precip} %`,
            `Gió: ${wind} km/h`,
            desc
        ];
    }
    weatherChart.update()
}