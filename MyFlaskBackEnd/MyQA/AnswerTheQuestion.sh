#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36/bin:$PATH"
export CLASSPATH=$CLASSPATH:data/corenlp/*

export BERT_BASE_DIR=MyBERT/fine_tuned/BERT_BASE/squad
export QES_JSON_DIR=MyRetrievedData/DocToRead

#change to args!

mkdir -p MyRetrievedData/retrieved
mkdir -p MyRetrievedData/DocToRead
mkdir -p MyAnswers

rm MyRetrievedData/retrieved/retrieved.json

echo "Enter Your Questions:"
read question
question=${question%\?*}
question="$question ?"
# echo $question
# question="latent allocation"


python retriever/RetrieverProcess.py MyRetrievedData/myTFIDF/SearchBase.npz "$question" 3 MyRetrievedData/retrieved/retrieved.json
python retriever/Pipeline.py MySegmented MyRetrievedData/retrieved/retrieved.json MyRetrievedData/DocToRead/DocToRead.json "$question"

for d in $QES_JSON_DIR/*.json ;
do
  xpath=${d%/*}
  xbase=${d##*/}
  xpref=${xbase%.*}

    python MyBERT/run_squad.py \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR \
  --do_train=False \
  --train_file= \
  --do_predict=True \
  --predict_file="$d" \
  --train_batch_size=12 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=MyAnswers/

done

cat MyAnswers/predictions.json