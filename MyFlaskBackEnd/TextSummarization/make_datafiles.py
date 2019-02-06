import sys
import os
import hashlib
import subprocess
import collections

import json
import tarfile
import io
import pickle as pkl
import codecs


dm_single_close_quote = '\u2019' # unicode
dm_double_close_quote = '\u201d'
# acceptable ways to end a sentence
END_TOKENS = ['.', '!', '?', '...', "'", "`", '"',
              dm_single_close_quote, dm_double_close_quote, ")"]

# my_tokenized_stories_dir = "To_Be_Clean/my_stories_tokenized"
# finished_files_dir = "To_Be_Clean/finished_files"

tokenized_stories_list = []


def tokenize_stories(stories_dir, tokenized_stories_dir):
    """Maps a whole directory of .story files to a tokenized version using
       Stanford CoreNLP Tokenizer
    """
    print("Preparing to tokenize {} to {}...".format(stories_dir,
                                                     tokenized_stories_dir))
    stories = os.listdir(stories_dir)
    print("storis length is:" + str(len(stories)))
    # make IO list file
    print("Making list of files to tokenize...")
    with codecs.open("mapping.txt", "w", encoding="utf-8") as f:
        for s in stories:
            f.write(
                "{} \t {}\n".format(
                    os.path.join(stories_dir, s),
                    os.path.join(tokenized_stories_dir, s)
                )
            )
            tokenized_stories_list.append(s)
    command = ['java', 'edu.stanford.nlp.process.PTBTokenizer',
               '-ioFileList', '-preserveLines', 'mapping.txt']
    print("Tokenizing {} files in {} and saving in {}...".format(
        len(stories), stories_dir, tokenized_stories_dir))
    subprocess.call(command)
    print("Stanford CoreNLP Tokenizer has finished.")
    os.remove("mapping.txt")

    # Check that the tokenized stories directory contains the same number of
    # files as the original directory
    num_orig = len(os.listdir(stories_dir))
    num_tokenized = len(os.listdir(tokenized_stories_dir))
    if num_orig != num_tokenized:
        raise Exception(
            "The tokenized stories directory {} contains {} files, but it "
            "should contain the same number as {} (which has {} files). Was"
            " there an error during tokenization?".format(
                tokenized_stories_dir, num_tokenized, stories_dir, num_orig)
        )
    print("Successfully finished tokenizing {} to {}.\n".format(
        stories_dir, tokenized_stories_dir))


def read_story_file(text_file):
    with codecs.open(text_file, "r", encoding="utf-8") as f:
        # sentences are separated by 2 newlines
        # single newlines might be image captions
        # so will be incomplete sentence
        lines = f.read().split('\n\n')
    return lines


def hashhex(s):
    """Returns a heximal formated SHA1 hash of the input string."""
    h = hashlib.sha1()
    h.update(s.encode())
    return h.hexdigest()


def get_url_hashes(url_list):
    return [hashhex(url) for url in url_list]


def fix_missing_period(line):
    """Adds a period to a line that is missing a period"""
    if "@highlight" in line:
        return line
    if line == "":
        return line
    if line[-1] in END_TOKENS:
        return line
    return line + " ."


def get_art_abs(story_file):
    """ return as list of sentences"""
    lines = read_story_file(story_file)

    # Lowercase, truncated trailing spaces, and normalize spaces
    lines = [' '.join(line.lower().strip().split()) for line in lines]

    # Put periods on the ends of lines that are missing them (this is a problem
    # in the dataset because many image captions don't end in periods;
    # consequently they end up in the body of the article as run-on sentences)
    lines = [fix_missing_period(line) for line in lines]

    # Separate out article and abstract sentences
    article_lines = []
    highlights = []
    next_is_highlight = False
    for idx, line in enumerate(lines):
        if line == "":
            continue # empty line
        elif line.startswith("@highlight"):
            next_is_highlight = True
        elif next_is_highlight:
            highlights.append(line)
        else:
            article_lines.append(line)

    return article_lines, highlights


def my_write_to_tar(tokenized_files_location, out_file, makevocab=False):
    """Reads the tokenized .story files corresponding to the urls listed in the
       url_file and writes them to a out_file.
    """
    print("Making bin file for stories...")
    num_stories = len(tokenized_stories_list)

    if makevocab:
        vocab_counter = collections.Counter()

    with tarfile.open(out_file, 'w') as writer:
        for idx, s in enumerate(tokenized_stories_list):
            if idx % 1000 == 0:
                print("Writing story {} of {}; {:.2f} percent done".format(
                    idx, num_stories, float(idx)*100.0/float(num_stories)))

            if os.path.isfile(os.path.join(tokenized_files_location, s)):
                story_file = os.path.join(tokenized_files_location, s)
            else:
                print("File name " + s + " does not exist in the directory " + tokenized_files_location)
            # Get the strings to write to .bin file
            article_sents, abstract_sents = get_art_abs(story_file)

            # Write to JSON file
            js_example = {}
            js_example['id'] = s
            js_example['article'] = article_sents
            js_example['abstract'] = abstract_sents
            js_serialized = json.dumps(js_example, indent=4).encode()
            save_file = io.BytesIO(js_serialized)
            tar_info = tarfile.TarInfo('{}/{}.json'.format(
                os.path.basename(out_file).replace('.tar', ''), idx))
            tar_info.size = len(js_serialized)
            writer.addfile(tar_info, save_file)

            # Write the vocab to file, if applicable
            if makevocab:
                art_tokens = ' '.join(article_sents).split()
                abs_tokens = ' '.join(abstract_sents).split()
                tokens = art_tokens + abs_tokens
                tokens = [t.strip() for t in tokens] # strip
                tokens = [t for t in tokens if t != ""] # remove empty
                vocab_counter.update(tokens)

    print("Finished writing file {}\n".format(out_file))

    # write vocab to file
    if makevocab:
        print("Writing vocab file...")
        with codecs.open(os.path.join(finished_files_dir, "vocab_cnt.pkl"),
                  'wb', encoding="utf-8") as vocab_file:
            pkl.dump(vocab_counter, vocab_file)
        print("Finished writing vocab file")


if __name__ == '__main__':
    if len(sys.argv) == 4:
        my_stories_dir =sys.argv[1]
        my_tokenized_stories_dir = sys.argv[2] #"To_Be_Clean/my_stories_tokenized"
        finished_files_dir = sys.argv[3] #"To_Be_Clean/finished_files"

        if not os.path.exists(my_tokenized_stories_dir):
            os.makedirs(my_tokenized_stories_dir)

        if not os.path.exists(finished_files_dir):
            os.makedirs(finished_files_dir)
        
        tokenize_stories(my_stories_dir, my_tokenized_stories_dir)
        my_write_to_tar(my_tokenized_stories_dir, os.path.join(finished_files_dir, "test.tar"))
    
    else:
        print("USAGE: python make_datafiles.py"
              " <your_stories_dir> <your_tokenized_stories_dir> <finished_files_dir>")
        sys.exit()
    