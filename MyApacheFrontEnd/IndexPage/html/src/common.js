var AppConfig;
$.getJSON("./src/config.json", function (json) {
    AppConfig = json;
});

function LoadGoogle() {
    if (typeof google != 'undefined' && google) {
        // google.load('visualization', '1.0', {
        //     'packages': ['corechart']
        // });
        google.charts.load('current', {'packages': ['corechart']});
        google.charts.setOnLoadCallback();
    } else {
        setTimeout(LoadGoogle, 30);
    }
}

LoadGoogle();


function ClickToDrawChart(labels = ['False', 'True'], probs = '0.0', chartid = "piechart") {
    if (labels.length != (probs.length + 1)) {
        alert("labels and probs length not match!");
        alert(labels);
        alert(probs);
        alert(labels.length);
        return;
    }
    var i;
    sum_probs = 0;
    chartarr = [['label', 'Probability']];
    for (i = 0; i < probs.length; i++) {
        sum_probs += parseFloat(probs[i]);
        chartarr.push([labels[i], parseFloat(probs[i])]);
    }
    chartarr.push([labels[probs.length], 1 - sum_probs]);

    // var data = google.visualization.arrayToDataTable([
    //
    //     ['label', 'Probability'],
    //
    //     ['true', parseFloat("0.991")],
    //
    //     ['false', 1 - parseFloat("0.991")]
    //
    // ]);

    var data = google.visualization.arrayToDataTable(chartarr);
    var options = {'title': 'Probability Distribution', 'width': 550, 'height': 400};
    var chart = new google.visualization.PieChart(document.getElementById(chartid));
    chart.draw(data, options);
}


function ButtonToggleFunction(ButtonId, myi) {
    var element = document.getElementById(myi);
    var myButton = $(ButtonId);
    element.classList.toggle("fa-spinner");
    element.classList.toggle("fa-spin");
}


function PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi, CreateChart = false, labels = ['False', 'True'], ChartDefaultInput = '0.0', chartid = "piechart") {
    var myresponse = 'notknown';
    var InputText = $(InputTextAreaId).val();
    var PostJson = {
        "InputText": InputText
    };
    var jfPostJson = JSON.stringify(PostJson);
    $.ajax({
        url: Url,
        type: "POST",
        contentType: "application/json;charset=utf-8",
        data: jfPostJson,
        dataType: 'text',
        cache: false,
        crossDomain: true,
        success: function (response) {
            console.log("success");
            $(InputTextAreaId).val(InputText);
            $(ResponseTextAreaId).val(response);
            myresponse = response;
            if (CreateChart === true) {
                ClickToDrawChart(labels, [response], chartid);
            }
        },
        complete: function (jqXHR, textStatus) {
            console.log("complete");
        }
    }).done(function (response) {
        console.log("done");
        ButtonToggleFunction(ButtonId, myi);
        document.getElementById(ButtonId).disabled = false;

    }).fail(function (jqXHR, textStatus) {
        alert("fail");
    });
    return myresponse;
}

//
// function PostBioBERTQATextFunction(Url, InputText1AreaId, InputText2AreaId, ResponseTextAreaId, ButtonId, myi, CreateChart = false, labels = ['False', 'True'], ChartDefaultInput = '0.0', chartid = "piechart") {
//     var myresponse = 'notknown';
//     var InputText1 = $(InputTextAreaId1).val();
//     var InputText2 = $(InputText2AreaId2).val();
//     var PostJson = {
//         "InputText1": InputText1,
//         "InputText2": InputText2
//     };
//     var jfPostJson = JSON.stringify(PostJson);
//     $.ajax({
//         url: Url,
//         type: "POST",
//         contentType: "application/json;charset=utf-8",
//         data: jfPostJson,
//         dataType: 'text',
//         cache: false,
//         crossDomain: true,
//         success: function (response) {
//             console.log("success");
//             $(InputTextAreaId1).val(InputText1);
//             $(InputTextAreaId2).val(InputText2);
//             $(ResponseTextAreaId).val(response);
//             myresponse = response;
//             if (CreateChart === true) {
//                 ClickToDrawChart(labels, [response], chartid);
//             }
//         },
//         complete: function (jqXHR, textStatus) {
//             console.log("complete");
//         }
//     }).done(function (response) {
//         console.log("done");
//         ButtonToggleFunction(ButtonId, myi);
//         document.getElementById(ButtonId).disabled = false;
//
//     }).fail(function (jqXHR, textStatus) {
//         alert("fail");
//     });
//     return myresponse;
// }


function PostSimilarityTextFunction(Url, InputText1AreaId, InputText2AreaId, ResponseTextAreaId, ButtonId, myi, CreateChart = false, labels = ['False', 'True'], ChartDefaultInput = '0.0', chartid = "piechart") {
    var myresponse = 'notknown';
    var InputText1 = $(InputText1AreaId).val();
    var InputText2 = $(InputText2AreaId).val();
    var PostJson = {
        "InputText1": InputText1,
        "InputText2": InputText2
    };
    var jfPostJson = JSON.stringify(PostJson);
    $.ajax({
        url: Url,
        type: "POST",
        contentType: "application/json",
        data: jfPostJson,
        dataType: 'text',
        cache: false,
        crossDomain: true,
        success: function (response) {
            console.log("success");
            console.log(response);
            $(InputText1AreaId).val(InputText1);
            $(InputText2AreaId).val(InputText2);
            $(ResponseTextAreaId).val(response);
            myresponse = response;
            if (CreateChart === true) {
                ClickToDrawChart(labels, [response], chartid);
            }
        },
        complete: function (jqXHR, textStatus) {
            console.log("complete");
        }
    }).done(function (response) {
        console.log("done");
        ButtonToggleFunction(ButtonId, myi);
        document.getElementById(ButtonId).disabled = false;

    }).fail(function (jqXHR, textStatus) {
        alert("fail");
    });
    return myresponse;
}


function PostZipFileFunction(Url, FormId, ButtonId, myi) {
    var form_data = new FormData($(FormId)[0]);
    $.ajax({
        type: 'POST',
        url: Url,
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        crossDomain: true,
        success: function (data) {
            console.log('Success!');
        },
    }).done(function (response) {
        console.log("done");
        ButtonToggleFunction(ButtonId, myi);
        document.getElementById(ButtonId).disabled = false;
    }).fail(function (jqXHR, textStatus) {
        alert("fail");
    });
}


//
// $(document).ready(function () {
//     $("#myButton").click(function (event) {
//             const Url = AppConfig.public_ip_address + ":" + AppConfig.SummarizationPort + "/PostInputText";
//             const InputTextAreaId = "#InputText";
//             const ResponseTextAreaId = "#SummaryText";
//             const ButtonId = "myButton";
//             const myi = "myi";
//             ButtonToggleFunction(ButtonId, myi);
//             PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi);
//     });
// });
