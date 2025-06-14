import openai
import os
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your key via .env or system env

def generate_flashcards(content, subject="General"):
    if not content:
        return []

    system_prompt = "You are an expert teacher creating helpful flashcards for students."
    
    user_prompt = f"""
Generate 10–15 flashcards from the following {subject} content.

Format:
Topic: <optional topic>
Q: <Question>
A: <Answer>

Be concise, factually correct, and self-contained.
---
{content}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        raw_output = response['choices'][0]['message']['content']
        return parse_flashcards(raw_output)
    except Exception as e:
        print("OpenAI Error:", e)
        return []

def parse_flashcards(raw_output):
    flashcards = []
    lines = raw_output.strip().split("\n")
    topic = "General"
    question, answer = "", ""

    for line in lines:
        if line.lower().startswith("topic:"):
            topic = line.split(":", 1)[1].strip()
        elif line.lower().startswith("q:"):
            question = line.split(":", 1)[1].strip()
        elif line.lower().startswith("a:"):
            answer = line.split(":", 1)[1].strip()
            if question and answer:
                flashcards.append({"topic": topic, "question": question, "answer": answer})
                question, answer = "", ""

    return flashcards
