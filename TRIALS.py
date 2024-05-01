import random

# Define responses
greetings = ["Hi there! Welcome to PizzaBot. How can I assist you today?",
             "Hello! PizzaBot here. What can I do for you?",
             "Hey! Welcome to PizzaBot. How may I help you?"]

options = ["Would you like to order a pizza or ask about our specials?",
           "Are you looking to place an order or inquire about our menu?",
           "Do you want to order a pizza or know more about our deals?"]

goodbyes = ["Thank you for visiting PizzaBot! Have a great day!",
            "Thanks for chatting with PizzaBot. Enjoy your pizza!",
            "Goodbye! PizzaBot hopes to see you again soon!"]

# Define functions
def get_user_input():
    return input("You: ")

def respond(message):
    if "order" in message:
        return "Great! Let's start building your pizza. What size would you like?"
    elif "specials" in message or "deals" in message or "menu" in message:
        return "Our specials today are: 1. Pepperoni Pizza 2. Margherita Pizza 3. Veggie Supreme. What would you like to know more about?"
    elif any(greeting in message.lower() for greeting in ["hello", "hi", "hey"]):
        return random.choice(options)
    elif "thank" in message.lower() or "bye" in message.lower() or "see you" in message.lower():
        return random.choice(goodbyes)
    else:
        return "I'm sorry, I didn't understand that. How can I assist you?"

# Main function
def pizza_bot():
    print(random.choice(greetings))
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print(random.choice(goodbyes))
            break
        else:
            response = respond(user_input)
            print("PizzaBot:", response)

# Start the conversation
if __name__ == '__main__':
    pizza_bot()
