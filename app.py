import streamlit as st
import spacy
import pandas as pd
nlp_trf = spacy.load("en_core_web_trf") # Spacy model for entities extraction task: en Transformer based model RoBERTa used here. 
def extract_entities(text):
    entities = []
    doc = nlp_trf(text) # doc object to use the model logic
    for ent in doc.ents:
        entity_dict = {'text': ent.text, 'label': ent.label_}
        entities.append(entity_dict)
    return entities

# additional filter to find out dependecy only of extrcated entities
def highlight_entities(tokens, entities):
    highlighted_tokens = []
    for token in tokens:
        for entity in entities:
            if entity['text'] in token[0]:
                highlighted_tokens.append(f"<mark>{token[0]}</mark>")
                break
        else:
            highlighted_tokens.append(token[0])

    return highlighted_tokens


st.set_page_config(page_title="Relational Info extraction", page_icon=":tada:",layout="wide")

# header section 
with st.container():
    st.subheader("Hi, I'm Akshat, Final year student at NIT Warangal and here's my submission for :wave:")
    st.title("Project: Relational Information Extraction Application")
    st.write("[Project Repo >](https://github.com/akshatladdha16/Extraction-of-Relational-Information-from-Text-Using-Transformer-based-NLP-Techniques)")

# entity extraction 
with st.container():
    st.write("---")
    left_column,right_column=st.columns((2,1))
    with left_column:
        st.header("Please enter your text corpus")
        text_input = st.text_area('Enter your text here:', '')
        st.button('Extract Entities')
    with right_column:
        if text_input.strip() == '':
            st.warning('Please enter some text.')
        else:
            # Extract entities function
            entities = extract_entities(text_input)
            if not entities:
                st.warning('No entities found please try some other text corpus')
            else:
                st.write('**Extracted Entities:**')
                for entity in entities:    
                    key = f"{entity['text']}_{entity['label']}"
                    st.markdown(f"<div id='{key}'>{entity['text']} - {entity['label']}</div>", unsafe_allow_html=True)     


# Dependency parsing 
with st.container():
    st.write('---')
    st.header("Relational information btw extracted entities:")
    doc = nlp_trf(text_input)
    dependencies = [(token.text,token.pos_ ,token.dep_, token.head.text) for token in doc ]
    st.write("**Syntactic Dependencies with POS info:**")
    df=pd.DataFrame(dependencies, columns=['Token','Part of Speech','Dependency', 'Head'])
    st.dataframe(df)
    st.write('with these information about grammatical connections btw entites, We can make rules to extract relationship btw entities.')
    st.write('One such example: ')











# def main():
#     # st.title('Extraction of Relational Information from Text using Transformer Based NLP Techniques')
#     text_input = st.text_area('Enter your text here:', '')

#     if st.button('Extract Entities'):
#         if text_input.strip() == '':
#             st.warning('Please enter some text.')
#         else:
#             # Extract entities function
#             entities = extract_entities(text_input)
#             if not entities:
#                 st.warning('No entities found please try some other text corpus')
#             else:
#                 st.write('**Extracted Entities:**')
#                 for entity in entities:
#                     if st.button(entity['text']):
#                         st.write('**Label:**',entity['label'])           

            # Extract relationships
            # Assuming you have the relationships ready, show them here
            # st.write('**Extracted Relationships:**')
            # Your code to display relationships here

    # Add an anchor point for each entity label


# if __name__ == "__main__":
#     main()