# 📚 LLM Flashcard Generator - AI-Powered Q&A Maker

📽️ **Demo Video**  
[Watch on YouTube](https://your-demo-link.com) *(replace with actual link)*

## 🌟 Overview
**LLM Flashcard Generator** is a web application that helps users create intelligent flashcards from PDF documents using OpenAI's GPT-3.5. Ideal for students and educators, it simplifies studying with smart Q&A generation.

🔗 **Live URL:** [LLM Flashcard Generator](https://flashcardgenerator23.streamlit.app)
🔗 **GitHub Repository:** [flashcardgenerator](https://github.com/maneeish/flashcardgenerator/tree/main)

---

## ✨ Features
- 📄 **PDF Upload** – Upload learning materials directly.
- 🤖 **AI-Generated Flashcards** – Uses GPT-3.5 to extract Q&A.
- 📤 **Download Options** – Export as JSON or text.
- 🌐 **Streamlit UI** – Simple and clean user interface.

---

## 🛠️ Tech Stack
- **Python** – Core logic and backend.
- **Streamlit** – Web interface and deployment.
- **OpenAI GPT-3.5** – Natural language processing.
- **PyMuPDF** – Extract text from PDFs.

---

## 📂 Project Structure

- `app.py` – Main Streamlit app  
- `llm_utils.py` – GPT-based Q&A generation logic  
- `parser_utils.py` – PDF parsing helper  
- `flashcard_utils.py` – Export utilities  
- `requirements.txt` – Python dependencies  
- `.streamlit/`
  - `config.toml` – Streamlit app configuration

---

## 🚀 Getting Started
### 🔧 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/maneeish/flashcardgenerator.git
   cd flashcardgenerator
   
  ```bash
   pip install -r requirements.txt


### Run Locally
# Set your OpenAI API Key in environment variable
export OPENAI_API_KEY="your-openai-api-key"

## Then run the Streamlit app
streamlit run app.py


