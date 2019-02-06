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
});
