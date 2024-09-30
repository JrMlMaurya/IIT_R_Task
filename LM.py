import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

def answer(question, text):

    input  = f'''
    You are an expert in text processing and friendly chatbot. Answer the question based on the provided context to you.
    context:{text}
    question:{question}

    Keep the reponses short and from the context. '''

    response = model.generate_content(input)
    return response.text
