from groq import Groq
from dotenv import load_dotenv
import os
import sys
import re
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()

def get_emojis_for_sentence(sentence: str) -> str:
    try:
        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"I need to wrap up my sentence with a few emojis. Only print the emojis. Sentence: {sentence}.",
                }
            ],
            model="deepseek-r1-distill-llama-70b",
            stream=False,
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
def extract_emojis(response: str) -> str:
    cleaned_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
    return cleaned_response
if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:])
        emojis = extract_emojis(get_emojis_for_sentence(sentence))
        emojis = emojis.replace("\n", "")
        emojis = emojis.strip() 
        print(emojis.encode('utf-8').decode('utf-8'), flush=True)
    else:
        print("Please provide a sentence as an argument.")