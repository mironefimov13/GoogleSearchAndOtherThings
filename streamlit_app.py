import streamlit as st
from icrawler.builtin import GoogleImageCrawler
import nltk
from nltk.corpus import wordnet

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

links = st.text_input("Search Google Links:")
numlinks = st.slider("Number of Links:", 1, 300)
submitlinks = st.button("Submit Links")

if submitlinks:
    for j in search(links, tld="co.in", num=numlinks, stop=numlinks, pause=2):
        st.write(j)

findsynonyms = st.text_input("Find synonyms for: ")
submits = st.button("Submit")

if submits:
    synonyms = []
    for syn in wordnet.synsets(findsynonyms): 
        for l in syn.lemmas(): 
            synonyms.append(l.name())
    synonyms = list(set(synonyms))
    for i in range(len(synonyms)):
        st.write(synonyms[i])