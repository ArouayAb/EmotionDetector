export function drawChart(inference) {
    const data = {
        labels: [
            "Anger",
            "Contempt",
            "Disgust",
            "Fear",
            "Happy",
            "Neutral",
            "Sadness",
            "Surprise"
        ],
        datasets: [
            {
                label: 'Emotion Dataset',
                data: [10, 50, 300, 123, 634, 34, 1, 534],
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(230, 91, 232)',
                    'rgb(130, 6, 132)',
                    'rgb(255, 200, 132)',
                    'rgb(255, 92, 23)',
                    'rgb(255, 76, 150)',
                    'rgb(123, 99, 132)',
                    'rgb(9, 90, 240)'
                ],
                hoverOffset: 4
            }
        ]
    }

    const config = {
        type: 'doughnut',
        data: data
    };

    const options = {
        cutout: 90,
        responsive: true,
        maintainAspectRatio: true,
        yAxes: [{
            ticks: {
                beginAtZero: true
            }
        }]
    }

    let canvas = $("#chart-container-id").find("canvas");
    if(!canvas.length) {
        canvas = document.createElement("canvas");
    } else {
        canvas = canvas.get(0);
        let chart = Chart.getChart(canvas);
        chart.destroy();
    }

    const doughnutChart = new Chart(
        canvas,
        config,
        options
    );
    $("#chart-container-id").append(canvas);
}

// $("#buttonId").on("click", function () {
//     let canvas = $(this).parent().find("canvas");
//     if(!canvas.length) {
//         canvas = document.createElement("canvas");
//     } else {
//         canvas = canvas.get(0);
//         let chart = Chart.getChart(canvas);
//         chart.destroy();
//     }
//
//     const doughnutChart = new Chart(
//         canvas,
//         config,
//         options
//     );
//     $("#chart-container-id").append(canvas);
// })