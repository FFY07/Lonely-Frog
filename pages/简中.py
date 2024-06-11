import streamlit as st  
import pandas as pd 

import streamlit as st  
import pandas as pd 
import numpy as np

st.set_page_config("最好的青蛙聊天网站")

st.title("为青蛙量身打造的约会软体")
st.header("87%使用此网站的青蛙已找到心中的 “他” ", divider = "rainbow")

st.image("Ll4NX7.png")

st.write("!!! 即刻加入我们以获得69%优惠!!!")

st.write ("会员费 : 666$")

st.text_input("请输入信用卡号码","")
st.text_input("CVV", "", 3)

st.header("20KM以内附近的单身青蛙")


with st.container():
    df = pd.DataFrame(
    np.random.randn(10, 2) / [100, 150] + [1.2963,
    103.8502],
    columns=['lat', 'lon'])
    st.map(df)