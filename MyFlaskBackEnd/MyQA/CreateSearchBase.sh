#!/usr/bin/env bash

# set source
export PATH="/anaconda/envs/py36/bin:$PATH"
export CLASSPATH=$CLASSPATH:data/corenlp/*

# temp, export DIR=

# prepare corpus to do QA. Here we prepared a search source.json_path
mkdir -p MyRetrievedData
mkdir -p MyRetrievedData/tmp
mkdir -p MyRetrievedData/tmp/MyCorpusJson
mkdir -p MyRetrievedData/tmp/MyCorpusDataBase
mkdir -p MyRetrievedData/myTFIDF
python retriever/FromPureTextToJsons.py MySegmented MyRetrievedData/tmp/MyCorpusJson
python retriever/build_db.py -data_path MyRetrievedData/tmp/MyCorpusJson -save_path MyRetrievedData/tmp/MyCorpusDataBase/db.db
python retriever/build_tfidf.py MyRetrievedData/tmp/MyCorpusDataBase/db.db MyRetrievedData/myTFIDF
# clean data
rm -rf MyRetrievedData/tmp