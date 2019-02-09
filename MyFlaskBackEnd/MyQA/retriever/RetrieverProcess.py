import codecs
import argparse
import json
from subutils import tfidf_doc_ranker


def process(tfidf_model_path, question, k):
    ranker = tfidf_doc_ranker.TfidfDocRanker(tfidf_path=tfidf_model_path)
    doc_names, doc_scores = ranker.closest_docs(question, k)
    return doc_names, doc_scores


def main_func(tfidf_model_path, question, k, retrieved_json_path):
    doc_names, doc_scores = process(tfidf_model_path, question, k)
    my_dict = {}
    my_dict["doc_names"] = doc_names
    my_dict["doc_scores"] = doc_scores.tolist()
    with codecs.open(retrieved_json_path, 'w', encoding='utf-8') as fp:
        json.dump(my_dict, fp)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('tfidf_model_path', type=str, help='/path/to/tfidf_model.npz')
    parser.add_argument('question', type=str, help='the quetion to be answered')
    parser.add_argument('k', type=int, default=3, help='the maximum number of documents to be retrieved')
    parser.add_argument('retrieved_json_path', type=str, help='/path/to/retrieved_json.json')
    args = parser.parse_args()
    main_func(args.tfidf_model_path, args.question, args.k, args.retrieved_json_path)
