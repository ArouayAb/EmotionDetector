import { drawChart } from "./doughnutChart.js";

$(document).ready(function () {
    Dropzone.autoDiscover = false;
    let dropZone = new Dropzone("div#image-drop-zone", {
        url: $("#image-drop-zone").data("url"),
        autoProcessQueue: true,
        method: "post",
        headers: {'X-CSRFToken': $("#image-drop-zone").data("csrf")},
        success: function (file, response) {
            let output = JSON.parse(response);

            drawChart(output);
        }
    });

    dropZone.on("queuecomplete", function () {
        this.removeAllFiles();
    })
})
