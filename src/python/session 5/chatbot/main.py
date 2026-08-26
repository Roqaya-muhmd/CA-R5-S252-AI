if __name__=="__main__" :
    print("Hello, I am a chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        else:
            # Here you would typically process the user input and generate a response
            print(f"Chatbot: You said '{user_input}'. How interesting!")