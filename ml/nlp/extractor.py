import logging

nlp = None
try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
except (ImportError, OSError):
    logging.warning("spaCy not available. NLP extraction will be limited.")

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
