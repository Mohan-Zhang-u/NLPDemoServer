import os
import sys
import argparse
import nltk
import codecs

'''
This python script is searching for any words in the original news article that are capitalized and not the first word
 in a sentence, then replace the lower cased version of them in the summaries.
Also, it replace every word in the summaries that is the first word in a sentence to be capitalized.
'''


def capitalize(args):
    original_news = os.listdir(args.original_news_path)
    summmaries = os.listdir(args.summarization_path)
    to_write=''
    for summary in summmaries:
        with codecs.open(os.path.join(args.original_news_path, summary), "r", encoding='utf-8') as fo:
            with codecs.open(os.path.join(args.summarization_path, summary), "r", encoding='utf-8') as fs:
                to_be_replaced = []
                original_text = fo.read()
                original_text_sentences = nltk.tokenize.sent_tokenize(original_text)
                original_words = sum([i for i in [sentence.split()[1:] for sentence in original_text_sentences]], [])
                for original_word in original_words:
                    if original_word.lower() != original_word:
                        if original_word[-1] == '.':
                            original_word = original_word[:-1]
                        to_be_replaced.append(original_word)

                summary_text = fs.read()
                summary_text_sentences = nltk.tokenize.sent_tokenize(summary_text)

                for i in range(len(summary_text_sentences)):
                    summary_text_sentences[i] = summary_text_sentences[i][0].upper()+summary_text_sentences[i][1:]
                summary_words = sum([i.split() for i in summary_text_sentences], [])
                for word in to_be_replaced:
                    if word.lower() in summary_words:
                        for i in range(len(summary_words)):
                            if word.lower() == summary_words[i]:
                                summary_words[i] = word

                # a = summary_text_sentences[0].split() + summary_text_sentences[1].split()
                b=''
                for i in summary_words:
                    if i != '.':
                        b += ' '
                    b += i
                b = b[1:]
                to_write = b
            with codecs.open(os.path.join(args.summarization_path, summary), "w", encoding='utf-8') as fs:
                fs.write(b)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Capitalize those words that should be capitalized.')
    parser.add_argument('--summarization_path', required=True, help='path to summarization')
    parser.add_argument('--original_news_path', required=True, help='path to original news')
    args = parser.parse_args()
    capitalize(args)