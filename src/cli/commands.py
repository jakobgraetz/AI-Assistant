def quit(user_name):
    print(f"🧠 Assistant: 👋 Bye, {user_name}!")
    exit()

def help():
    print("📚 Available commands:")
    print("     /quit - Exit the program")
    print("     /help - Display the list of commands")

def imagine(prompt):
    print(prompt)

def error():
    print("❌ Invalid command. Please try again.")

def check_commands(prompt, user_name):
    if prompt[0] == "/":
        if prompt == "/quit":
            quit(user_name)
        elif prompt == "/help":
            help()
        else:
            error()
    else:
        return False