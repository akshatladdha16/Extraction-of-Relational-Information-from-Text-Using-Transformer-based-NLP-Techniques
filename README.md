# Extraction-of-Relational-Information-from-Text-Using-Transformer-based-NLP-Techniques
To identify relational information using transformer-based NLP techniques. Relationship to be identified in extracted entities from the text corpus.
1. Phase 1: Entites Extraction : Ways to do this: ->Generalised Way(Used Pre-trained models like Spacy), Specific Task(Fine tunign of model with our data), Specific_easy( Model Stacking )
2. Phase 2: Relational information of extracted entities (Dependency Parsing Concept -> Rule based matching(specific rules for labels))
3. Phase 3: Build UI to take input of text corpus and showcase model visualizations.(Streamlit Web App)

### Model Information:
1. Spacy en transformer based model for entity and relation extraction:
Used coz contains more labels than other models and can be fine tuned on any other dataset for specific tasks. 
RoBERTa model is used here(tokenization accuracy of 100% and Part of Speech Tags accuracy 98%) and working fine for multi sentence text corpus. Labels available: CARDINAL(Numerals that do not fall under another type), DATE, EVENT(Named hurricanes, battles, wars, sports events, etc.), FAC(Buildings, airports, highways, bridges, etc.), GPE, LANGUAGE, LAW(Named documents made into laws), LOC, MONEY, NORP(Nationalities or religious or political groups), ORDINAL(First, second, third etc.), ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART(Nobel prize etc.). Here's the link to model: https://spacy.io/models/en#en_core_web_trf 
2. Another way of entity extration can be done by Model Stacking concept where we combine results from different models and extract entities. Tried that out and good for specific tasks. 

### Dependency Parsing 
For explicit relationship, we can identify relational information between entities directly just by mapping it with each other but for implicit relationship we need to understand the grammatical formation btw entities . So using Spacy dependency parsing concept here. More info here : https://towardsdatascience.com/natural-language-processing-dependency-parsing-cf094bbbe3f7 
