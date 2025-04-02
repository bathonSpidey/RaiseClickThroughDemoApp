import streamlit as st
import time
import random
import pandas as pd

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
        option = st.selectbox("Choose a crop:", ["Winter Wheat", "Rice", "Corn", "Vineyard", "Potatoes", "Herbs", "Onion"])

    with col2:
        st.write("###  Processing")
        processing_options = ["Nitrate Content", "Water", "Weeds", "Pests", "Damages", "All"]
        selected_option = st.selectbox("Choose a processing type:", processing_options, index=0)

    html_file_path = "heatmap.html"

    if st.button("Process"):
        try:
            with open(html_file_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            # Embed the HTML content inside Streamlit
            st.components.v1.html(html_content, height=600, scrolling=True)
            main_data = {
        "Crop": ["Winter wheat"],
        "Processing": ["All"],
        "Type": ["Drone"],
        "Total Hectares": [9],
        "Total Analyed": [4],
        "Growth Month": ["3rd"],
        "Location": ["Bayern, Germany"],
        "Upcoming Weather Conditions": ["Seems to rise, please take care of water. There might be a storm approaching, please make sure your crops are insured."]
    }
            def style_df(df):
                return df.style.set_properties(**{
                    'text-align': 'center',
                    'word-wrap': 'break-word'
                }).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}])
            df_main = pd.DataFrame(main_data)
            
            st.write("### Inspection Results")
            st.markdown(df_main[['Crop', 'Processing', "Location", 'Growth Month']].to_html(escape=False, index=False, justify="left"), unsafe_allow_html=True)
            st.write("### Type & Hectares")
            st.markdown(df_main[['Type', 'Total Hectares']].to_html(escape=False, index=False, justify="left"), unsafe_allow_html=True)
            st.write("### Weather Forecast")
            st.markdown(df_main[['Upcoming Weather Conditions']].to_html(escape=False, index=False, justify="left"), unsafe_allow_html=True)


        # Display damages as a separate sub-table
            damage_data = [
            {"Type": "Nitrate", "Area Affected": "1 ha", "Remedy": "Apply more after consulting expert"},
            {"Type": "Water Content", "Area Affected": "2 ha", "Remedy": "Addition to nitrate water content seems lacking. If it was a mistake please check nitrate content."},
            {"Type": "Weed", "Area Affected": "None", "Remedy": "None"}
        ]
            df_damages = pd.DataFrame(damage_data)
            st.write("### Damage Report")
            st.dataframe(df_damages, hide_index=True)


        except FileNotFoundError:
            st.error("Error: The map file was not found. Please generate the map first.")

