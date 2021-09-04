import numpy as np
import pandas as pd
import re
import nltk
import spacy
import string
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from extract_text import train_resumes, test_resumes

train_resumes_lower = []
for resume in train_resumes:
    train_resumes_lower.append(resume.lower())

test_resumes_lower = []
for resume in test_resumes:
    test_resumes_lower.append(resume.lower())

PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

train_punc_removed = []
for resume in train_resumes_lower:
    punc_removed = remove_punctuation(resume)
    train_punc_removed.append(punc_removed)

test_punc_removed = []
for resume in test_resumes_lower:
    punc_removed = remove_punctuation(resume)
    test_punc_removed.append(punc_removed)

STOPWORDS = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

train_stopwords_removed = []
for resume in train_punc_removed:
    stopwords_removed = remove_stopwords(resume)
    train_stopwords_removed.append(stopwords_removed)

test_stopwords_removed = []
for resume in test_punc_removed:
    stopwords_removed = remove_stopwords(resume)
    test_stopwords_removed.append(stopwords_removed)

lemmatizer = WordNetLemmatizer()
wordnet_map = {"N":wordnet.NOUN, "V":wordnet.VERB, "J":wordnet.ADJ, "R":wordnet.ADV}
def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

train_lemma = []
for resume in train_stopwords_removed:
    lemma = lemmatize_words(resume)
    train_lemma.append(lemma)

test_lemma = []
for resume in test_stopwords_removed:
    lemma = lemmatize_words(resume)
    test_lemma.append(lemma)


print(train_punc_removed[0])
print('===========')
print(test_punc_removed[0])
print('\n')
print('\n')
print(train_stopwords_removed[0])
print('===========')
print(test_stopwords_removed[0])
print('\n')
print('\n')
print(train_lemma[0])
print('===========')
print(test_lemma[0])
