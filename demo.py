import streamlit as st
import time
import random

st.title("Raise Field Inspector")

# File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "heic"])

loading_messages = [
    "Taking too long to upload... How big is your farm? 🌾",
    "Still uploading... Your crops are growing! 🌱",
    "Almost there... Harvesting the pixels! 🍎",
    "Wow, is this a satellite image? 🚀",
    "Hang tight! Good things take time. ⏳",
    "Processing... Meanwhile, grab a coffee ☕"
]

# Initialize session state variables
if "upload_complete" not in st.session_state:
    st.session_state.upload_complete = False

if uploaded_file is not None and not st.session_state.upload_complete:
    st.write("Uploading should take about 30 seconds. Depending on field size, it can be longer or shorter.")
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i in range(101):
        time.sleep(0.15)
        progress_bar.progress(i)
        if i % 20 == 0:
            status_text.write(random.choice(loading_messages))

    st.success("Upload complete! 🎉")
    st.session_state.upload_complete = True  # Mark upload as completed

if st.session_state.upload_complete:
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Select your crop")
        option = st.selectbox("Choose a crop:", ["Rice", "Winter wheat", "Corn", "Vineyard", "Potatoes", "Herbs", "Onion"])

    with col2:
        st.write("### Select type of Processing you want")
        if "processing_options" not in st.session_state:
            st.session_state.processing_options = {"Nitrate Content": False, "Weeds": False, "Pests": False, "Damages": False, "All": False}

        for key in st.session_state.processing_options:
            st.session_state.processing_options[key] = st.checkbox(key, st.session_state.processing_options[key])

    st.button("Start Processing")
