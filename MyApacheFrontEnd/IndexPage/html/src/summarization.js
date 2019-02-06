$(document).ready(function () {
    $("#myButton").click(function (event) {
        const Url= AppConfig.public_ip_address + ":" + AppConfig.SummarizationPort + "/PostInputText";
        const InputTextAreaId = "#InputText";
        const ResponseTextAreaId = "#SummaryText";
        const ButtonId = "myButton";
        const myi = "myi";
        ButtonToggleFunction(ButtonId, myi);
        PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi);
    });
});
