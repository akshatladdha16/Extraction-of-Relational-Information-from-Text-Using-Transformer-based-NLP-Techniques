import streamlit as st
import spacy
nlp_trf = spacy.load("en_core_web_trf") # Spacy model for entities extraction task: en Transformer based model RoBERTa used here. 
def extract_entities(text):
    entities = []
    doc = nlp_trf(text) # doc object to use the model logic
    for ent in doc.ents:
        entity_dict = {'text': ent.text, 'label': ent.label_}
        entities.append(entity_dict)
    return entities

def main():
    st.title('Extraction of Relational Information from Text using Transformer Based NLP Techniques')
    text_input = st.text_area('Enter your text here:', '')

    if st.button('Extract Entities'):
        if text_input.strip() == '':
            st.warning('Please enter some text.')
        else:
            # Extract entities function
            entities = extract_entities(text_input)
            st.write('**Extracted Entities:**')
            for entity in entities:
                label = entity['label']
                entity_text = entity['text']
                st.markdown(f"[{entity_text}](#{label})")

            # Extract relationships
            # Assuming you have the relationships ready, show them here
            st.write('**Extracted Relationships:**')
            # Your code to display relationships here

    # Add an anchor point for each entity label
    for entity in entities:
        label = entity['label']
        st.markdown(f"<h1 id='{label}'>{label}</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()