Text Processing with Gensim, spaCy, and NLTK
This repository contains scripts that demonstrate basic text processing techniques using different Natural Language Processing (NLP) libraries: gensim, spaCy, and NLTK. The provided scripts cover tasks such as tokenization, stop words removal, stemming, and lemmatization.

This script showcases text processing using spaCy and gensim. It includes:

Tokenization: Breaking down the sample text into individual tokens using spaCy.
Stop Words Removal: Removing common words that do not add significant meaning using both gensim and spaCy.
Stemming: Reducing words to their root form using gensim's Porter Stemmer.
Lemmatization: Converting words to their dictionary form using spaCy.

* You can install them using pip:
pip install gensim spacy nltk
*Download the spaCy model:
python -m spacy download en_core_web_sm

*Run the scripts:
python spacygenism.py
python tokenization.py
python nlp.py
