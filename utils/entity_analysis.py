import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(article_text: str) -> dict:
    doc = nlp(article_text)
    entities = {"PERSON": set(), "ORG": set(), "GPE": set()}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].add(ent.text)
    return entities

def generate_entity_prompts(entities: dict) -> list:
    prompts = []
    for person in entities["PERSON"]:
        prompts.append(f"Investigate the author's previous work: {person}")
    for org in entities["ORG"]:
        prompts.append(f"Look into the funding or history of: {org}")
    for loc in entities["GPE"]:
        prompts.append(f"Check the context or relevance of the location: {loc}")
    return prompts