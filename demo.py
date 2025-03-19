import streamlit as st
import time
import random

st.title("Raise Field Inspector")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "heic"])

loading_messages = [
    "Taking too long to upload... How big is your farm? 🌾",
    "Still uploading... Your crops are growing! 🌱",
    "Almost there... Harvesting the pixels! 🍎",
    "Wow, is this a satellite image? 🚀",
    "Hang tight! Good things take time. ⏳",
    "Processing... Meanwhile, grab a coffee ☕"
]

if uploaded_file is not None:
    st.write("Uplaoding in average should take about 30 seconds.. Depending on field size it can be longer or shorter.")
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(101):
        time.sleep(0.15)  
        progress_bar.progress(i)
        if i % 20 == 0:
            status_text.write(random.choice(loading_messages))
    st.success("Upload complete! 🎉")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Select your crop")
        option = st.selectbox("Choose a crop:", ["Rice", "Winter wheat", "Corn", "Vineyard", "Potatoes", "Herbs", "Onion"])
    with col2:
        st.write("### Select type of Processing you want")
        st.checkbox("Nitrate Content")
        st.checkbox("Weeds")
        st.checkbox("Pests")
        st.checkbox("Damages")
        st.checkbox("All")
    
    st.button("Start Processing")