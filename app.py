import streamlit as st #used to develop easy UI for our project 
import spacy_streamlit
import spacy 
from spacy import displacy
import pandas as pd
nlp_trf = spacy.load("en_core_web_trf") # Spacy model for entities extraction task: en Transformer based model RoBERTa used here. 

def extract_entities(text):
    entities = []
    doc = nlp_trf(text) # doc object to use the model logic
    for ent in doc.ents:
        entity_dict = {'text': ent.text, 'label': ent.label_}
        entities.append(entity_dict)
    return entities


st.set_page_config(page_title="Relational Info extraction", page_icon=":tada:",layout="wide")

# header section 
with st.container():
    st.subheader("Hi, I'm Akshat :wave:")
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


# Dependency parsing and relational info btw entites 
with st.container():
    st.write('---')
    st.header("Relational information btw extracted entities:")
    doc = nlp_trf(text_input)
    dependencies = [(token.text,token.pos_ ,token.dep_, token.head.text) for token in doc ]
    st.write("**Syntactic Dependencies with POS info:**")
    df=pd.DataFrame(dependencies, columns=['Token','Part of Speech','Dependency', 'Head'])
    st.dataframe(df)

    st.write('with these information about grammatical connections btw entites, We can make rules to extract relationship btw entities.')
    st.write('**Dependency Visualization:**')
    html = spacy_streamlit.visualize_parser(doc)
    st.components.v1.html(f"<div style='width:100%;'>{html}</div>")
    st.write("One Rule Based Relationship extraction is done in [Jupyter Notebook](https://github.com/akshatladdha16/Extraction-of-Relational-Information-from-Text-Using-Transformer-based-NLP-Techniques/blob/main/Relational%20Information%20of%20Extracted%20Entities.ipynb)") 
    st.write("Please do give your feedback.Reach out to me here: [Email](mailto:laddhaakshatrai@gmail.com) ")









