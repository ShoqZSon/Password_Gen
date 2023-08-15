import os.path
import random
import string
import csv

import create_config

def shuffle():
    # contains alphabe, digits 0-9 and special characters
    chars = list(string.ascii_letters + string.digits + string.punctuation)

    # randomize the order of the characters in "characters"
    random.shuffle(chars)

    return chars

# question method for asking if the input is correct or not
def question(function, use_case, characters):
    answer = True

    # y -> yes, n -> no, len(x) for the length of the string
    user_input = input(f"Choose '{use_case}'? y/n ")
    while (user_input != "y" or user_input != "n") and (len(user_input) != 1 or len(user_input) == 0):
        if user_input == "y":
            break
        if user_input == "n":
            answer = False
            break
        if len(user_input) != 1:
            answer = False
            break
        if any(element in characters for element in user_input):
            print("Only 'y' and 'n' allowed")
            answer = False
            break

    # if answer is False it asks again
    if answer:
        print(f"{use_case} set successful")
    else:
        function()

def create_usage():
    # usage means the purpose of the password
    usage = str(input("Input the passwords usage: "))
    #question(usage, "Usage", characters)

    return usage

def create_password(characters):
    # generates random number between 14 and 20
    length = random.randint(14,20);

    # empty password list for the new password
    pw_list = []

    # iterate through the length of inserted password amount
    # appends a random character to the list "pw_list"
    for i in range(length):
        pw_list.append(random.choice(characters))

    # convert "password" from list to string
    password = "".join(map(str, pw_list))
    #question(password, create_password, "Password")

    return password

def create_csv(usage, password, current_directory):
    # write onto existing/new csv file
    fieldnames = ["Usage", "Password"]
    data = {"Usage": usage, "Password": password}
    # directory where the code is placed
    file_path = current_directory + r"\password_list.csv"

    try:
        if os.path.exists(file_path):
            with open(file_path, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(data)
        else:
            with open(file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(data)
    except PermissionError:
        print("Error: Access to password file denied")

def generateEntry(current_directory):
    # shuffles the characters 
    characters = shuffle()

    # captures the usage
    usage = create_usage()
    print(f"Usage: {usage}")

    # captures the password
    password = create_password(characters)
    print(f"Password: {password}")

    # creates the csv file
    create_csv(usage, password, current_directory)