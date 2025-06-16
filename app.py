import streamlit as st
from parser_utils import extract_text_from_file
from llm_utils import generate_flashcards
from flashcard_utils import (
    parse_flashcards,
    export_flashcards
)

st.set_page_config(page_title="📚 LLM Flashcard Generator")

st.title("📚 LLM-Powered Flashcard Generator")
st.markdown("Generate smart Q&A flashcards from educational content using AI.")

uploaded_file = st.file_uploader("📄 Upload a .pdf or .txt file", type=["pdf", "txt"])
text_input = st.text_area("📝 Or paste content here", height=300)

col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox("📘 Choose subject (optional)", ["General", "Biology", "History", "CS"])

with col2:
    language = st.selectbox("🌐 Choose output language", ["English", "Hindi", "Spanish", "French", "German"])

if st.button("🚀 Generate Flashcards"):
    with st.spinner("Processing..."):

        # Extract content
        if uploaded_file:
            text = extract_text_from_file(uploaded_file)
        elif text_input.strip():
            text = text_input.strip()
        else:
            st.error("Please upload a file or paste content.")
            st.stop()

        # LLM Generation
        raw_output = generate_flashcards(text, subject, language)
        flashcards_by_section = parse_flashcards(raw_output)

        if not flashcards_by_section:
            st.error("No flashcards generated. Please try different input.")
            st.stop()

        # Display flashcards
        st.subheader("📇 Flashcards")
        for section, cards in flashcards_by_section.items():
            st.markdown(f"### 📘 Section: {section}")
            for i, card in enumerate(cards, 1):
                st.markdown(f"**Q{i}:** {card['question']}")
                st.markdown(f"**A{i}:** {card['answer']}")
                st.markdown(f"🔖 *Difficulty:* `{card.get('difficulty', 'Medium')}`")
                st.markdown("---")

        # Export buttons
        st.subheader("📤 Export Options")
        col1, col2 = st.columns(2)

        with col1:
            csv_data = export_flashcards(flashcards_by_section, "csv")
            st.download_button("⬇️ Download CSV", csv_data, "flashcards.csv", "text/csv")

        with col2:
            json_data = export_flashcards(flashcards_by_section, "json")
            st.download_button("⬇️ Download JSON", json_data, "flashcards.json", "application/json")
