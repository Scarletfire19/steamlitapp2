
import streamlit as st
from threading import activeCount
import matplotlib.pyplot as plt
#import umap
import io
import numpy as np
import pandas as pd
from scipy.spatial import distance
import seaborn as sns
from matplotlib import pyplot as plt



st.title("App")

uploaded_file = st.file_uploader("Enter G25 co-ordinates")
if uploaded_file is not None:
     input = pd.read_csv(uploaded_file)
     st.write(input)

Tools = st.selectbox("Choose your Tool", ['Euclidean','braycurtis','canberra','chebyshev']) 

#dfcurrentgroup=input.groupby(['DNA sample ethnicity']).mean().reset_index()

#a1=input.columns[1]
a1=input.iloc[:,2]
st.dataframe(a1)

dfnext25 = input.iloc[:,1:]

#dfnext25=input.drop(columns=input.columns[0], axis=1, inplace=True)

st.dataframe(dfnext25)

if Tools == "Euclidean":
  #euclidean
  deuclidean=distance.cdist(dfnext25,dfnext25, metric='euclidean')
  dmateuclidean=pd.DataFrame(deuclidean)
  st.dataframe(dmateuclidean)
  fig1=sns.clustermap(dmateuclidean,figsize=(20, 30))
  st.pyplot(fig1)

elif Tools == "braycurtis":
  #braycurtis
  dbraycurtis=distance.cdist(dfnext25,dfnext25, metric='braycurtis')
  dmatbraycurtis=pd.DataFrame(dbraycurtis)
  st.dataframe(dmatbraycurtis)
  st.dataframe(dmatbraycurtis)
  fig2=sns.clustermap(dmatbraycurtis,figsize=(20, 30))
  st.pyplot(fig2)

elif Tools == "canberra":
  #canberra
  dcanberra=distance.cdist(dfnext25,dfnext25, metric='canberra')
  dmatcanberra=pd.DataFrame(dcanberra)
  st.dataframe(dmatcanberra)
  fig3=sns.clustermap(dmatcanberra,figsize=(20, 30))
  st.pyplot(fig3)

elif Tools == "chebyshev":
  #chebyshev
  dchebyshev=distance.cdist(dfnext25,dfnext25, metric='chebyshev')
  dmatchebyshev=pd.DataFrame(dchebyshev)
  st.dataframe(dmatchebyshev)
  fig4=sns.clustermap(dmatchebyshev,figsize=(20, 30))
  st.pyplot(fig4)

     
Settools = st.selectbox("Choose your Tool", ['Dice','Hamming']) 

if Settools == "Dice":
     pdice = np.zeros((len(input),len(input)))
     for i in range(len(input)):
          for j in range(len(input)):
               pdice[i][j]=distance.dice(input.loc[[j]],input.loc[[i]])          
     distmatdice=pd.DataFrame(pdice)
     st.dataframe(distmatdice)
     fig11=sns.clustermap(distmatdice,figsize=(20, 30))
     st.pyplot(fig11)
     
     
elif Settools == "Hamming":
     phamming=np.zeros((len(input),len(input)))
     for i in range(len(input)):
          for j in range(len(input)):
               phamming[i][j]=distance.hamming(input.loc[[j]],input.loc[[i]])
     distmathamming=pd.DataFrame(phamming)
     st.dataframe(distmathamming)
     
     fig12=sns.clustermap(distmathamming,figsize=(20, 30))
     st.pyplot(fig12)
