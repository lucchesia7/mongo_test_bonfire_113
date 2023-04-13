import streamlit as st # Alias our streamlit import as st

st.title('MTG Tracer')
st.text('My first application which uses\n')
st.text('pandas, streamlit, mongo, and Python to marry together the application')

st.header('Here are the different pages of my application!:')

st.text('Image Return: Returns an image of the requested card')
st.text("Recommender: Uses a NN model to return recommended cards")
st.text("Visualizer: Allows users to view information about cards")


st.title('Image Return')
st.title('Visualizer')
st.title('recommender')