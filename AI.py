import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
API= os.getenv("GEMINI_API_KEY")
if not API:
    raise ValueError("Error! API Not found")
rules="Do not use bold texts, and keep all responses very short and consice."
client=genai.Client(api_key=API)
chat=client.chats.create(model="gemini-3.6-flash")
print("chat started. type 'quit' or 'exit' to end")
while True:
    question = input("You: ").strip()
    if question.lower() in ["exit","quit"]:
        print("session ended")
        break
    if not question:
        continue

    response=chat.send_message(question + rules)
    print(f"\nGemini:{response.text}\n")