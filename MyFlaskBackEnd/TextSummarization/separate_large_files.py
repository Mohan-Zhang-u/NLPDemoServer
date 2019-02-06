import os
import sys
import argparse
import codecs

def separate(args):
    with codecs.open(os.path.join(args.target_file_location, args.target_file_name), "r",  encoding='utf-8') as f:
        file = f.read()
        file = file.split('\n')
        num_of_sent = args.num_of_sent
        k=0
        for i in range(0, len(file), num_of_sent):
            k+=1
            files = file[i:i + num_of_sent]
            with codecs.open(os.path.join(args.storage_location, args.target_file_name + '_' + str(k)),'w', encoding='utf-8') as fw:
                for strings in files:
                    fw.write(strings + '\n')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='separate large articles into several smaller articles that contains several paragraphs of it so that the summarization has a better performance. ')
    parser.add_argument('--target_file_location', required=True, help='path to target file\'s parent directory that to be separated')
    parser.add_argument('--target_file_name', required=True, help='target file\'s name')
    parser.add_argument('--storage_location', help='path to store the separated files')
    parser.add_argument('--num_of_sent', nargs='?', type=int, default=10, help='number of paragraphs per article')
    args = parser.parse_args()
    if args.storage_location is None:
        args.storage_location = args.target_file_location
    separate(args)