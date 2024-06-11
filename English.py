import streamlit as st  
import pandas as pd 
import numpy as np
from pages import Home, About, Service

st.set_page_config("Best Frog dating website")

st.title(":rainbow[LONELY]:green[FROG]")
st.header("A Perfect :red[Dating] app for Frog ")
st.subheader(":orange[87%] of frog who use our app has matched! ", divider = "rainbow")
st.image("smile.jpg")

frog18 = st.checkbox(":gray[I agree that I'm an adult Frog.]")
agree = st.checkbox(":gray[I agree to the terms & conditions.]")

st.subheader(":gray[Please agree before proceed to our service.]", divider = "gray")
if frog18 and agree == True:


    st.header("Welcome to LONELY:green[FROG]")
    st.image("zeus.jpg")

    st.subheader("We provide the best platform and service to all frogs!! ")

    tab1, tab2, tab3, tab4 = st.tabs(["Home", "Service", "Customer Review", "Our User"])

    with tab1:
        st.header(":rainbow[LONELYFROG]")
        st.subheader("With our team of excellent professionals, be ready to find your Mr/Mrs Right in no time!",divider = "gray")
        st.write(":red[Before] using LONELYFROG")
        st.image("before.jpg", width=200)
        st.write(":green[After] using LONELYFROG")
        st.image("after.gif", width=200)

    with tab2:
        st.header("We provide alot of service such as")
        st.subheader(":orange[Frogy Dating]", divider = "gray")
        st.write("Meet eligible frogs with our different packages")
        st.image("diffrentfrog.jpg", width=350)

        st.subheader(":orange[Fleek Image Consulting]", divider = "gray")
        st.write("Build confidence and self image with various workshops held by Fleek")
        st.image("Ll4NX7.png", width=350)

        st.subheader(":orange[Frog Events]", divider = "gray")
        st.write("Events hosted by :rainbow[LONELYFROG] to spice up speed dating in today’s era")
        st.image("event.jpg", width=350)

        st.subheader("Drop us an e-mail at")
        st.subheader("LONELYFROG@yafrog.com")
        st.subheader("or Whatsapp")
        st.subheader("+65 6666 4200")

    with tab3:
        st.image("coolfrog.jpg", 'Justin frogber',width=100,)
        st.subheader("⭐⭐⭐⭐⭐")
        st.write('"I managed to get my True love,thanks to LONELYFROG"')

        st.image("body.jpg",'Chris BumFrog', width=100)
        st.subheader("⭐⭐⭐⭐")
        st.write('"Still better than other Dating App"')

        st.image("halal.png","Shafiq Katak", width=100)
        st.subheader("⭐⭐⭐⭐⭐")
        st.write('"Aplikasi ini sempurna, dia ada katak yang islam "')

        st.image("xukun.jpg", '菜蛙坤',width=100)
        st.subheader("⭐⭐⭐⭐⭐")
        st.write('"这田鸡太美"')

    with tab4:
        st.subheader("Frog that are using LONELY:green[FROG] Right now!!!")
        with st.container():
            df = pd.DataFrame(
            np.random.randn(400, 2) / [100, 100] + [1.2963,
            103.8502],
            columns=['lat', 'lon'])
            st.map(df)

        