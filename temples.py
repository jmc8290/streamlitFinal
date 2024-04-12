import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

st.title('Latter-Day Saint Temples')

st.set_option('deprecation.showPyplotGlobalUse', False)

url = 'https://raw.githubusercontent.com/jmc8290/streamlitFinal/main/templeDimensionElevation.csv'
#df = pd.read_csv('templeDimensionElevation.csv')
df = pd.read_csv(url)

col1, col2 = st.columns(2)
with col1:
    varX = st.radio(
        "Select a Variable for the X-Axis",
        ["Instruction Rooms", "Sealing Rooms", "Baptismal Fonts", "Square Footage", "Acreage", "Elevation"],
        captions = ["Number of", "Number of", "Number of", "ft^2", "acre", "ft"])
with col2:
    varY = st.radio(
        "Select a Different Variable for the Y-Axis",
        ["Instruction Rooms", "Sealing Rooms", "Baptismal Fonts", "Square Footage", "Acreage", "Elevation"],
        captions = ["Number of", "Number of", "Number of", "ft^2", "acre", "ft"])

if varX == "Instruction Rooms":
    if varY == "Sealing Rooms":
        plot = sb.lmplot(df, x = 'Instruction Rooms', y = 'Sealing Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot(plot)
    elif varY == "Baptismal Fonts":
        sb.lmplot(df, x = 'Instruction Rooms', y = 'Baptismal Fonts', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.05, fit_reg = False)
        st.pyplot()
    elif varY == "Square Footage":
        sb.boxplot(df, x = 'Instruction Rooms', y = 'Square Footage', hue = 'Instruction Rooms', palette = 'Set2')
        st.pyplot()
    elif varY == "Acreage":
        sb.boxplot(df, x = 'Instruction Rooms', y = 'Acreage', hue = 'Instruction Rooms', palette = 'Set2')
        st.pyplot()
    elif varY == "Elevation":
        sb.boxplot(df, x = 'Instruction Rooms', y = 'Elevation (Feet)', hue = 'Instruction Rooms', palette = 'Set2')
        st.pyplot()


with st.sidebar:
    location = st.text_input('Enter a location to pull up its data', value='Arizona')
    locationDf = df[df['Temple'].str.contains(location)]
    
    locationDf['Temple'] = locationDf['Temple'].str.replace(location, '')
    
    locationDf = locationDf.drop(locationDf.columns[0], axis=1)
    locationDf = locationDf.set_index('Temple')
    st.dataframe(locationDf)
    
   