#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36/bin:$PATH"


task_name="MRPC"
python ../my_run_classifier.py \
 --task_name=mrpc \
 --do_predict=true \
 --data_dir=../To_Be_Clean/MRPC \
 --vocab_file=../fine_tuned/BERT_BASE/vocab.txt \
 --bert_config_file=../fine_tuned/BERT_BASE/bert_config.json \
 --init_checkpoint=../fine_tuned/BERT_BASE/MRPC_output \
 --max_seq_length=128 \
 --output_dir=../To_Be_Clean/MRPC/output/



