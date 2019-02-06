$(document).ready(function () {
    $("#myButton").click(function (event) {
        const Url= AppConfig.public_ip_address + ":" + AppConfig.BERTPort + "/PostAcceptability";
        const InputTextAreaId = "#InputText";
        const ResponseTextAreaId = "#ReturnText";
        const ButtonId = "myButton";
        const myi = "myi";
        ButtonToggleFunction(ButtonId, myi);
        PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi, true,["Acceptable","Not Acceptable"]);
    });
});
