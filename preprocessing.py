import re
from nltk.stem import PorterStemmer

class Preprocessor:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", "", text)
        tokens = text.split()
        return [self.stemmer.stem(token) for token in tokens]
