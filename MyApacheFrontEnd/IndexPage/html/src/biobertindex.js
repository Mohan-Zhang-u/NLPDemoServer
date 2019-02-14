// import * as AppConfig from "./config.json";
var AppConfig;
$.getJSON("./src/config.json", function (json) {
    AppConfig = json;
    $("a[href='https://biobertqa-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/biobertqa.html");
})


$(document).ready(function () {
    $("a[href='https://biobertqa-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/biobertqa.html");
});
