import mzutils
import argparse
import subprocess
import os
import sys

sys.path.append("retriever")
import retriever.RetrieverProcess
import retriever.Pipeline

BERT_BASE_DIR = "MyBERT/fine_tuned/BERT_BASE/squad"
QES_JSON_DIR = "MyRetrievedData/DocToRead"
DEFAULT_CONTENT = "  I'm pretty sure that it is not the answer.  \n"


def main_func(question, isServer=True):
    mzutils.mkdir_p("MyRetrievedData/retrieved")
    mzutils.mkdir_p("MyRetrievedData/DocToRead")
    mzutils.mkdir_p("MyAnswers")
    mzutils.clean_dir("MyRetrievedData/retrieved", False)

    retriever.RetrieverProcess.main_func("MyRetrievedData/myTFIDF/SearchBase.npz", question, 3,
                                         "MyRetrievedData/retrieved/retrieved.json")
    retriever.Pipeline.pipeline("MySegmented", "MyRetrievedData/retrieved/retrieved.json",
                                "MyRetrievedData/DocToRead/DocToRead.json", question, DEFAULT_CONTENT)
    print("finished retrieve.")
    print(question)
    subprocess.call(
        [sys.executable, "MyBERT/run_squad.py",
         "--vocab_file=" + os.path.join(BERT_BASE_DIR, "vocab.txt"),
         "--bert_config_file=" + os.path.join(BERT_BASE_DIR, "bert_config.json"),
         "--init_checkpoint=" + os.path.join(BERT_BASE_DIR),
         "--do_train=False",
         "--train_file=",
         "--do_predict=True",
         "--predict_file=" + "MyRetrievedData/DocToRead/DocToRead.json",
         "--train_batch_size=12",
         "--learning_rate=3e-5",
         "--num_train_epochs=2.0",
         "--max_seq_length=384",
         "--doc_stride=128",
         "--output_dir=" + "MyAnswers/"
         ])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('question', type=str, help='The question to be asked.')
    parser.add_argument('--isServer', type=str, default="True", help='Running from the server side or not')
    args = parser.parse_args()
    main_func(args.question, mzutils.argparse_bool(args.isServer))
