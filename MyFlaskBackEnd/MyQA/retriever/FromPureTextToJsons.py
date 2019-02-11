''' this file converts a set of UTF-8 encoded documents with no repeated names to json files like:

{"id": "doc1", "text": "text of doc1"}
...
{"id": "docN", "text": "text of docN"}
'''

import json
import codecs
import os
import argparse

def CreateJsonFile(datafile_path, json_path):
    for filename in os.listdir(datafile_path):
        with codecs.open(os.path.join(datafile_path, filename), 'r', encoding='utf8') as fp:
            text = fp.read()
            dictionary={}
            dictionary['id']=filename
            dictionary['text']=text
            print(dictionary.keys())
            with codecs.open(os.path.join(json_path, filename), 'w', encoding='utf8') as fpw:
                json.dump(dictionary, fpw)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('datafile_path', type=str, help='/path/to/datafiles')
    parser.add_argument('json_path', type=str, help='/path/to/store/jsonfiles')
    args = parser.parse_args()
    CreateJsonFile(args.datafile_path, args.json_path)