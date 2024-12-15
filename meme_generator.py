import streamlit as st
from PIL import Image
import random

# Load pre-set FOOR templates
def load_templates():
    return [
        {"name": "Classic FOOR", "image": "foor_classic.png"},
        {"name": "Banana Attack", "image": "foor_banana.png"},
        {"name": "Zen Master", "image": "foor_zen.png"},
    ]

def generate_caption(prompt):
    captions = [
        f"When life gives you {prompt}, FOOR throws bananas!",
        f"FOOR says: '{prompt}' is no match for duct tape!",
        f"Chaos, {prompt}, and bananas: FOOR approves!",
    ]
    return random.choice(captions)

# Streamlit app
st.title("FOOR Meme Generator")
st.subheader("Create your own FOOR memes and share with the community!")

# Meme template selection
st.sidebar.title("Choose Your FOOR Template")
templates = load_templates()
selected_template = st.sidebar.radio(
    "Templates:", [template["name"] for template in templates]
)

# Load selected image
selected_image = next(
    template["image"] for template in templates if template["name"] == selected_template
)
image = Image.open(selected_image)

# Prompt input
prompt = st.text_input(
    "What is FOOR's chaos handling today?", placeholder="e.g., bear market, FUD, broken duct tape"
)

# Generate and display meme
if st.button("Generate Meme"):
    if prompt:
        caption = generate_caption(prompt)
        st.image(image, caption=caption, use_column_width=True)
        st.success("Meme generated! Right-click to save or share.")
    else:
        st.warning("Please enter a prompt to generate a caption.")

# Sharing options
st.subheader("Share Your Meme")
st.write("Click below to download your meme and share it on X or Telegram!")
if st.button("Save Meme"):
    st.write("Feature coming soon: One-click share!")
