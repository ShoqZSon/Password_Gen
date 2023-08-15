from cryptography.fernet import Fernet
import os.path

def write_key(directory):
    print("Creating key...")
    # generates a key and save it into a file
    key = Fernet.generate_key()
    with open(directory, "wb") as key_f:
        key_f.write(key)
    print("New key created")

def question(function):
    answer = False
    # question method for asking if the input is correct or not
    # y -> yes, n -> no, len(x) for the length of the string
    user_input = input(f"'Create a new key'? y/n ")
    while (user_input != "y" or user_input != "n") and len(user_input) != 1:
        if user_input == "y":
            answer = True
            break
        if user_input == "n":
            answer = True
            break

    # if answer is False it asks again
    if (user_input == "y" or user_input == "n") and answer:
        if user_input == "y":
            function()
        elif user_input == "n":
            print("No new key created")
        else:
            print("")
            question(write_key())

def check_key(directory):
    while True:
        try:
            if os.path.exists(directory):
                return True
            else:
                return False
        except FileNotFoundError:
            print("Error: File has not been found")
            break

def generate_key(current_directory):
    directory = current_directory + r"\key.key"
    if (check_key(directory)):
        print("Key exists")
    else:
        print("Key doesnt exist")
        write_key(directory)