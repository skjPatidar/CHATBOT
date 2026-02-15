import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

DISCLAIMER = """
⚠️ Disclaimer: I am an AI assistant and not a licensed doctor.
Please consult a healthcare professional for serious medical concerns.
"""

def ask_ollama(prompt):
    payload = {
        'model': MODEL,
        'prompt': prompt,
        'stream': False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()['response']

def medical_bot(user_input):
    prompt = f"{DISCLAIMER}\n\nUser: {user_input}\nMedical Bot:"
    response = ask_ollama(prompt)
    return response


if __name__ == "__main__":
    print("Welcome to the Medical Bot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = medical_bot(user_input)
        print(f"Medical Bot: {response}")

        print(DISCLAIMER)
    

