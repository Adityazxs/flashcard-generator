import streamlit as st
from utils.parser import extract_text
from utils.flashcard_gen import generate_flashcards
from utils.export import export_to_csv, export_to_json
import os

st.set_page_config(page_title="Flashcard Generator", layout="wide")
st.title("📚 LLM-Powered Flashcard Generator")

uploaded_file = st.file_uploader("Upload a .pdf or .txt file", type=["pdf", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

st.text_area("Paste content here:")

st.button("Generate Flashcards")

text_input = st.text_area("Or paste your educational content here:", height=300)

subject = st.selectbox("Select Subject (Optional)", ["General", "Biology", "History", "Computer Science", "Physics"])

if st.button("Generate Flashcards"):
    with st.spinner("Processing content and generating flashcards..."):
        content = extract_text(uploaded_file, text_input)
        flashcards = generate_flashcards(content, subject)

        if flashcards:
            st.success(f"Generated {len(flashcards)} flashcards successfully!")
            for i, card in enumerate(flashcards):
                st.markdown(f"**{i+1}. {card['question']}**")
                st.markdown(f"> {card['answer']}")

            # Save
            os.makedirs("outputs", exist_ok=True)
            export_to_csv(flashcards, "outputs/flashcards.csv")
            export_to_json(flashcards, "outputs/flashcards.json")

            st.download_button("📥 Download CSV", data=open("outputs/flashcards.csv", "rb"), file_name="flashcards.csv")
            st.download_button("📥 Download JSON", data=open("outputs/flashcards.json", "rb"), file_name="flashcards.json")
        else:
            st.error("No flashcards were generated. Try different content.")
