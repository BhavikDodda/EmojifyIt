from groq import Groq
from dotenv import load_dotenv
import os
import sys
import re
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()
context="My name is Bhavik Dodda and I am a 3rd year Integrated M.Sc. Mathematics student."
response_requirements="Generate a reasonable human-like response that's not too long and use the same language in the messasge. If it is in English then keep it English otherwise if it is in Hindi then you can make it Hinglish."
def get_response(sentence: str) -> str:
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Context: ${context} I need to respond to the following message. ${response_requirements} Message: {sentence}.",
                }
            ],
            model="deepseek-r1-distill-llama-70b",
            stream=False,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
def extract_response(response: str) -> str:
    cleaned_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
    return cleaned_response
if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:])
        ans = extract_response(get_response(sentence))
        ans = ans.replace("\n", "")
        ans = ans.strip() 
        print(ans.encode('utf-8').decode('utf-8'), flush=True)
    else:
        print("Please provide a sentence as an argument.")