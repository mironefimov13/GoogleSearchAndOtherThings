import streamlit as st
from icrawler.builtin import GoogleImageCrawler
import nltk
# import translators as ts
from nltk.corpus import wordnet

try:
    from googlesearch import search
    from PyDictionary import PyDictionary
except ImportError: 
    print("No module named 'google' found")

dictionary = PyDictionary()
links = st.text_input("Search Google Links:")
numlinks = st.slider("Number of Links:", 1, 300)
submitlinks = st.button("Submit")

if submitlinks:
    for j in search(links, tld="co.in", num=numlinks, stop=numlinks, pause=2):
        st.write(j)

findsynonyms = st.text_input("Find synonyms for: ")
submits = st.button("Submit ")

if submits:
    synonyms = []
    nltk.download("wordnet")
    for syn in wordnet.synsets(findsynonyms): 
        for l in syn.lemmas(): 
            synonyms.append(l.name())
    synonyms = list(set(synonyms))
    print(synonyms)
    for i in range(len(synonyms)):
        st.write(synonyms[i])
    st.write(dictionary.meaning(findsynonyms))

translate = st.text_input("Translate:")
language = st.selectbox("Which Language?", ["French", "Spanish"])
submittrans = st.button("Submit  ")

if submittrans:
    if language == "French":
        lan = "fr"
    elif language == "Spanish":
        lan = "sp"
    res = ts.deepl(translate, lan)
    st.write(res)
