#!/anaconda/envs/py36/bin/python

from flask import Flask, request, jsonify, abort, make_response
# from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import subprocess
import time
import codecs
import os
import json
import csv
import nltk.data
import mzutils

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


'''Now starts core functions of text summarization server'''


# notice: function names of route should be different!!!!!
# all the tsv are read as strings


# now starts helper functions.
def SelectFirstSentence(InputText):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(InputText)[0]


def addSpacesBetweenSpecialCharacter(InputText):
    regular = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM "
    b = set(list(InputText))
    for i in b:
        if i not in regular:
            InputText = InputText.replace(i, ' ' + i + ' ')
    return InputText


@app.route('/PostAcceptability', methods=['POST'])
def PostAcceptabilityTextTask():
    if not request.json:
        abort(400)
    sentence = request.json['InputText']
    sentence = SelectFirstSentence(sentence)
    executable = "./inferencecola.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/CoLA/test.tsv"
    result_tsv = "../To_Be_Clean/CoLA/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "sentence"])
        tsv_writer.writerow(["0", sentence])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][1]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob


@app.route('/PostSentiment', methods=['POST'])
def PostSentimentTextTask():
    if not request.json:
        abort(400)
    sentence = request.json['InputText']
    sentence = SelectFirstSentence(sentence)
    sentence = addSpacesBetweenSpecialCharacter(sentence)
    executable = "./inferencesst.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/SST/test.tsv"
    result_tsv = "../To_Be_Clean/SST/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "sentence"])
        tsv_writer.writerow(["0", sentence])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][1]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob

    # result_class = "unknown"
    # if result_prob == "0":
    #     result_class = "negative"
    # elif result_prob == "1":
    #     result_class = "positive"
    #
    # # return result_prob+":"+str(isinstance(result_prob,str))+":"+str(isinstance(result_prob,int))


@app.route('/PostSentiment2', methods=['POST'])
def PostSentimentParagraphTask():
    if not request.json:
        abort(400)
    itext = request.json['InputText']
    itext = addSpacesBetweenSpecialCharacter(itext)
    sentences = nltk.tokenize.sent_tokenize(itext, 'english')
    sent_len = len(sentences)
    executable = "./inferencesst.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/SST/test.tsv"
    result_tsv = "../To_Be_Clean/SST/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "sentence"])
        for sentence in sentences:
            tsv_writer.writerow(["0", sentence])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    sentiment_value = 0
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row[1])
            if float(row[1]) > 0.5:
                sentiment_value += 1
    sentiment_value = sentiment_value / sent_len
    re_dict = {}
    re_dict["overall sentitment"] = sentiment_value
    detail_dict = {}
    for i in range(sent_len):
        detail_dict[sentences[i]] = cached_list[i]
    re_dict["sentences' individual sentiment"] = detail_dict

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return str(re_dict)


@app.route('/PostSimilarity', methods=['POST'])
def PostSimilarityTask():
    if not request.json:
        abort(400)
    sentence1 = request.json['InputText1']
    sentence2 = request.json['InputText2']
    sentence1 = SelectFirstSentence(sentence1)
    sentence2 = SelectFirstSentence(sentence2)
    sentence1 = addSpacesBetweenSpecialCharacter(sentence1)
    sentence2 = addSpacesBetweenSpecialCharacter(sentence2)
    executable = "./inferencemrpc.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/MRPC/test.tsv"
    result_tsv = "../To_Be_Clean/MRPC/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "#1 ID", "#2 ID", "#1 String", "#2 String"])
        tsv_writer.writerow(["0", "1089874", "1089925", sentence1, sentence2])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][1]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob


@app.route('/PostEntailment', methods=['POST'])
def PostEntailmentTask():
    if not request.json:
        abort(400)
    sentence1 = request.json['InputText1']
    sentence2 = request.json['InputText2']
    sentence1 = SelectFirstSentence(sentence1)
    sentence2 = SelectFirstSentence(sentence2)
    # sentence1 = addSpacesBetweenSpecialCharacter(sentence1)
    # sentence2 = addSpacesBetweenSpecialCharacter(sentence2)
    executable = "./inferencerte.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/RTE/test.tsv"
    result_tsv = "../To_Be_Clean/RTE/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "sentence1", "sentence2"])
        tsv_writer.writerow(["0", sentence1, sentence2])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][0]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob


@app.route('/PostQuestionInference', methods=['POST'])
def PostQuestionInferenceTask():
    if not request.json:
        abort(400)
    sentence1 = request.json['InputText1']
    sentence2 = request.json['InputText2']
    sentence1 = SelectFirstSentence(sentence1)
    sentence2 = SelectFirstSentence(sentence2)
    # sentence1 = addSpacesBetweenSpecialCharacter(sentence1)
    # sentence2 = addSpacesBetweenSpecialCharacter(sentence2)
    executable = "./inferencequestioninference.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/QNLI/test.tsv"
    result_tsv = "../To_Be_Clean/QNLI/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "question", "sentence"])
        tsv_writer.writerow(["0", sentence1, sentence2])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][0]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob


@app.route('/PostQuestionSimilarity', methods=['POST'])
def PostQuestionSimilarityTask():
    if not request.json:
        abort(400)
    sentence1 = request.json['InputText1']
    sentence2 = request.json['InputText2']
    sentence1 = SelectFirstSentence(sentence1)
    sentence2 = SelectFirstSentence(sentence2)
    # sentence1 = addSpacesBetweenSpecialCharacter(sentence1)
    # sentence2 = addSpacesBetweenSpecialCharacter(sentence2)
    executable = "./inferencequestionsimilarity.sh"
    clean = "./clean.sh"
    test_tsv = "../To_Be_Clean/QQP/test.tsv"
    result_tsv = "../To_Be_Clean/QQP/output/test_results.tsv"

    # read tsv
    with codecs.open(test_tsv, "w", encoding="utf-8") as fp:
        tsv_writer = csv.writer(fp, delimiter='\t')
        tsv_writer.writerow(["index", "question11", "question2"])
        tsv_writer.writerow(["0", sentence1, sentence2])

    # inference
    p1 = subprocess.Popen([executable], shell=True, executable="/bin/bash")
    p1.wait()

    # get result
    cached_list = []
    with codecs.open(result_tsv, "r", encoding="utf-8") as fp:
        tsv_reader = csv.reader(fp, delimiter='\t')
        for row in tsv_reader:
            cached_list.append(row)
    result_prob = cached_list[0][1]  # it is the acceptable prob

    # clean
    p2 = subprocess.Popen([clean], shell=True, executable="/bin/bash")
    p2.wait()

    return result_prob


@app.route("/")
def hello():
    import platform
    return "123"


@app.route("/hello")
def hello2():
    import platform
    return "1234"


if __name__ == "__main__":
    app.run()
