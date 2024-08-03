from dataclasses import dataclass
from typing import List

@dataclass
class User:
    first_name: str
    last_name: str
    username: str
    password: str
    city: str
   

@dataclass
class Hobbies:
    username: str
    hobby1: str
    hobby2: str
    hobby3: str

def new_account():
    first_name=input("Type your First Name: ")
    last_name=input("Type you Last name: ")

    password=True
    while password:
        print("Please type the password that you would like to use, it must be atleast 6 digits long!")
        while True:
            user_password=input("Password: ")
            if len(user_password)>=6:
                break
            else:
                print("Please make sure its atleast 6 digits long!")
        print("Confirm your password again")
        while True:
            user_input=input("Password: ")
            if user_input==user_password:
                password=False
                break
            else:
                print("Passwords do not match!")

    print("Please type your username")
    username=input("Username: ")
    city=input("Please type your city. ")
        
    
    hobbies_list = [
    "Reading", "Traveling", "Cooking", "Gardening", "Painting",
    "Drawing", "Photography", "Playing musical instruments", "Writing", "Hiking",
    "Running", "Cycling", "Swimming", "Knitting or crocheting", "Playing sports",
    "Playing video games", "Bird watching", "Dancing", "Yoga", "Crafting"
]
    print("Pick your 3 hobbies form this list")
    print(", ".join(hobbies_list))
    hobby1=input("Hobby #1: ").capitalize()
    hobby2=input("Hobby #2: ").capitalize()
    hobby3=input("Hobby #3: ").capitalize()
    user=User(first_name,last_name,username,user_password,city)
    hobbies=Hobbies(username,hobby1,hobby2,hobby3)
    print("You have sucessfuly made a new account!!")
    return user,hobbies
def write_users_to_txt(user:User,hobbies: Hobbies,users_info_path: str):
    with open (users_info_path,"a") as txt_file:
        txt_file.write(f"First Name: {user.first_name}\n")
        txt_file.write(f"Last Name: {user.last_name}\n")
        txt_file.write(f"Username: {user.username}\n")
        txt_file.write(f"Password: {user.password}\n")
        txt_file.write(f"City: {user.city}\n")
        txt_file.write(f"Hobby #1: {hobbies.hobby1}\n")
        txt_file.write(f"Hobby #2: {hobbies.hobby2}\n")
        txt_file.write(f"Hobby #3: {hobbies.hobby3}\n")
        txt_file.write("\n")

def log_user_in(users_info_path: str):
    while True:
        print("Please type your username")
        username=input("Username: ")

        user_found=False
        password_line=""
        city=""

        with open(users_info_path,"r") as txt_file:
            find_city=False
            for line in txt_file:
                if line.startswith("Username:"):
                    file_username=line.split(": ")[1].strip()
                    if file_username==username:
                        user_found=True
                        password_line=next(txt_file).strip()
                        find_city=True       
                elif find_city and line.startswith("City:"):
                    city=line.split(": ")[1].strip()
                    break
        if user_found:
                 print("Username found! please enter your password to log in")
                 user_password=input("Password: ")
                 if password_line.startswith("Password: "):
                     file_password=password_line.split(": ")[1].strip()
                     if file_password==user_password:
                         print("Login successful!")
                         return username,city
                     else:
                         print("Incorrect password! Try again.")
        else:
            print("Username not found! Try again.")
    
def show_user_hobbies(users_info_path: str,current_user: str):
    hobbies=[]
    with open(users_info_path,"r") as txt_file:
        collect_hobbies=False
        for line in txt_file:
            if line.startswith("Username:"):
                file_username=line.split(": ")[1].strip()
                collect_hobbies=(file_username==current_user)
            elif collect_hobbies:
                if line.startswith("Hobby #"):
                    hobby=line.split(": ")[1].strip()
                    hobbies.append(hobby)
                elif line.strip()=="":
                    break 
    if hobbies:
        print(f"{current_user}'s hobbies:")
        for hobby in hobbies:
            print(f"- {hobby}")



                
def update_user_hobbies(users_info_path: str, current_user: str): 
    hobbies_list = [
        "Reading", "Traveling", "Cooking", "Gardening", "Painting",
        "Drawing", "Photography", "Playing musical instruments", "Writing", "Hiking",
        "Running", "Cycling", "Swimming", "Knitting or crocheting", "Sports",
        "Games", "Bird watching", "Dancing", "Yoga", "Crafting"
    ]
    print("Update your hobbies. Pick 3 hobbies from this list:")
    print(", ".join(hobbies_list))
    hobby1 = input("New Hobby #1: ").capitalize()
    hobby2 = input("New Hobby #2: ").capitalize()
    hobby3 = input("New Hobby #3: ").capitalize()

    updated_lines = []
    with open(users_info_path, "r") as txt_file:
        lines = txt_file.readlines()

    collect_hobbies = False
    for line in lines:
        if line.startswith("Username:"):
            file_username = line.split(": ")[1].strip()
            if file_username == current_user:
                collect_hobbies = True
            else:
                collect_hobbies = False
            updated_lines.append(line)
        elif collect_hobbies and line.startswith("Hobby #"):
            if "Hobby #1:" in line:
                updated_lines.append(f"Hobby #1: {hobby1}\n")
            elif "Hobby #2:" in line:
                updated_lines.append(f"Hobby #2: {hobby2}\n")
            elif "Hobby #3:" in line:
                updated_lines.append(f"Hobby #3: {hobby3}\n")
        else:
            updated_lines.append(line)

    with open(users_info_path, "w") as txt_file:
        txt_file.writelines(updated_lines)



    
def show_users_in_same_city(users_info_path: str, current_city: str):
    users_in_city = []
    
    with open(users_info_path, "r") as txt_file:
        collect_city = False
        user = {}
        
        for line in txt_file:
            if line.startswith("City:"):
                file_city = line.split(": ")[1].strip()
                if file_city == current_city:
                    collect_city = True
                else:
                    collect_city = False
            
            if collect_city:
                if line.startswith("First Name:"):
                    user['first_name'] = line.split(": ")[1].strip()
                elif line.startswith("Last Name:"):
                    user['last_name'] = line.split(": ")[1].strip()
                elif line.startswith("Username:"):
                    user['username'] = line.split(": ")[1].strip()
                elif line.startswith("City:"):
                    user['city'] = line.split(": ")[1].strip()
                    
                
                    if 'first_name' in user and 'last_name' in user and 'username' in user:
                        users_in_city.append(user)
                    user = {}  
                  
    if users_in_city:
        print(f"Users in {current_city}:")
        for user in users_in_city:
                print(f"- {user['first_name']} {user['last_name']} (Username: {user['username']})")
          
    else:
        print(f"No users found in {current_city}.")