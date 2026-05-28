def sanitize(raw : str) -> str:
    return raw.lower().strip()

def bot_dictionary() -> dict:
    return {
        "hello": "Hi there!",
        "hi": "Hola wassup!",
        "how are you": "I'm doing great!",
        "bye": "Goodbye!",
        "your name": "I'm DecoBot! what anput you?",
        "my name is aya": "Nice to meet you Aya!",
        "help": "I can answer basic questions!",
        "who made you": "Aya made me!",
        "who is aya": "The best future AI engineer!!",
        "tell me about aya": "Aya is 2nd year Computer science engineering stuent at USTHB, a very talented one and she's an AI enthusiast and a UI/UX designer!"
    }

knowledge = bot_dictionary()

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit" or user_input.lower() == "exit":
        print("Bot: Ending chat.")
        break
    clean = sanitize(user_input)
    if clean in knowledge:
        print(f"Bot: {knowledge[clean]}")
    else:
        print("Bot: I don't understand that.")



