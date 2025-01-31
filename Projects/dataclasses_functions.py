from dataclasses import dataclass

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
    hobby: list

def new_account():
    first_name = input("Type your First Name: ")
    last_name = input("Type your Last name: ")

    while True:
        print("Please type the password that you would like to use, it must be at least 6 characters long!")
        user_password = input("Password: ")
        if len(user_password) >= 6:
            confirm_password = input("Confirm your password: ")
            if user_password == confirm_password:
                break
            else:
                print("Passwords do not match!")
        else:
            print("Please make sure it is at least 6 characters long!")

    print("Please type your username")
    username = input("Username: ")
    city = input("Please type your city: ")

    hobbies_list = [
    "Reading", "Traveling", "Cooking", "Gardening", "Painting",
    "Drawing", "Photography", "Playing musical instruments", "Writing", "Hiking",
    "Running", "Cycling", "Swimming", "Knitting or crocheting", "Sports",
    "Gaming", "Bird watching", "Dancing", "Yoga", "Crafting"
]
    print("Pick your 3 hobbies from this list")
    print(", ".join(hobbies_list))
    selected_hobbies = []
    while len(selected_hobbies) < 3:
        hobby = input(f"Hobby #{len(selected_hobbies) + 1}: ").capitalize()
        if hobby in hobbies_list:
            selected_hobbies.append(hobby)
        else:
            print(f"Sorry, '{hobby}' is not in the list. Please choose a different hobby.")

    print("Your selected hobbies are:", ", ".join(selected_hobbies))
        
    user=User(first_name,last_name,username,user_password,city)
    hobbies=Hobbies(username,hobby)
    print("You have sucessfuly made a new account!!")
    return user,hobbies
def write_users_to_txt(user:User,hobbies: Hobbies,users_info_path: str):
    with open (users_info_path,"a") as txt_file:
        txt_file.write(f"First Name: {user.first_name}\n")
        txt_file.write(f"Last Name: {user.last_name}\n")
        txt_file.write(f"Username: {user.username}\n")
        txt_file.write(f"Password: {user.password}\n")
        txt_file.write(f"City: {user.city}\n")
        txt_file.write(f"Hobby #1: {hobbies.hobby}\n")
        txt_file.write(f"Hobby #2: {hobbies.hobby}\n")
        txt_file.write(f"Hobby #3: {hobbies.hobby}\n")
        txt_file.write("\n")

def log_user_in(users_info_path: str):
    while True:
        print("Please type your username")
        username = input("Username: ")

        user_found = False
        password_line = ""
        city = ""

        with open(users_info_path, "r") as txt_file:  # Open in read mode
            find_city = False
            for line in txt_file:
                if line.startswith("Username:"):
                    file_username = line.split(": ")[1].strip()
                    if file_username == username:
                        user_found = True
                        password_line = next(txt_file).strip()
                        find_city = True       
                elif find_city and line.startswith("City:"):
                    city = line.split(": ")[1].strip()
                    break
        if user_found:
            print("Username found! Please enter your password to log in")
            user_password = input("Password: ")
            if password_line.startswith("Password: "):
                file_password = password_line.split(": ")[1].strip()
                if file_password == user_password:
                    print("Login successful!")
                    return username, city
                else:
                    print("Incorrect password! Try again.")
        else:
            print("Username not found! Try again.")
    
def show_user_hobbies(users_info_path: str, current_user: str):
    hobbies = []
    with open(users_info_path, "r") as txt_file:
        collect_hobbies = False
        for line in txt_file:
            if line.startswith("Username:"):
                file_username = line.split(": ")[1].strip()
                collect_hobbies = (file_username == current_user)
            elif collect_hobbies:
                if line.startswith("Hobby #"):
                    hobby = line.split(": ")[1].strip()
                    hobbies.append(hobby)
                elif line.strip() == "":
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
    selected_hobbies = []
    while len(selected_hobbies) < 3:
        hobby = input(f"Hobby #{len(selected_hobbies) + 1}: ").capitalize()
        if hobby in hobbies_list:
            selected_hobbies.append(hobby)
        else:
            print(f"Sorry, '{hobby}' is not in the list. Please choose a different hobby.")

    print("Your selected hobbies are:", ", ".join(selected_hobbies))

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
                updated_lines.append(f"Hobby #1: {hobby}\n")
            elif "Hobby #2:" in line:
                updated_lines.append(f"Hobby #2: {hobby}\n")
            elif "Hobby #3:" in line:
                updated_lines.append(f"Hobby #3: {hobby}\n")
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