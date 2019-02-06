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

# now, deal with squad
#
#for d in /home/mozhang/Desktop/GitRepo/MyBERT/ForQA/Data/*.json ;

for d in "test_cases" ;
#"bee" "beeshort" "imperial_long" "imperial_short" ;
do
    python my_run_squad.py \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=fine_tuned/BERT_BASE_UNCASED/squad_base \
  --do_train=False \
  --train_file=$SQUAD_DIR/train-v1.1.json \
  --do_predict=True \
  --predict_file=/home/mozhang/Desktop/GitRepo/MyBERT/ForQA/Data/"$d".json \
  --train_batch_size=12 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=tmp/squad_predict_output_"$d"

done


#zip -r QA.zip asdfsadf
#$SQUAD_DIR/dev-v1.1.json \
#/home/mozhang/Desktop/GitRepo/MyBERT/ForQA/Data/test_cases.json \
#python $SQUAD_DIR/evaluate-v1.1.py $SQUAD_DIR/dev-v1.1.json fine_tuned/BERT_BASE_UNCASED/squad_base/predictions.json