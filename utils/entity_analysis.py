import spacy

# Load small English model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

def extract_entities(article_text: str) -> dict:
    """
    Extracts key entities from the article: people (PERSON), organizations (ORG), locations (GPE).

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - dict: {'PERSON': set, 'ORG': set, 'GPE': set}
    """
    doc = nlp(article_text)
    entities = {"PERSON": set(), "ORG": set(), "GPE": set()}
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].add(ent.text)
    return entities

def generate_entity_prompts(entities: dict) -> list:
    """
    Generates investigation prompts for key entities to guide reader research.

    Parameters:
    - entities (dict): Output from extract_entities()

    Returns:
    - list: Prompts for readers to investigate people, organizations, and locations.
    """
    prompts = []
    for person in entities["PERSON"]:
        prompts.append(f"PERSON: Investigate the author's previous work: {person}")
    for org in entities["ORG"]:
        prompts.append(f"ORG: Look into the funding or history of: {org}")
    for loc in entities["GPE"]:
        prompts.append(f"GPE: Check the context or relevance of the location: {loc}")
    return prompts