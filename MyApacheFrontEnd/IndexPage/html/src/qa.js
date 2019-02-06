$(document).ready(function () {
    $("#uploadButton").click(function (event) {
        const Url=AppConfig.public_ip_address + ":" + AppConfig.QAPort + "/uploadzip";
        const FormId = "#InputZip";
        const ButtonId = "uploadButton";
        const myi = "uploadmyi";
        ButtonToggleFunction(ButtonId, myi);
        PostZipFileFunction(Url, FormId, ButtonId, myi);
    });

    $("#myButton").click(function (event) {
        const Url=AppConfig.public_ip_address + ":" + AppConfig.QAPort + "/answerquestion";
        const InputTextAreaId = "#InputText";
        const ResponseTextAreaId = "#ResponseText";
        const ButtonId = "myButton";
        const myi = "myi";
        ButtonToggleFunction(ButtonId, myi);
        PostInputTextFunction(Url, InputTextAreaId, ResponseTextAreaId, ButtonId, myi);
    });
});
