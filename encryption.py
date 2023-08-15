from cryptography.fernet import Fernet
import os.path
import string

def check_file(file, type):
    print(f"Checking {type}")
    while True:
        try:
            os.path.exists(file)
            if os.path.exists(file):
                print(type + " exists")
                break
            if not os.path.exists(file):
                print(type + " doesnt exist")
                break
        except FileNotFoundError:
            print(f"Error: {type} has not been found")
            break

def check_file_encryption(file):
    print("Checking if file is encrypted")

    while True:
        try:
            # opens file and reads it in normal read mode
            with open(file, "r") as f:
                # read all file data
                file_data = f.read()

                test = ["Usage", "Password"]
                if any(element in file_data for element in test):
                    print("File is not encrypted")

                else:
                    print("File is already encrypted")
        except FileNotFoundError:
            print("File not found")

def load_key():
    # loads the key from the current directory named 'key.key'
    print("Key loaded")
    return open(r"X:\Programming\Python_Programs\password_generator\key.key", "rb").read()

def encrypt(file, key):
    # Given a filename (str) and key (bytes), it encrypts the file and write it

    f = Fernet(key)

    with open(file, "rb") as f:
        # read all file data
        file_data = f.read()

    encrypted_data = f.encrypt(file_data)

    with open(file, "wb") as f:
        f.write(encrypted_data)

    print("File encrypted")

def encryption():
    # put in files to use here
    file = "X:\Programming\Python_Programs\password_generator\password_list.csv"
    key_file = "X:\Programming\Python_Programs\password_generator\key.key"

    # checks if file to encrypt exists
    check_file(file, "Password file")
    print("")
    # checks if key file exists
    check_file(key_file, "Key file")

    encrypt(file, key_file)

#encryption()