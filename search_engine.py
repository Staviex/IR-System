import math

class SearchEngine:
    def __init__(self, indexer):
        self.indexer = indexer

    def tf_idf_score(self, term, doc_id):
        postings = self.indexer.get_postings(term)
        if postings is None or doc_id not in postings:
            return 0.0
        tf = postings[doc_id]
        df = len(postings)
        N = self.indexer.N
        idf = math.log((N + 1) / (df + 1)) + 1
        return tf * idf

    def search(self, query):
        terms = self.indexer.preprocessor.preprocess(query)
        scores = {}
        for term in terms:
            postings = self.indexer.get_postings(term)
            if postings:
                for doc_id in postings:
                    scores[doc_id] = self.tf_idf_score(term, doc_id)
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:3]
