#!/usr/bin/env bash

export PATH="/anaconda/envs/py36/bin:$PATH"

task_name="CoLA"
python ../my_run_classifier.py \
 --task_name=cola \
 --do_predict=true \
 --data_dir=../To_Be_Clean/CoLA \
 --vocab_file=../fine_tuned/BERT_BASE/vocab.txt \
 --bert_config_file=../fine_tuned/BERT_BASE/bert_config.json \
 --init_checkpoint=../fine_tuned/BERT_BASE/CoLA_output \
 --max_seq_length=128 \
 --output_dir=../To_Be_Clean/CoLA/output/



