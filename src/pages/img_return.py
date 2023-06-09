import streamlit as st
from PIL import Image
from io import BytesIO
import requests
from pathlib import Path
import os
import sys
import pandas as pd

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)
from to_mongo import ToMongo

st.title('Image Return')
c = ToMongo()
answer = st.text_input('Enter Card Name', value='Sol Ring')
card = list(c.cards.find({'name':answer}))[0]['image_uris']['normal']
st.image(Image.open(BytesIO(requests.get(card).content)))
