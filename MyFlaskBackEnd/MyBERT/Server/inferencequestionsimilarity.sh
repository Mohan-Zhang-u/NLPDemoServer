#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36server/bin:$PATH"
# alias pip=/anaconda/envs/py36/bin/pip
alias anaconda-navigator=/anaconda/bin/anaconda-navigator


task_name="QQP"
python ../my_run_classifier.py \
 --task_name=qqp \
 --do_predict=true \
 --data_dir=../To_Be_Clean/QQP \
 --vocab_file=../fine_tuned/BERT_BASE/vocab.txt \
 --bert_config_file=../fine_tuned/BERT_BASE/bert_config.json \
 --init_checkpoint=../fine_tuned/BERT_BASE/QQP_output \
 --max_seq_length=128 \
 --output_dir=../To_Be_Clean/QQP/output/



