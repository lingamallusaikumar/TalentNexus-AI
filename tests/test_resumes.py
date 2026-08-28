import pytest
import os
from app.resumes.parser import parse_resume_file
from ml.nlp.extractor import clean_text, extract_entities

def test_resume_parser_txt(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "resume.txt"
    p.write_text("This is a software engineer resume. Python and Java.")
    
    text = parse_resume_file(str(p), 'txt')
    assert "software engineer" in text

def test_clean_text():
    raw = "  This   is \n some raw \t text  "
    cleaned = clean_text(raw)
    assert cleaned == "This is some raw text"

def test_extract_entities():
    # Only test if spaCy model actually loaded (it might not be in CI/CD without download)
    import ml.nlp.extractor
    if ml.nlp.extractor.nlp:
        text = "Apple is looking at buying U.K. startup for $1 billion"
        entities = extract_entities(text)
        assert "ORG" in entities
        assert "Apple" in entities["ORG"]
