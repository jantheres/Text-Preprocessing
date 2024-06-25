import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = input("Enter the Text:")
tokens = word_tokenize(text)
print(tokens)