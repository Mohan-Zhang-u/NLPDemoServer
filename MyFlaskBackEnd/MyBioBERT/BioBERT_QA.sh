export BIOBERT_DIR="Data/pubmed_pmc_470k"
export FINE_TUNE_DIR="fine_tuned/QA"
export PREDICT_FILE="To_Be_Clean/QA/test-v1.1.json"
export OUTPUT_DIR="To_Be_Clean/QA"
python run_qa.py \
    --do_train=False \
    --do_predict=True \
    --vocab_file=$BIOBERT_DIR/vocab.txt \
    --bert_config_file=$BIOBERT_DIR/bert_config.json \
    --init_checkpoint=$FINE_TUNE_DIR/ \
    --max_seq_length=384 \
    --train_batch_size=12 \
    --learning_rate=3e-5 \
    --doc_stride=128 \
    --num_train_epochs=50.0 \
    --do_lower_case=False \
    --predict_file=$PREDICT_FILE \
    --output_dir=$OUTPUT_DIR/
