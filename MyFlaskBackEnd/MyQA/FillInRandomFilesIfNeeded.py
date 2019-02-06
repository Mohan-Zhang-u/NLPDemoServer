import codecs
import os
import time
import argparse


"""No that the TF-IDF retriever RetrieverProcess cannot retrieve when there are less than 3 files in MyCorpus, this file is to address this issue."""
"""Will be diged into."""


def create_Notselected_files(filepath):
    if not os.path.isfile(filepath):
        with codecs.open(filepath, 'w+', encoding='utf8') as fp:
            fp.write("I'm pretty sure that it is not the answer.")

def create_Notselected_file(corpus_path):
    ctime = str(int(round(time.time() * 1000)))
    num_of_files = len([name for name in os.listdir(corpus_path) if os.path.isfile(name)])
    if num_of_files < 3:
        # print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
        create_Notselected_files(corpus_path + ctime + "1" + ".txt")
        create_Notselected_files(corpus_path + ctime + "2" + ".txt")
        create_Notselected_files(corpus_path + ctime + "3" + ".txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('MyCorpus_path', type=str, help='MyCorpus/')
    args = parser.parse_args()
    create_Notselected_file(args.MyCorpus_path)
