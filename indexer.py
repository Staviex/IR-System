from bptree import BPlusTree
from preprocessing import Preprocessor

class Indexer:
    def __init__(self):
        self.tree = BPlusTree(t=3)
        self.preprocessor = Preprocessor()
        self.N = 0

    def index_documents(self, documents):
        self.N = len(documents)
        for doc_id, doc in documents.items():
            terms = self.preprocessor.preprocess(doc["text"])
            term_freq = {}
            for term in terms:
                term_freq[term] = term_freq.get(term, 0) + 1
            for term, tf in term_freq.items():
                self.tree.insert(term, {doc_id: tf})

    def get_postings(self, term):
        return self.tree.search(term)
