from agent.controller import chat
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = chat(user_input)
    print("Bot:", response)