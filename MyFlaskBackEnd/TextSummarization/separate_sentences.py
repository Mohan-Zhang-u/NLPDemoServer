import sys
import os
import codecs


def separate_by_dot(news_dir, tokenized_news_dir):
    if not os.path.exists(tokenized_news_dir):
        os.makedirs(tokenized_news_dir)
    news = os.listdir(news_dir)
    print("Separating sentences by dots...")
    for s in news:
        whole_article=""
        with codecs.open(os.path.join(news_dir, s), "r", encoding='utf-8') as fr:
            whole_article = fr.read()
        with codecs.open(os.path.join(tokenized_news_dir, s), "w", encoding='utf-8') as fw:
            whole_article = whole_article.replace(".", ". \n \n")
            fw.write(whole_article)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        news_dir = sys.argv[1]
        tokenized_news_dir = sys.argv[2]
        separate_by_dot(news_dir, tokenized_news_dir)

    else:
        print("USAGE: python separate_sentences.py <your_news_dir> <dir_to_store_your_tokenized_files")
        sys.exit()