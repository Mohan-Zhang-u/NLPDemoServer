// import * as AppConfig from "./config.json";
var AppConfig;
$.getJSON("./src/config.json", function (json) {
    AppConfig = json;
    $("a[href='https://summarization-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/summarization.html");
    $("a[href='https://qa-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/qa.html");
    $("a[href='https://acceptability-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/acceptability.html");
    $("a[href='https://sentiment-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/sentiment.html");
    $("a[href='https://similarity-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/similarity.html");
    $("a[href='https://entailment-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/entailment.html");
    $("a[href='https://biobertindex-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/biobertindex.html");
    $("a[href='https://questioninference-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/questioninference.html");
    $("a[href='https://questionsimilarity-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/questionsimilarity.html");
})


$(document).ready(function () {
    $("a[href='https://summarization-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/summarization.html");
    $("a[href='https://qa-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/qa.html");
    $("a[href='https://acceptability-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/acceptability.html");
    $("a[href='https://sentiment-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/sentiment.html");
    $("a[href='https://similarity-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/similarity.html");
    $("a[href='https://entailment-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/entailment.html");
    $("a[href='https://biobertindex-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/biobertindex.html");
    $("a[href='https://questioninference-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/questioninference.html");
    $("a[href='https://questionsimilarity-address']").attr("href", AppConfig.public_ip_address + ":" + AppConfig.IndexPagePort + "/questionsimilarity.html");
});
