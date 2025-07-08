import streamlit as st
import base64
import json
import os

from script_parser import parse_script
from character_voice import generate_voice_per_scene
from scene_visualizer import generate_scene_image
from movie_editor import assemble_full_movie

# Load app config
with open("production.json") as f:
    config = json.load(f)

st.set_page_config(page_title=config["app_title"], layout="wide")
st.title(config["app_title"])
st.markdown(config["description"])

script_file = st.file_uploader("📜 Upload Script (.txt, .docx, .pdf)", type=["txt", "docx", "pdf"])
photo_files = st.file_uploader("🖼️ Upload Character Photos", type=["jpg", "png"], accept_multiple_files=True)

def show_download_link(filepath):
    with open(filepath, "rb") as file:
        b64 = base64.b64encode(file.read()).decode()
        href = f'<a href="data:video/mp4;base64,{b64}" download="movie_output.mp4">📥 Download Final Movie</a>'
        st.markdown(href, unsafe_allow_html=True)

os.makedirs("storage", exist_ok=True)

if script_file and photo_files:
    with st.spinner("📖 Parsing script..."):
        scenes = parse_script(script_file)

    with st.spinner("🗣️ Generating voices..."):
        voice_clips = generate_voice_per_scene(scenes)

    with st.spinner("🖼️ Generating scene visuals..."):
        image_clips = generate_scene_image(scenes, photo_files)

    with st.spinner("🎞️ Assembling movie..."):
        final_path = assemble_full_movie(scenes, voice_clips, image_clips)

    st.success("✅ Movie generated!")
    st.video(final_path)
    show_download_link(final_path)
else:
    st.info("Please upload both a script and character photos.")
