import pytest
from ml.skill_extraction.custom_ner import CustomTechnicalNER

def test_custom_technical_ner_extraction():
    text = "We require strong Python 3.12, Docker, PostgreSQL, and Kubernetes experience. Knowledge of PyTorch is a plus."
    entities = CustomTechnicalNER.extract_entities(text)
    
    extracted_names = [e['text'] for e in entities]
    assert "Python" in extracted_names
    assert "Docker" in extracted_names
    assert "PostgreSQL" in extracted_names
    assert "Kubernetes" in extracted_names
    assert "PyTorch" in extracted_names
