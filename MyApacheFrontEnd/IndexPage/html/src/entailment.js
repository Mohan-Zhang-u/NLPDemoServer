$(document).ready(function () {
    $("#myButton").click(function (event) {
        const Url= AppConfig.public_ip_address + ":" + AppConfig.BERTPort + "/PostEntailment";
        const InputTextAreaId1 = "#InputText1";
        const InputTextAreaId2 = "#InputText2";
        const ResponseTextAreaId = "#ReturnText";
        const ButtonId = "myButton";
        const myi = "myi";
        ButtonToggleFunction(ButtonId, myi);
        PostSimilarityTextFunction(Url, InputTextAreaId1, InputTextAreaId2, ResponseTextAreaId, ButtonId, myi, true, ["Context entails Hypothesis", "Context does not entail Hypothesis"]);
    });
});
