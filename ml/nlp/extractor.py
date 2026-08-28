import spacy
import logging

# We will load a small model by default for extraction
# Ensure you run: python -m spacy download en_core_web_sm
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    logging.warning("spaCy model 'en_core_web_sm' not found. NLP extraction will be limited.")
    nlp = None

def extract_entities(text: str):
    if not nlp:
        return {}
    
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text)
    
    # Deduplicate
    for label in entities:
        entities[label] = list(set(entities[label]))
        
    return entities

def clean_text(text: str) -> str:
    if not text:
        return ""
    # Basic cleanup
    text = " ".join(text.split())
    return text.strip()
