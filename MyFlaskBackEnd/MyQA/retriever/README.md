# Document Retriever

## Storing the Documents

- requirements:
numpy
scikit-learn
termcolor
regex
tqdm
prettytable
scipy
nltk
pexpect==4.2.1
- make sure the you have corenlp prepared: you should download it to the root directory: ~/corenlp from https://drive.google.com/open?id=1bcmljJkEacPXRA6qY9NiUXscnBtANCHm

- Note: the encoding for those documents should be UTF-8

- Note: The document should not have duplicate document names, since their names will be treat as keys in a sqlite database.

- 