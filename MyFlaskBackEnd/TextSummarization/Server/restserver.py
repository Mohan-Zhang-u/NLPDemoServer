#!/anaconda/envs/py36/bin/python

from flask import Flask, request, jsonify, abort, make_response
# from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import subprocess
import time
import codecs
import os
import json

app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


'''Now starts core functions of text summarization server'''


def store_file(text, ctime):
    if not os.path.exists("../To_Be_Clean"):
        os.mkdir("../To_Be_Clean")
    if not os.path.exists("../To_Be_Clean/" + ctime):
        os.mkdir("../To_Be_Clean/" + ctime)
    if not os.path.exists("../To_Be_Clean/" + ctime + "/my_news"):
        os.mkdir("../To_Be_Clean/" + ctime + "/my_news")
    with codecs.open("../To_Be_Clean/" + ctime + "/my_news/1", 'w', encoding='utf-8') as fp:
        fp.write(text)


def open_sum(ctime):
    with codecs.open("../To_Be_Clean/" + ctime + "/summarizations/output/1", 'r', encoding='utf-8') as fp:
        return fp.read()


@app.route('/PostInputText', methods=['POST'])
def PostInputTextTask():
    if not request.json:
        abort(400)
    # return json.dumps(request.json['InputText'])
    file_text = request.json['InputText']
    ctime = str(int(round(time.time() * 1000)))
    runstring = "./run.sh " + str(ctime)
    store_file(file_text, ctime)
    p1 = subprocess.Popen([runstring], shell=True, executable="/bin/bash")
    p1.wait()
    my_sum = open_sum(ctime)
    p2 = subprocess.Popen(["./clean.sh " + ctime], shell=True, executable="/bin/bash")
    p2.wait()
    return my_sum


# auth = HTTPBasicAuth()
#
# @auth.get_password
# def get_password(username):
#     if username == 'miguel':
#         return 'python'
#     return None
#
#
# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.route("/")
def hello():
    import platform
    return "123"



if __name__ == "__main__":
    app.run()
