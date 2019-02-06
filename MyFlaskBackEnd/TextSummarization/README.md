# Please be aware: the Text Summarization Demo is now limiting access.
# Text Summarization Tool
This repository is based on the ACL 2018 paper:

*[Fast Abstractive Summarization with Reinforce-Selected Sentence Rewriting](https://arxiv.org/abs/1805.11080)*.

## Dependencies
- **Python 3** (tested both on 3.6 and 3.7)
- Java runtime environment (JRE 8 will work)
- [PyTorch](https://github.com/pytorch/pytorch) (tested both on 0.4.0 and 0.4.1 with cuda 8.0 or 9.0)
- [gensim](https://github.com/RaRe-Technologies/gensim)
- [cytoolz](https://github.com/pytoolz/cytoolz)
- [tensorboardX](https://github.com/lanpa/tensorboard-pytorch)
- [nltk](https://www.nltk.org/)
- [pyrouge](https://github.com/bheinzerling/pyrouge) (for evaluation)

You can use the python package manager of your choice (*pip/conda*) to install the dependencies.
The code is tested on the *Linux* operating system.

## How to run the server's backend
- make sure you have both pretrained models *[here](https://bit.ly/acl18_pretrained)* and Stanford CoreNLP *[here](https://stanfordnlp.github.io/CoreNLP/)* in your directory.
(make sure you've copied all the .jar file into the directory stanford-corenlp-full-\<version you choose\>)
- make sure you have nltk tokenized installed (in python environment, type 
```>>> import nltk ```
```>>> nltk.download('punkt')```)
- create a subfolder under To_Be_Clean/$name_of_your_choice$/my_news
- put all the articles you want to summarize (must be in plain text format and contains only unicode characters) in the To_Be_Clean/$name_of_your_choice$/my_news directory.

- run the python script bash_script_executer.py ```python bash_script_executer.py $name_of_your_choice$```, the summarizations of my_news shall be generated in the directory To_Be_Clean/$name_of_your_choice$/summarizations/output
<!--- 
- run the run.sh script (type ./run.sh $name_of_your_choice$ in bash commandline under this directory), which will execute a series of command and python files to generate the summaries.
- after running the script, summarizations of my_news shall be generated in the directory To_Be_Clean/$name_of_your_choice$/summarizations/output
- if you want to run it again to generate new summaries, please make sure to execute clean.sh (by type ./clean.sh in bash commandline under this directory) to clean up previously-generated summaries and temp files.
-->
- also, there's already a python file provided for you to separate a large file into smaller files to achieve better summarziation performance.
run ```python separate_large_files.py --target_file_location=[path/to/target's parent directory] --target_file_name=[target file's name] --storage_location=[(optional) path/to/storage/location] --num_of_sent=[(optional) number of paragraphs per article]```

## How to run the server
## Dependencies
- apache2 with cgi tookit
- you can install by running ``` sudo apt-get install libexpat1 apache2-utils ssl-cert -y ``` and ``` sudo apt-get install libapache2-mod-wsgi -y ```
- make sure apache2 server is running and cgi-scripts are enabled. You may find this [tutorial](https://code-maven.com/set-up-cgi-with-apache) helpful: 
- make sure you server can be accessed with a public IP address and port 5000 is enabled.
- run ``` ./Server/flaskrun.sh ```, the feedback shoudl be sometime like ```* Debug mode: on * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) * Restarting with stat * Debugger is active! * Debugger PIN: XXX-XXX-XXX```
- you should be able to access the up-and-running server through internally ```0.0.0.0:5000``` or externally ```Public.IP.Address:5000```
- all use cases and codes are under Apache 2.0 License

## Train your own models

1. pretrained a *word2vec* word embedding
```
python train_word2vec.py --path=[path/to/word2vec]
```
2. make the pseudo-labels
```
python make_extraction_labels.py
```
3. train *abstractor* and *extractor* using ML objectives
```
python train_abstractor.py --path=[path/to/abstractor/model] --w2v=[path/to/word2vec/word2vec.128d.226k.bin]
python train_extractor_ml.py --path=[path/to/extractor/model] --w2v=[path/to/word2vec/word2vec.128d.226k.bin]
```
4. train the *full RL model*
```
python train_full_rl.py --path=[path/to/save/model] --abs_dir=[path/to/abstractor/model] --ext_dir=[path/to/extractor/model]
```
After the training finishes you will be able to run the decoding as described above.
The above will use the best hyper-parameters as default.
Please refer to the respective source code for options to set the hyper-parameters.

