
import streamlit as st
from threading import activeCount
import matplotlib.pyplot as plt
#import umap
import io
import numpy as np
import pandas as pd
from scipy.spatial import distance



st.title("App")

uploaded_file = st.file_uploader("Enter G25 co-ordinates")
if uploaded_file is not None:
     input = pd.read_csv(uploaded_file)
     st.write(input)

Tools = st.selectbox("Choose your Tool", ['Euclidean','braycurtis','canberra','chebyshev']) 

dfnext25 = input.iloc[:,1:]

#dfnext25=input.drop(columns=input.columns[0], axis=1, inplace=True)

st.dataframe(dfnext25)

if Tools == "Euclidean":
  #euclidean
  deuclidean=distance.cdist(dfnext25,dfnext25, metric='euclidean')
  dmateuclidean=pd.DataFrame(deuclidean)
  st.dataframe(dmateuclidean)

elif Tools == "braycurtis":
  #braycurtis
  dbraycurtis=distance.cdist(dfnext25,dfnext25, metric='braycurtis')
  dmatbraycurtis=pd.DataFrame(dbraycurtis)
  st.dataframe(dmatbraycurtis)

elif Tools == "canberra":
  #canberra
  dcanberra=distance.cdist(dfnext25,dfnext25, metric='canberra')
  dmatcanberra=pd.DataFrame(dcanberra)
  st.dataframe(dmatcanberra)

elif Tools == "chebyshev":
  #chebyshev
  dchebyshev=distance.cdist(dfnext25,dfnext25, metric='chebyshev')
  dmatchebyshev=pd.DataFrame(dchebyshev)
  st.dataframe(dmatchebyshev)
