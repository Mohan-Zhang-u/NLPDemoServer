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

#python my_run_classifier.py \
#  --task_name=MRPC \
#  --do_train=true \
#  --do_eval=true \
#  --data_dir=$GLUE_DIR/MRPC \
#  --vocab_file=$BERT_BASE_DIR/vocab.txt \
#  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
#  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
#  --max_seq_length=128 \
#  --train_batch_size=32 \
#  --learning_rate=2e-5 \
#  --num_train_epochs=3.0 \
#  --output_dir=tmp/mrpc_output/

task_name="QQP"
export TRAINED_CLASSIFIER=fine_tuned/BERT_BASE_UNCASED/"$task_name"_output

python my_run_classifier.py \
  --task_name=$task_name \
  --do_predict=true \
  --data_dir=$GLUE_DIR/$task_name \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=128 \
  --output_dir=tmp/"$task_name"_predict_output/

#
#for task_name in  "QNLI" "SNLI" "WNLI"; # already: "CoLA" "MNLI" "MRPC" not: "QQP" "RTE" "SST-2" "STS-B"
#do
#    python my_run_classifier.py \
#  --task_name=xnli \
#  --do_train=true \
#  --do_eval=true \
#  --data_dir=$GLUE_DIR/$task_name \
#  --vocab_file=$BERT_BASE_DIR/vocab.txt \
#  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
#  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
#  --max_seq_length=128 \
#  --train_batch_size=32 \
#  --learning_rate=2e-5 \
#  --num_train_epochs=3.0 \
#  --output_dir=fine_tuned/BERT_BASE_UNCASED/"$task_name"_output/
#done


