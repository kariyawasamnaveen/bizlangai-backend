import spacy

nlp = spacy.load("en_core_web_sm")

def detect_query_type(prompt: str) -> str:
    doc = nlp(prompt)
    for ent in doc.ents:
        if ent.label_ in ["DATE", "ORG", "GPE", "CARDINAL"]:
            return "file_analysis"
    return "general"
