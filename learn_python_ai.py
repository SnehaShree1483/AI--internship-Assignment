import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

def learn_python(topic):
    prompt = f"""
    You are an expert Python tutor.
    Teach {topic} with examples.
    """

    response = model.generate_content(prompt)
    return response.text

print(learn_python("Functions"))
