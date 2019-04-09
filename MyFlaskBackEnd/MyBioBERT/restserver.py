#!/anaconda/envs/py36/bin/python

from flask import Flask, request, jsonify, abort, make_response
# from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import subprocess
import codecs
import os
import sys
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


@app.route('/PostQA', methods=['POST'])
def PostBERTQA():
    if not request.json:
        abort(400)
    content = request.json['InputText1']
    question = request.json['InputText2']
    dir_path = "To_Be_Clean/QA"
    test_file = "test-v1.1.json"
    mzutils.mkdir_p(dir_path)
    mzutils.clean_dir(dir_path, False)
    mzutils.generate_multi_test_cases([content], [question], os.path.join(dir_path, test_file))
    p1 = subprocess.call([sys.executable, "run_qa.py", "--do_train=False", "--do_predict=True",
                          "--vocab_file=Data/pubmed_pmc_470k/vocab.txt",
                          "--bert_config_file=Data/pubmed_pmc_470k/bert_config.json",
                          "--init_checkpoint=fine_tuned/QA/", "--max_seq_length=384", "--train_batch_size=12",
                          "--learning_rate=3e-5", "--doc_stride=128", "--num_train_epochs=50.0",
                          "--do_lower_case=False", "--predict_file=To_Be_Clean/QA/test-v1.1.json",
                          "--output_dir=To_Be_Clean/QA/"])

    return str(list(mzutils.load_config("To_Be_Clean/QA/predictions.json").values())[0])
    # with codecs.open("To_Be_Clean/QA/predictions.json", "r", encoding="utf-8") as fp:
    #     return fp.read()


@app.route('/PostRE', methods=['POST'])
def PostBERTRE():
    if not request.json:
        abort(400)
    sentence = request.json['InputText']
    dir_path = "To_Be_Clean/REdata/GAD/1"
    test_file = "test.tsv"
    mzutils.mkdir_p(dir_path)
    mzutils.clean_dir(dir_path, False)
    rows = [["index", "sentence", "label"], [0, sentence, 9]]
    mzutils.write_tsv(os.path.join(dir_path, test_file), rows)
    p1 = subprocess.call(
        [sys.executable, "run_re.py", "--task_name=gad", "--do_train=False", "--do_eval=False", "--do_predict=True",
         "--vocab_file=Data/pubmed_pmc_470k/vocab.txt",
         "--bert_config_file=Data/pubmed_pmc_470k/bert_config.json",
         "--init_checkpoint=fine_tuned/REdata/GAD/1/", "--max_seq_length=128", "--train_batch_size=12",
         "--learning_rate=3e-5", "--num_train_epochs=3.0",
         "--do_lower_case=false", "--data_dir=To_Be_Clean/REdata/GAD/1/", "--output_dir=To_Be_Clean/REdata/GAD/1/"])

    return mzutils.read_tsv(os.path.join(dir_path, "test_results.tsv"))[0][1]
    # with codecs.open("To_Be_Clean/QA/predictions.json", "r", encoding="utf-8") as fp:
    #     return fp.read()


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
