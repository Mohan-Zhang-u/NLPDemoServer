#!/usr/bin/env bash
#mylines
export PATH="/anaconda/envs/py36/bin:$PATH"
alias anaconda-navigator=/anaconda/bin/anaconda-navigator
export CLASSPATH=$CLASSPATH:data/corenlp/*

rm ../MyCorpus/*
unzip UploadFolder/*.zip -d ../MyCorpus
mkdir -p ../MyRetrievedData
mkdir -p ../MyRetrievedData/tmp
mkdir -p ../MyRetrievedData/tmp/MyCorpusJson
mkdir -p ../MyRetrievedData/tmp/MyCorpusDataBase
mkdir -p ../MyRetrievedData/myTFIDF
python ../FillInRandomFilesIfNeeded.py ../MyCorpus/
python ../retriever/FromPureTextToJsons.py ../MyCorpus ../MyRetrievedData/tmp/MyCorpusJson
python ../retriever/build_db.py ../MyRetrievedData/tmp/MyCorpusJson ../MyRetrievedData/tmp/MyCorpusDataBase/db.db
python ../retriever/build_tfidf.py ../MyRetrievedData/tmp/MyCorpusDataBase/db.db ../MyRetrievedData/myTFIDF
# clean data
rm -rf ../MyRetrievedData/tmp
rm UploadFolder/*
