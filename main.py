import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit')

st.write('Display Image')
img = Image.open('DSC_2547.JPG')
st.image(img, caption='Doggie',use_column_width=True)