""" make reference text files needed for ROUGE evaluation """
import json
import sys
import os
from os.path import join, exists
from time import time
from datetime import timedelta

from utils import count_data
from decoding import make_html_safe

try:
    DATA_DIR = os.environ['DATA']
except KeyError:
    print('please use environment variable to specify data directories')


def dump(split):
    start = time()
    print('start processing {} split...'.format(split))
    data_dir = join(DATA_DIR, split)
    dump_dir = join(DATA_DIR, 'refs', split)
    n_data = count_data(data_dir)
    for i in range(n_data):
        print('processing {}/{} ({:.2f}%%)\r'.format(i, n_data, 100*i/n_data),
              end='')
        with open(join(data_dir, '{}.json'.format(i))) as f:
            data = json.loads(f.read())
        abs_sents = data['abstract']
        with open(join(dump_dir, '{}.ref'.format(i)), 'w') as f:
            f.write(make_html_safe('\n'.join(abs_sents)))
    print('finished in {}'.format(timedelta(seconds=time()-start)))

def main():
    for split in ['val', 'test']:  # evaluation of train data takes too long
        if not exists(join(DATA_DIR, 'refs', split)):
            os.makedirs(join(DATA_DIR, 'refs', split))
        dump(split)

def make_ref_for_news_name():
    if not exists(join(DATA_DIR, 'refs')):
        os.makedirs(join(DATA_DIR, 'refs'))
        start = time()
        print('start processing test split...')
        data_dir = join(DATA_DIR, 'test')
        dump_dir = join(DATA_DIR, 'refs')
        n_data = count_data(data_dir)
        for i in range(n_data):
            print('processing {}/{} ({:.2f}%%)\r'.format(i, n_data, 100 * i / n_data),
                  end='')
            with open(join(data_dir, '{}.json'.format(i))) as f:
                data = json.loads(f.read())
            ids = data['id']
            with open(join(dump_dir, '{}.ref'.format(i)), 'w') as f:
                f.write(ids)
        print('finished in {}'.format(timedelta(seconds=time() - start)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        make_ref_for_news_name()
    else:
        main()
