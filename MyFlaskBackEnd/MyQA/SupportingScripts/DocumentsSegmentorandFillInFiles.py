"""
Note that, since in BERT, the probability of word i being the start (same with end)

And, it is tokenized wordly using WordPiece tokenizer, we shall limit it to 2/3 of H (768 for BERT base, 1024 for BERT large.)
"""

"""
No that the TF-IDF retriever RetrieverProcess cannot retrieve when there are less than 3 files in MyCorpus, this file is to address this issue.
Will be diged into.
"""

import codecs
import os
import time
import argparse
import mzutils


# def tokenize_to_sentences(location, filename):
#     sent_text=nltk.sent_tokenize(,'english')
# os.path.join(dir_path, name)

# def main_segmentor(MyCorpus, MySegmented, H):
#     names = [name for name in os.listdir(MyCorpus) if os.path.isfile(os.path.join(MyCorpus, name))]
#     for name in names:
#         document_segmentor(MyCorpus, MySegmented, name, H)
#
#
# def document_segmentor(MyCorpus, MySegmented, name, H):
#     limit = int(4 * H / 5)
#     documents = []
#     with codecs.open(os.path.join(MyCorpus, name), "r", "utf-8") as fp:
#         filecontent = fp.read()
#         sentences = nltk.sent_tokenize(filecontent, 'english')
#         i = 0
#         word_count = 0
#         document = ""
#         while i < len(sentences):
#             sentence = sentences[i]
#             current_count = len(nltk.word_tokenize(sentence, 'english'))
#             if word_count + current_count < limit:
#                 document = document + sentence + " "
#                 word_count = word_count + current_count
#                 i = i + 1
#             else:
#                 documents.append(document)
#                 word_count = 0
#                 document = ""
#         documents.append(document)
#     save_documents(MySegmented, name, documents)
#
#
# def save_documents(MySegmented, name, documents):
#     with codecs.open(os.path.join(MySegmented, name), "w+", "utf-8") as fp:
#         fp.write(documents[0])
#     for document in documents[1:]:
#         filepath = check_existance(MySegmented, name)
#         with codecs.open(filepath, "w+", "utf-8") as fp:
#             fp.write(document)
#
#
# def check_existance(location, name):
#     rand = str(int(round(time.time() * 1000)))
#     filepath = location + name
#     while os.path.exists(filepath):
#         filepath += rand
#     return filepath


def create_notselected_file(filepath):
    if not os.path.exists(filepath):
        with codecs.open(filepath, 'w+', encoding='utf8') as fp:
            fp.write("I'm pretty sure that it is not the answer.")


def create_notselected_files(MySegmented):
    ctime = str(int(round(time.time() * 1000)))
    num_of_files = len([name for name in os.listdir(MySegmented) if os.path.isfile(os.path.join(MySegmented, name))])
    if num_of_files < 3:
        create_notselected_file(os.path.join(MySegmented, ctime + "1" + ".txt"))
        create_notselected_file(os.path.join(MySegmented, ctime + "2" + ".txt"))
        create_notselected_file(os.path.join(MySegmented, ctime + "3" + ".txt"))


def main_func(MyCorpus_path, MySegmented_path, H):
    max_length = int(
        4 * H / 5)  # here, still need to implement sampling from customized distribution to eliminate bias.
    mzutils.documents_segementor_on_word_length(MyCorpus_path, MySegmented_path, max_length)
    # this is for the TF-IDF issue.
    create_notselected_files(MySegmented_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--MyCorpus_path', type=str, default='MyCorpus/', help='MyCorpus/')
    parser.add_argument('--MySegmented_path', type=str, default='MySegmented/', help='MySegmented/')
    parser.add_argument('--H', type=int, default=768,
                        help='This is the H parameter from BERT. If using BERT BASE, H = 768. If suing BERT LARGE, H = 1024. Default is set ti 768.')
    args = parser.parse_args()
    main_func(args.MyCorpus_path, args.MySegmented_path, args.H)

