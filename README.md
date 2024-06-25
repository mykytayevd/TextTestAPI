# Text Processing API with NLTK and FastAPI

This project implements a REST API using FastAPI for text processing tasks with NLTK (Natural Language Toolkit). The API provides endpoints for tokenization, part-of-speech tagging (POS tagging), and named entity recognition (NER).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mykytayevd/TextTestAPI.git
```

2. Set up a virtual environment:

```bash
python -m venv venv
```
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app. Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

## Usage

##### There are 3 endpoints to use: /tokenize, /pos_tag, /ner.
You can use Postman or Curl to perform requests.
All of them expect POST request with JSON: ``
{
"text": "Any random text"
}
``
There is example of usage via curl:
```bash
curl -X POST http://127.0.0.1:8000/tokenize -H "Content-Type: application/json" -d '{"text": "Your text here"}'
```
