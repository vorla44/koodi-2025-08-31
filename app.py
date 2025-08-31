import streamlit as st
import pandas as pd
import numpy as np

st.title("Tervetuloa Streamlit-sovellukseen! 👋")

st.write("Tässä pieni demo, joka näyttää satunnaisia numeroita taulukossa.")

# Luo satunnaista dataa
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.dataframe(data)

# Interaktiivinen komponentti
nimi = st.text_input("Kirjoita nimesi:")
if nimi:
    st.success(f"Hei {nimi}, hienoa että kokeilet Streamlitiä!")
