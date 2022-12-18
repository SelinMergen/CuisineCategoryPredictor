import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

st.title('Recipe Classifier')

with open("ingredients.json", 'r') as fp:
    ingredients_list = json.load(fp)

ingredients = st.multiselect(
    'Add the ingredients to classify',
    ingredients_list, ['salt', 'pepper'])

# st.write('You selected:', options)

text = str(ingredients).replace('\', \'', ' ').replace('[\'', '').replace('\']', '').lower()

with open('./pickles/tfidf_cuisine.pickle','rb') as read_file1:
    tfidf_cuisine = pickle.load(read_file1)
with open('./pickles/le_cuisine.pickle','rb') as read_file2:
    lb_cuisine = pickle.load(read_file2)
with open('./pickles/model_cuisine.pickle','rb') as read_file3:
    model_cuisine = pickle.load(read_file3)
with open('./pickles/tfidf_category.pickle','rb') as read_file4:
    tfidf_category = pickle.load(read_file4)
with open('./pickles/le_category.pickle','rb') as read_file5:
    le_category = pickle.load(read_file5)
with open('./pickles/model_category.pickle','rb') as read_file6:
    model_category = pickle.load(read_file6)

X_cuisine = tfidf_cuisine.transform( [text] ).astype('float16')
X_category = tfidf_category.transform( [text] ).astype('float16')

pred_cuisine = model_cuisine.predict(X_cuisine)
pred_cuisine = lb_cuisine.inverse_transform(pred_cuisine)

pred_category = model_category.predict(X_category)
pred_category = le_category.inverse_transform(pred_category)

if (len(ingredients) != 0):
    st.write( 'Cousine: ' + pred_cuisine[0])
    st.write( 'Category: ' + pred_category[0])