#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36QA/bin:$PATH"
# alias pip=/anaconda/envs/py36QA/bin/pip
alias anaconda-navigator=/anaconda/bin/anaconda-navigator

# temp, export DIR=
export GLUE_DIR=Data/glue_data
export BERT_BASE_DIR=fine_tuned/BERT_BASE/squad
export SQUAD_DIR=Data/squad
export QES_JSON_DIR=QuestionsAndParagraphs

# now, deal with squad
#
#for d in /home/mozhang/Desktop/GitRepo/MyBERT/ForQA/Data/*.json ;

# for d in "test_cases" ;
#"bee" "beeshort" "imperial_long" "imperial_short" ;

for d in $QES_JSON_DIR/*.json ;
do
  xpath=${d%/*}
  xbase=${d##*/}
  xpref=${xbase%.*}

    python run_squad.py \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR \
  --do_train=False \
  --train_file=$SQUAD_DIR/train-v1.1.json \
  --do_predict=True \
  --predict_file="$d" \
  --train_batch_size=12 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=tmp/squad_predict_output/"$xpref"

done


#zip -r QA.zip asdfsadf
#$SQUAD_DIR/dev-v1.1.json \
#/home/mozhang/Desktop/GitRepo/MyBERT/ForQA/Data/test_cases.json \
#python $SQUAD_DIR/evaluate-v1.1.py $SQUAD_DIR/dev-v1.1.json fine_tuned/BERT_BASE_UNCASED/squad_base/predictions.json