# IRSystem

A simple Information Retrieval system supporting TXT and DOCX files, using a B+ Tree and TF-IDF ranking.  
This project can process single-word queries and display the top 3 relevant documents.

## Requirements

- Python 3.8 or higher
- Python libraries:
  - `python-docx`
  - `nltk`

## Installing Libraries

It is recommended to create a virtual environment first:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

Then install the required libraries:
pip install -r requirements.txt
