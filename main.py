from fastapi import FastAPI, HTTPException
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from models.requests import TextRequest


app = FastAPI()

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

try:
    nltk.data.find('chunkers/maxent_ne_chunker')
except LookupError:
    nltk.download('maxent_ne_chunker')

try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')


@app.post("/tokenize")
async def tokenize(request: TextRequest):
    try:
        tokens = word_tokenize(request.text)
        return {"tokens": tokens}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/pos_tag")
async def pos_tagging(request: TextRequest):
    try:
        tokens = word_tokenize(request.text)
        pos_tags = pos_tag(tokens)
        return {"pos_tags": pos_tags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ner")
async def ner(request: TextRequest):
    try:
        tokens = word_tokenize(request.text)
        pos_tags = pos_tag(tokens)
        named_entities = ne_chunk(pos_tags)
        entities = []
        for chunk in named_entities:
            if hasattr(chunk, 'label'):
                entity = " ".join(c[0] for c in chunk)
                entity_type = chunk.label()
                entities.append({"entity": entity, "type": entity_type})
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
