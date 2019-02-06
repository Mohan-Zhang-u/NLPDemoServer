#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36/bin:$PATH"
# alias pip=/anaconda/envs/py36/bin/pip
alias anaconda-navigator=/anaconda/bin/anaconda-navigator

# temp, export DIR=
export GLUE_DIR=Data/glue_data
export BERT_BASE_DIR=Data/BERT_BASE_UNCASED
export BERT_LARGE_DIR=Data/BERT_LARGE_UNCASED
export SQUAD_DIR=Data/squad2

python run_squad.py \
 --vocab_file=$BERT_BASE_DIR/vocab.txt \
 --bert_config_file=$BERT_BASE_DIR/bert_config.json \
 --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
 --do_train=True \
 --train_file=$SQUAD_DIR/train-v2.0.json \
 --do_predict=True \
 --predict_file=$SQUAD_DIR/dev-v2.0.json \
 --train_batch_size=24 \
 --learning_rate=3e-5 \
 --num_train_epochs=2.0 \
 --max_seq_length=384 \
 --doc_stride=128 \
 --output_dir=fine_tuned/BERT_BASE/squad2/ \
 --version_2_with_negative=True

# python run_squad.py \
#   --vocab_file=$BERT_LARGE_DIR/vocab.txt \
#   --bert_config_file=$BERT_LARGE_DIR/bert_config.json \
#   --init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
#   --do_train=True \
#   --train_file=$SQUAD_DIR/train-v1.1.json \
#   --do_predict=True \
#   --predict_file=$SQUAD_DIR/dev-v1.1.json \
#   --train_batch_size=12 \
#   --learning_rate=3e-5 \
#   --num_train_epochs=2.0 \
#   --max_seq_length=384 \
#   --doc_stride=128 \
#   --output_dir=fine_tuned/BERT_LARGE/squad/