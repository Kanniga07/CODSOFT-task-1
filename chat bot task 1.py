# chatbot's responses
data = {
    "hi": "Hey there! I am a helpful chatbot available to help you.",
    "hello": "Hey there! In what way may I assist you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from": "I'm from the digital world, always ready to chat!",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today": "I don't eat, but I can help you find delicious recipes and food-related information.",
    "what is your favorite color?": "I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music, but I'm here to chat about it!",
    "bye": "Goodbye! Have a wonderful day and be careful"
}

# To get a response based on input using if-else statements
def get_response(user_input):
    user_input = user_input.lower()

    # Responding based on the predefined rules
    if user_input == "hi":
        return data["hi"]
    elif user_input == "hello":
        return data["hello"]
    elif user_input == "what is your name":
        return data["what is your name"]
    elif user_input == "where are you from":
        return data["where are you from"]
    elif user_input == "how are you":
        return data["how are you"]
    elif user_input == "do you have any hobbies or interests?":
        return data["do you have any hobbies or interests?"]
    elif user_input == "what did you eat today":
        return data["what did you eat today"]
    elif user_input == "what is your favorite color?":
        return data["what is your favorite color?"]
    elif user_input == "do you enjoy listening to music?":
        return data["do you enjoy listening to music?"]
    elif user_input == "bye":
        return data["bye"]
    else:
        return "I apologize for not understanding it. Would you mind changing your sentence?"

# Main
print("Chatbot: Hello! I'm a basic chatbot, and I'm here to help!")

while True:
    user_input = input("Me: ")
    if user_input.lower() == "bye":
        print("Chatbot: Farewell! Enjoy your wonderful day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
