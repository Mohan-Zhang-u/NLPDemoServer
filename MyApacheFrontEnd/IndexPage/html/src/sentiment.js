$(document).ready(function () {
    $("#myButton").click(function (event) {
        const Url= AppConfig.public_ip_address + ":" + AppConfig.BERTPort + "/PostSentiment";
        const InputTextAreaId = "#InputText";
        const ResponseTextAreaId = "#ReturnText";
        const ButtonId = "myButton";
        const myi = "myi";
        ButtonToggleFunction(ButtonId, myi);
        var myresponse = PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi, true,["Positive","Negative"]);
    });

    $("#myButton2").click(function (event) {
        const Url= AppConfig.public_ip_address + ":" + AppConfig.BERTPort + "/PostSentiment2";
        const InputTextAreaId = "#InputText2";
        const ResponseTextAreaId = "#ReturnText2";
        const ButtonId = "myButton2";
        const myi = "myi2";
        ButtonToggleFunction(ButtonId, myi);
        var myresponse = PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi, false,["Positive","Negative"]);
    });

});
