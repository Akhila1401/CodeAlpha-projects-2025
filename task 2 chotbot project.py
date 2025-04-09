import nltk
import random
import string
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Define the chatbot pairs (pattern-response)
chatbot_pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I assist you today?"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm just a chatbot, but I'm doing well!", "I'm feeling fine, how about you?"]),
    (r"what is your name?", ["I am a chatbot, I don't have a name, but you can call me 'Chatbot'."]),
    (r"bye|exit|quit", ["Goodbye! Have a great day!", "Bye! Take care!", "It was nice chatting with you."]),
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", "Why was the math book sad? Because it had too many problems."]),
    (r"what can you do?", ["I can chat with you and answer basic questions. Ask me anything!"]),
    (r"(.*)", ["Sorry, I don't understand that. Could you rephrase it?"]),
]

# Create the chatbot
chatbot = Chat(chatbot_pairs, reflections)

# Start the conversation
def start_chat():
    print("Chatbot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()
