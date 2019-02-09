#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36/bin:$PATH"


task_name="QNLI"
python ../my_run_classifier.py \
 --task_name=qnli \
 --do_predict=true \
 --data_dir=../To_Be_Clean/QNLI \
 --vocab_file=../fine_tuned/BERT_BASE/vocab.txt \
 --bert_config_file=../fine_tuned/BERT_BASE/bert_config.json \
 --init_checkpoint=../fine_tuned/BERT_BASE/QNLI_output \
 --max_seq_length=128 \
 --output_dir=../To_Be_Clean/QNLI/output/



