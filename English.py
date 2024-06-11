import streamlit as st  
import pandas as pd 
import numpy as np

st.set_page_config("Best Frog dating website")

st.title("Perfect Dating app for Frog")
st.header("87% of frog has matched! ", divider = "rainbow")

st.image("Ll4NX7.png")

st.write("!!! JOIN OUR MEMBER NOW TO ENJOY 69% OFFER !!!")

st.write ("Member fee : 666$")

st.text_input("Card Number","")
st.text_input("CVV", "", 3)

st.header("Frog nearby you")


with st.container():
    df = pd.DataFrame(
    np.random.randn(10, 2) / [100, 150] + [1.2963,
    103.8502],
    columns=['lat', 'lon'])
    st.map(df)

# # df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
# # st.table(df)

# chart_data = pd.DataFrame(np.random.randn(3, 2), columns=["Who using Frog dating app", "Not using Frog dating app"])
# # st.bar_chart(chart_data)
# st.line_chart(chart_data)

