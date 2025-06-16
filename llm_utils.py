import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcards(text, subject="General", language="English"):
    prompt = f"""
You are an intelligent flashcard generator for {subject} students.
Read the following content and generate 10–15 Q&A style flashcards.

For each flashcard, include:
- A question starting with 'Q:'
- An answer starting with 'A:'
- A difficulty level (Easy, Medium, Hard) starting with 'Difficulty:'

Format:
Q: <Question>
A: <Answer>
Difficulty: <Easy | Medium | Hard>

If a section or chapter heading is detected, format it like:
# <Section Title>

Output must be in {language}.

Content:
{text[:3000]}  # Trimmed to fit within token limits
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
