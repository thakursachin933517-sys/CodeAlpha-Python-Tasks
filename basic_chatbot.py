# Simple Rule-Based Chatbot
# Code Alpha Internship Task 4

def chatbot():
    # Introduction message
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the conversation.")
    
    # Main conversation loop
    while True:
        # Get user input and normalize it
        user_input = input("You: ").lower().strip()
        
        # Rule-based response system
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "i'm fine" or user_input == "i am good":
            print("Chatbot: That's great to hear!")
        elif user_input == "what's your name" or user_input == "what is your name":
            print("Chatbot: I'm just a simple chatbot created for Code Alpha internship!")
        elif user_input == "bye" or user_input == "goodbye":
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop
        else:
            # Default response for unknown inputs
            print("Chatbot: I'm not sure how to respond to that. I'm still learning!")

# Program entry point
if __name__ == "__main__":
    chatbot()  # Start the chatbot
