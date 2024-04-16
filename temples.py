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


if varX == "Sealing Rooms":
    if varY == "Instruction Rooms":
        plot = sb.lmplot(df, x = 'Sealing Rooms', y = 'Instruction Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot(plot)
    elif varY == "Baptismal Fonts":
        sb.lmplot(df, x = 'Sealing Rooms', y = 'Baptismal Fonts', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.05, fit_reg = False)
        st.pyplot()
    elif varY == "Square Footage":
        sb.lmplot(df, x = 'Sealing Rooms', y = 'Square Footage', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()
    elif varY == "Acreage":
        sb.lmplot(df, x = 'Sealing Rooms', y = 'Acreage', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()
    elif varY == "Elevation":
        sb.lmplot(df, x = 'Sealing Rooms', y = 'Elevation (Feet)', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()

if varX == "Baptismal Fonts":
    if varY == "Instruction Rooms":
        sb.boxplot(df, x = 'Baptismal Fonts', y = 'Instruction Rooms', hue = 'Baptismal Fonts', palette = 'Set2')
        st.pyplot()
    elif varY == "Sealing Rooms":
        sb.boxplot(df, x = 'Baptismal Fonts', y = 'Sealing Rooms', hue = 'Baptismal Fonts', palette = 'Set2')
        st.pyplot()
    elif varY == "Square Footage":
        sb.boxplot(df, x = 'Baptismal Fonts', y = 'Square Footage', hue = 'Baptismal Fonts', palette = 'Set2')
        st.pyplot()
    elif varY == "Acreage":
        sb.boxplot(df, x = 'Baptismal Fonts', y = 'Acreage', hue = 'Baptismal Fonts', palette = 'Set2')
        st.pyplot()
    elif varY == "Elevation":
        sb.boxplot(df, x = 'Baptismal Fonts', y = 'Elevation (Feet)', hue = 'Baptismal Fonts', palette = 'Set2')
        st.pyplot()

if varX == "Square Footage":
    if varY == "Instruction Rooms":
        plot = sb.lmplot(df, x = 'Square Footage', y = 'Instruction Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot(plot)
    elif varY == "Baptismal Fonts":
        sb.lmplot(df, x = 'Square Footage', y = 'Baptismal Fonts', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.1, fit_reg = False)
        st.pyplot()
    elif varY == "Sealing Rooms":
        sb.lmplot(df, x = 'Square Footage', y = 'Sealing Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()
    elif varY == "Acreage":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Square Footage', y = 'Acreage', hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'})
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')
    elif varY == "Elevation":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Square Footage', y = 'Elevation (Feet)',hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'})
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')

if varX == "Acreage":
    if varY == "Instruction Rooms":
        plot = sb.lmplot(df, x = 'Acreage', y = 'Instruction Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot(plot)
    elif varY == "Baptismal Fonts":
        sb.lmplot(df, x = 'Acreage', y = 'Baptismal Fonts', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.1, fit_reg = False)
        st.pyplot()
    elif varY == "Sealing Rooms":
        sb.lmplot(df, x = 'Acreage', y = 'Sealing Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()
    elif varY == "Square Footage":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Acreage', y = 'Square Footage',hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'})
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')
    elif varY == "Elevation":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Acreage', y = 'Elevation (Feet)',hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'})
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')

if varX == "Elevation":
    if varY == "Instruction Rooms":
        plot = sb.lmplot(df, x = 'Elevation (Feet)', y = 'Instruction Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot(plot)
    elif varY == "Baptismal Fonts":
        sb.lmplot(df, x = 'Elevation (Feet)', y = 'Baptismal Fonts', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.1, fit_reg = False)
        st.pyplot()
    elif varY == "Sealing Rooms":
        sb.lmplot(df, x = 'Elevation (Feet)', y = 'Sealing Rooms', scatter_kws={"s": 10, "alpha": 0.5}, x_jitter = 0.3, y_jitter = 0.5)
        st.pyplot()
    elif varY == "Square Footage":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Elevation (Feet)', y = 'Square Footage',hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'} )
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')
    elif varY == "Acreage":
        location1 = st.text_input('Enter a location to highlight its temples', value='Arizona')
        df['temp'] = df['Temple'].str.contains(location1)
        hoverTemple = {col: True if col == 'Temple' else False for col in df.columns}
        
        fig = px.scatter(df, x = 'Elevation (Feet)', y = 'Acreage',hover_data= hoverTemple, color = 'temp', color_discrete_map={0: 'blue', 1: 'red'})
        st.plotly_chart(fig)
        
        df = df.drop(columns = 'temp')

with st.sidebar:
    option = st.selectbox(
        'Select a Variable to Filter Dataframe by',
        ('Location', 'Instruction Rooms', 'Sealing Rooms', 'Baptismal Fonts', 'Square Footage', 'Acreage', 'Elevation'))
    if option == 'Location':   
        location = st.text_input('Enter a location to pull up its data', value='Arizona')
        locationDf = df[df['Temple'].str.contains(location)]
    
        locationDf['Temple'] = locationDf['Temple'].str.replace(location, '')
    
        locationDf = locationDf.drop(locationDf.columns[0], axis=1)
        locationDf = locationDf.set_index('Temple')
        st.dataframe(locationDf)
    if option == 'Instruction Rooms':
        rooms = st.text_input('Enter a number of rooms', value = '1')
        roomsDf = df[df['Instruction Rooms'] == int(rooms)]
        
        roomsDf = roomsDf.drop(roomsDf.columns[0], axis=1)
        roomsDf = roomsDf.set_index('Temple')
        st.dataframe(roomsDf)
    if option == 'Sealing Rooms':
        seal = st.text_input('Enter a number of rooms', value = '1')
        sealDf = df[df['Sealing Rooms'] == int(seal)]
        
        sealDf = sealDf.drop(sealDf.columns[0], axis=1)
        sealDf = sealDf.set_index('Temple')
        st.dataframe(sealDf)
    if option == 'Baptismal Fonts':
        fonts = st.text_input('Enter a number of fonts', value = '1')
        fontsDf = df[df['Baptismal Fonts'] == int(fonts)]
        
        fontsDf = fontsDf.drop(fontsDf.columns[0], axis=1)
        fontsDf = fontsDf.set_index('Temple')
        st.dataframe(fontsDf)
    if option == 'Square Footage':
        minFootage = st.text_input('Enter a minimum square footage', value = '10000')
        footageDf = df[df['Square Footage']  > int(minFootage)]
        
        footageDf = footageDf.drop(footageDf.columns[0], axis=1)
        footageDf = footageDf.set_index('Temple')
        st.dataframe(footageDf)
    if option == 'Acreage':
        acre = st.text_input('Enter a minimum acreage', value = '10')
        acreDf = df[df['Acreage'] > int(acre)]
        
        acreDf = acreDf.drop(acreDf.columns[0], axis=1)
        acreDf = acreDf.set_index('Temple')
        st.dataframe(acreDf)
    if option == 'Elevation':
        minElevation = st.text_input('Enter a minimum Elevation', value = '1000')
        elevationDf = df[df['Elevation (Feet)'] > int(minFootage)]
        
        elevationDf = elevationDf.drop(elevationDf.columns[0], axis=1)
        elevationDf = elevationDf.set_index('Temple')
        st.dataframe(elevationDf)
    
    
   