import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import streamlit as st 


uploaded_file =r"data\tips.csv"
data=pd.read_csv(uploaded_file)

st.title("Tips Data Dashboard")
st.header("Data Overview")
st.write("First few rows of the dataset")
st.dataframe(data.head())

st.header("Summary Statics")
st.dataframe(data.describe())

st.header("Data Visulation")
st.write("Select column Visulation")
x_axis=st.selectbox("X axis ", data.columns)
y_axis=st.selectbox("Y axis ", data.columns)
plot_Type=st.radio("Select Plot Type :",["Scatter plot","Line plot","Histogram plot"])

if plot_Type == "Scatter plot" :
    fig=plt.figure()
    sns.scatterplot(x=x_axis,y=y_axis,data=data)    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_Type == "Line plot" :
    fig=plt.figure()
    sns.lineplot(x=x_axis,y=y_axis,data=data)    
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_Type == "Histogram plot" :
    fig=plt.figure()
    sns.histplot(x=x_axis,data=data)    
    plt.xlabel(x_axis)
    st.pyplot(fig)
st.header("Correction Heatmap")
if st.button("Generate Heatmap") :
    fig=plt.figure()
    sns.heatmap(data.corr(numeric_only=True),annot=True,cmap="Blues")
    st.pyplot(fig)