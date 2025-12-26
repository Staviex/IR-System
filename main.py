from document_loader import DocumentLoader
from indexer import Indexer
from search_engine import SearchEngine

def main():
    loader = DocumentLoader("documents")
    documents = loader.load_documents()
    indexer = Indexer()
    indexer.index_documents(documents)
    searcher = SearchEngine(indexer)

    while True:
        query = input("Enter single-word query (or 'exit'): ").strip().lower()
        if query == "exit":
            break
        results = searcher.search(query)
        if not results:
            print("No results found.")
        else:
            print("Top results:")
            for rank, (doc_id, score) in enumerate(results, start=1):
                print(f"{rank}. {documents[doc_id]['name']} → score: {score:.3f}")

if __name__ == "__main__":
    main()
