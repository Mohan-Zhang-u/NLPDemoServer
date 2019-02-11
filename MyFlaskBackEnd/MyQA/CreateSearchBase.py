import os
import sys

sys.path.append("retriever")
# sys.path.append("retriever/subutils")
import argparse
import mzutils
import SupportingScripts.DocumentsSegmentorandFillInFiles
import retriever.FromPureTextToJsons
import retriever.build_db
import retriever.build_tfidf
import subprocess
import math

my_args = ["UploadFolder", "MyCorpus", "MySegmented", 3847681024, "MyRetrievedData", "MyRetrievedData/tmp",
           "MyRetrievedData/tmp/MyCorpusJson", "MyRetrievedData/tmp/MyCorpusDataBase", "MyRetrievedData/myTFIDF",
           "MyRetrievedData/tmp/MyCorpusDataBase/db.db"]


def main_func(H, isServer):
    # os.environ['PATH'] = "/anaconda/envs/py36QA/bin"
    # os.environ['CLASSPATH'] = "data/corenlp/*"
    #
    mzutils.clean_dir(my_args[5], just_files=False)
    mzutils.clean_dir(my_args[2], just_files=False)
    if isServer:
        mzutils.clean_dir(my_args[1], just_files=False)
        mzutils.unzip_all(my_args[0], my_args[1])

    mzutils.mkdir_p(my_args[2])
    mzutils.mkdir_p(my_args[4])
    mzutils.mkdir_p(my_args[5])
    mzutils.mkdir_p(my_args[6])
    mzutils.mkdir_p(my_args[7])
    mzutils.mkdir_p(my_args[8])
    print(1)
    SupportingScripts.DocumentsSegmentorandFillInFiles.main_func(my_args[1], my_args[2], H)
    print(2)
    retriever.FromPureTextToJsons.CreateJsonFile(my_args[2], my_args[6])
    print(3)
    retriever.build_db.store_contents(my_args[6], my_args[9], None, None)
    p2 = subprocess.call([sys.executable, "retriever/build_tfidf.py", my_args[9], my_args[8]])

    # mzutils.clean_dir(my_args[5], just_files=False)
    if isServer:
        mzutils.clean_dir(my_args[1], just_files=False)
        mzutils.clean_dir(my_args[0], just_files=False)


# retriever.build_db.store_contents(my_args[6], my_args[9])
# p1 = subprocess.Popen(["python retriever/build_db.py " + my_args[6] + " " + my_args[9]], shell=True,
#                       executable="/bin/bash")
# p1 = subprocess.Popen([r"python retriever/build_db.py","-data_path", my_args[6], "-save_path", my_args[9]], shell=True,
#                       executable="/bin/bash")
# p1.wait()
# p2 = subprocess.Popen(["python retriever/build_tfidf.py " + my_args[9] + " " + my_args[8]], shell=True,
#                       executable="/bin/bash")
# p2.wait()
# retriever.build_tfidf.main_func(my_args[9], my_args[8], 2, int(math.pow(2, 24)), 'simple', None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--isServer', type=str, default="True", help='Running from the server side or not')
    parser.add_argument('--MyCorpus_path', type=str, default='MyCorpus/', help='MyCorpus/')
    parser.add_argument('--MySegmented_path', type=str, default='MySegmented/', help='MySegmented/')
    parser.add_argument('--H', type=int, default=768,
                        help='This is the H parameter from BERT. If using BERT BASE, H = 768. If suing BERT LARGE, H = 1024. Default is set ti 768.')
    args = parser.parse_args()
    main_func(args.H, mzutils.argparse_bool(args.isServer))
