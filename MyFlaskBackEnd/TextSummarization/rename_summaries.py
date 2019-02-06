import os
import sys
import argparse


def rename(args):
    refs = os.listdir(args.refs_path)
    summs = os.listdir(args.summarization_path)
    for ref in refs:
        original_name = ref[:-4] + '.dec'
        with open(os.path.join(args.refs_path, ref), "r") as f:
            name = f.read()
            os.rename(os.path.join(args.summarization_path, original_name), os.path.join(args.summarization_path, name))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='rename summarized files corresponding to given news')
    parser.add_argument('--summarization_path', required=True, help='path to summarization')
    parser.add_argument('--refs_path', help='path to refs files')
    args = parser.parse_args()
    rename(args)
    # print(args.summarization_path)
    # print(args.refs_path)
