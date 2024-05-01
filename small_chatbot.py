import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'(.*) car', ['Cars are 4 wheel drivers that are commonly used for transportation']),
    (r'(.*) bus', ['Buses are 2 wheel drivers that are commonly used for transportation']),
    (r'(.*) truck', ['Trucks are 3 wheel drivers that are commonly used for transportation']),
    (r'(.*) boat', ['Boats are 4 wheel drivers that are commonly used for transportation']),
    (r'(.*) plane', ['Planes are 5 wheel drivers that are commonly used for transportation']),
    (r'(.*) train', ['Trains are 6 wheel drivers that are commonly used for transportation']),
    (r'(.*) motorcycle', ['Motorcycles are 7 wheel drivers that are commonly used for transportation']),
    (r'(.*) bicycle', ['Bicycles are 8 wheel drivers that are commonly used for transportation']),
]

#create a chatbot
chatbot = Chat(patterns, reflections)


# Define a function to start the conversation
def vehicle_info_system():
    print("Welcome to VehicleInfo System!")
    print("Ask about any vehicle. Type exit to end the conversation")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
          print("Exiting....")
          break
        else:
          response = chatbot.respond(user_input)
          print("Bot: ", response)

# Start the conversation
if __name__ == '__main__':
    nltk.download('punkt')
    vehicle_info_system()