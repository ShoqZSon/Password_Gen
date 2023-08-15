import os
import json

# function check_file
# check if path\to\config.json file exists
    # if True
        # proceed
    # if False
        # create path\to\config.json 


# check if path\to\password_list is filled in
    # if True
        # check if path\to\password_list is valid
        # if True
            # proceed
        # if False
            # print current path\to\password_list
            # user input correct path\to\password_list of password_list.csv
    # if False
        # input path\to\password_list


def check_config(current_directory):
    config_directory = current_directory + r"\config.json"
    try:
        if (os.path.exists(config_directory)):
            return True
        else:
            return False
    except PermissionError:
        print("Error: Access to config denied.")

def validate_path(directory):
     

def create_config(current_directory):
    if (check_config(current_directory)):
        wit