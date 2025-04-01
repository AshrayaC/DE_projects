import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("SpaCy installation is successful!")

# Print the processed tokens
for token in doc:
    print(token.text)

## Process a text for NER
doc = nlp("Apple is looking to buy a startup in the UK for $1 billion.")

# Print named entities found in the text
for ent in doc.ents:
    print(ent.text, ent.label_)
