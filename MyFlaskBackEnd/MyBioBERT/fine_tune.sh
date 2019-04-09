#!/usr/bin/env bash

export PATH="/anaconda/envs/py36/bin:$PATH"



export BIOBERT_DIR="Data/pubmed_pmc_470k"


# for QA
export BIOASQ_DIR="Data/QA"
export FINE_TUNE_DIR="fine_tuned/QA"

 mkdir -p $FINE_TUNE_DIR/$d
 python run_qa.py \
      --do_train=True \
      --do_predict=True \
      --vocab_file=$BIOBERT_DIR/vocab.txt \
      --bert_config_file=$BIOBERT_DIR/bert_config.json \
      --init_checkpoint=$BIOBERT_DIR/biobert_model.ckpt \
      --max_seq_length=384 \
      --train_batch_size=12 \
      --learning_rate=3e-5 \
      --doc_stride=128 \
      --num_train_epochs=50.0 \
      --do_lower_case=False \
      --train_file=$BIOASQ_DIR/BioASQ-train-4b.json \
      --predict_file=$BIOASQ_DIR/BioASQ-test-4b-1.json \
      --output_dir=$FINE_TUNE_DIR/




# # for RE
# export RE_DIR="Data/REdata/euadr"
# export FINE_TUNE_DIR="fine_tuned/REdata/euadr"
# for d in "1" "2" "3" "4" "5" "6" "7" "8" "9" "10";
# do
# mkdir -p $FINE_TUNE_DIR/$d
# python run_re.py \
#     --task_name=euadr \
#     --do_train=true \
#     --do_eval=true \
#     --do_predict=true \
#     --vocab_file=$BIOBERT_DIR/vocab.txt \
#     --bert_config_file=$BIOBERT_DIR/bert_config.json \
#     --init_checkpoint=$BIOBERT_DIR/biobert_model.ckpt \
#     --max_seq_length=128 \
#     --train_batch_size=32 \
#     --learning_rate=2e-5 \
#     --num_train_epochs=3.0 \
#     --do_lower_case=false \
#     --data_dir=$RE_DIR/$d/ \
#     --output_dir=$FINE_TUNE_DIR/$d/
# done

# export RE_DIR="Data/REdata/GAD"
# export FINE_TUNE_DIR="fine_tuned/REdata/GAD"
# for d in "1" "2" "3" "4" "5" "6" "7" "8" "9" "10";
# do
# mkdir -p $FINE_TUNE_DIR/$d
# python run_re.py \
#     --task_name=euadr \
#     --do_train=true \
#     --do_eval=true \
#     --do_predict=true \
#     --vocab_file=$BIOBERT_DIR/vocab.txt \
#     --bert_config_file=$BIOBERT_DIR/bert_config.json \
#     --init_checkpoint=$BIOBERT_DIR/biobert_model.ckpt \
#     --max_seq_length=128 \
#     --train_batch_size=32 \
#     --learning_rate=2e-5 \
#     --num_train_epochs=3.0 \
#     --do_lower_case=false \
#     --data_dir=$RE_DIR/$d/ \
#     --output_dir=$FINE_TUNE_DIR/$d/
# done


# for NER
export NER_DIR="Data/NERdata"
export FINE_TUNE_DIR="fine_tuned/NERdata"
for d in  "BC5CDR-chem" "BC5CDR-disease" "JNLPBA" "linnaeus" "NCBI-disease" "s800"; # "BC2GM" "BC4CHEMD"
do
    mkdir -p $FINE_TUNE_DIR/$d
    python run_ner.py \
    --do_train=true \
    --do_eval=true \
    --vocab_file=$BIOBERT_DIR/vocab.txt \
    --bert_config_file=$BIOBERT_DIR/bert_config.json \
    --init_checkpoint=$BIOBERT_DIR/biobert_model.ckpt \
    --num_train_epochs=10.0 \
    --data_dir=$NER_DIR/$d/ \
    --output_dir=$FINE_TUNE_DIR/$d/
done

