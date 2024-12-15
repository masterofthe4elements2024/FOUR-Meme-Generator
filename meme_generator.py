import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# Load pre-set FOOR templates
def load_templates():
    base_path = Path(__file__).parent
    return [
        {"name": "Classic FOOR", "image": base_path / "foor_classic.png"},
        {"name": "Banana Attack", "image": base_path / "foor_banana.png"},
        {"name": "Zen Master", "image": base_path / "foor_zen.png"},
    ]

# Add text to image
def add_text_to_image(image_path, text):
    # Load the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Define font size and position
    try:
        font = ImageFont.truetype("arial.ttf", size=30)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    image_width, image_height = image.size

    # Position text at the center bottom of the image
    text_x = (image_width - text_width) / 2
    text_y = image_height - text_height - 20

    # Add text with a black outline for readability
    draw.text((text_x - 1, text_y - 1), text, font=font, fill="black")
    draw.text((text_x + 1, text_y - 1), text, font=font, fill="black")
    draw.text((text_x - 1, text_y + 1), text, font=font, fill="black")
    draw.text((text_x + 1, text_y + 1), text, font=font, fill="black")
    draw.text((text_x, text_y), text, font=font, fill="white")

    return image

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

# Prompt input
prompt = st.text_input(
    "What is FOOR's chaos handling today?", placeholder="e.g., bear market, FUD, broken duct tape"
)

# Generate and display meme
if st.button("Generate Meme"):
    if prompt:
        meme_image = add_text_to_image(selected_image, prompt)
        st.image(meme_image, caption="Your Meme", use_column_width=True)
        st.success("Meme generated! Right-click to save or share.")
    else:
        st.warning("Please enter a prompt to generate a caption.")

# Sharing options
st.subheader("Share Your Meme")
st.write("Click below to download your meme and share it on X or Telegram!")
if st.button("Save Meme"):
    st.write("Feature coming soon: One-click share!")
