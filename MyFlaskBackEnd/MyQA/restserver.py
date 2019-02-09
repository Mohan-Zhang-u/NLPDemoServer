#!/anaconda/envs/py36/bin/python

from flask import Flask, request, jsonify, abort, make_response, flash, redirect, url_for, send_from_directory
# from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from werkzeug.utils import secure_filename
import subprocess
import time
import codecs
import os
import json

import CreateSearchBase
import AnswerTheQuestion


UPLOAD_FOLDER = 'UploadFolder'
ALLOWED_EXTENSIONS = set(['txt', 'zip'])

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


'''Now starts core functions of QA server'''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadzip', methods=['GET', 'POST'])
def upload_file():
    import sys
    with open('1111111111.txt','w+') as fp:
        fp.write(sys.executable)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            CreateSearchBase.main_func()

            # runstring = "./run.sh"
            # p1 = subprocess.Popen([runstring], shell=True, executable="/bin/bash")
            # p1.wait()
            return "finished"
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/answerquestion', methods=['POST'])
def PostInputTextTask():
    if not request.json:
        abort(400)
    file_text = request.json['InputText']
    AnswerTheQuestion.main_func(file_text)
    with codecs.open("MyAnswers/predictions.json", 'r', encoding='utf-8') as fp:
        predictDict = json.load(fp)
    if list(predictDict.values())[0] == "empty":
        return "Sorry, the model is not able to find an answer to the question in the uploaded corpus."
    else:
        return predictDict

    # ctime = str(int(round(time.time() * 1000)))
    # runstring = "./AnswerTheQuestion.sh \"" + file_text + "\""
    # p1 = subprocess.Popen([runstring], shell=True, executable="/bin/bash")
    # p1.wait()
    # with codecs.open("../MyAnswers/predictions.json", 'r', encoding='utf-8') as fp:
    #     predictDict = json.load(fp)
    # ans = list(predictDict.values())[0]
    # if ans == "empty":
    #     return "Sorry, the model is not able to find an answer to the question in the uploaded corpus."
    # else:
    #     return ans


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


# def store_file(text, ctime):
#     if not os.path.exists("../To_Be_Clean"):
#         os.mkdir("../To_Be_Clean")
#     if not os.path.exists("../To_Be_Clean/" + ctime):
#         os.mkdir("../To_Be_Clean/" + ctime)
#     if not os.path.exists("../To_Be_Clean/" + ctime + "/my_news"):
#         os.mkdir("../To_Be_Clean/" + ctime + "/my_news")
#     with codecs.open("../To_Be_Clean/" + ctime + "/my_news/1", 'w', encoding='utf-8') as fp:
#         fp.write(text)
#
#
# def open_sum(ctime):
#     with codecs.open("../To_Be_Clean/" + ctime + "/summarizations/output/1", 'r', encoding='utf-8') as fp:
#         return fp.read()
#
#
# @app.route('/PostInputText', methods=['POST'])
# def PostInputTextTask():
#     if not request.json:
#         abort(400)
#     # return json.dumps(request.json['InputText'])
#     file_text = request.json['InputText']
#     ctime = str(int(round(time.time() * 1000)))
#     runstring = "./run.sh " + str(ctime)
#     store_file(file_text, ctime)
#     p1 = subprocess.Popen([runstring], shell=True, executable="/bin/bash")
#     p1.wait()
#     my_sum = open_sum(ctime)
#     p2 = subprocess.Popen(["./clean.sh " + ctime], shell=True, executable="/bin/bash")
#     p2.wait()
#     return my_sum


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


# @app.route("/")
# def hello():
#     import platform
#     return "123"


if __name__ == "__main__":
    app.run()
