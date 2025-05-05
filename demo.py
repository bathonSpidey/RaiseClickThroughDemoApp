import streamlit as st
import time
import random
import pandas as pd

st.set_page_config(page_title="Raise Field Inspector", layout="wide")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = "upload"

st.title("🌾 Raise Field Inspector")

# ---------------- STEP 1: UPLOAD ----------------
if st.session_state.step == "upload":
    st.subheader("Step 1: Upload Field Image")

    uploaded_file = st.file_uploader("📷 Upload an image (simulation only)", type=["jpg", "png", "heic"])

    if uploaded_file:
        st.info("Simulating upload (approx. 30 seconds per hectare)...")
        progress_bar = st.progress(0)
        status_text = st.empty()

        loading_messages = [
            "Simulating processing... 🌾",
            "Tailoring to your crops and needs 🌱",
            "Usually 2 mins per hectare in real case 🍎",
            "Please wait... ☕",
        ]

        for i in range(101):
            time.sleep(0.05)
            progress_bar.progress(i)
            if i % 25 == 0:
                status_text.write(random.choice(loading_messages))

        st.success("✅ Upload complete!")
        st.session_state.step = "analysis"  # Move to next step
        st.rerun()  # Refresh UI to show next step

# ---------------- STEP 2: ANALYSIS ----------------
if st.session_state.step == "analysis":
    st.subheader("Step 2: Select Crop and Processing")

    col1, col2 = st.columns(2)

    with col1:
        crop_options = [
            "Winter Wheat", 
            "Rice (coming soon)", 
            "Corn (coming soon)"
        ]
        selected_crop = st.selectbox("Select your crop", crop_options, index=0)

        if selected_crop != "Winter Wheat":
            st.warning("Only Winter Wheat is supported currently.")
            st.stop()

    with col2:
        processing_options = [
            "All", 
            "Nitrate (coming soon)", 
            "Water (coming soon)"
        ]
        selected_processing = st.selectbox("Select processing type", processing_options, index=0)

        if selected_processing != "All":
            st.warning("Only 'All' processing is available.")
            st.stop()

    if st.button("🔍 Process Field"):
        st.session_state.step = "results"
        st.rerun()

# ---------------- STEP 3: RESULTS ----------------

if st.session_state.step == "results":
    st.subheader("Step 3: Inspection Results")

    try:
        with open("heatmap.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        st.markdown("#### Field Heatmap")
        st.components.v1.html(html_content, height=600, scrolling=True)

        main_data = {
            "Crop": ["Winter Wheat"],
            "Processing": ["All"],
            "Type": ["Drone"],
            "Total Hectares": [9],
            "Total Analyzed": [4],
            "Growth Month": ["3rd"],
            "Location": ["Bavaria, Germany"],
            "Upcoming Weather": [
                "Rising temps expected. Water management recommended. Possible storms — ensure insurance coverage."
            ]
        }

        df_main = pd.DataFrame(main_data)

        st.markdown("#### Field Overview")
        st.dataframe(df_main[["Crop", "Processing", "Location", "Growth Month"]], hide_index=True)

        st.markdown("#### Summary")
        st.dataframe(df_main[["Type", "Total Hectares", "Total Analyzed"]], hide_index=True)

        st.markdown("#### Weather Forecast")
        st.info(df_main["Upcoming Weather"][0])

        st.markdown("#### Damage Report")
        df_damages = pd.DataFrame([
            {"Type": "Nitrate", "Affected Area": "1 ha", "Recommendation": "Consult expert before applying more nitrate."},
            {"Type": "Water", "Affected Area": "2 ha", "Recommendation": "Add water. Confirm nitrate levels."},
            {"Type": "Weeds", "Affected Area": "None", "Recommendation": "None"}
        ])
        st.dataframe(df_damages, hide_index=True)

    except FileNotFoundError:
        st.error("Map file 'heatmap.html' not found.")
