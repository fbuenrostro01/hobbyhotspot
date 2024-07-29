from dataclasses import dataclass

@dataclass
class Users:
    first_name: str
    last_name: str
    username: str
    password: str
    zip_code: int



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
    user_input=input("Username: ")
    username=user_input
   
    
    while True:
        print("Please type your zip code ")
        zip_code=input("Zip Code: ")
        if zip_code.isdigit():
            zip_code=int(zip_code)
            break
        else:
            print("Please type a valid zipcode")
    
    user1=Users(first_name,last_name,username,user_password,zip_code)
    print("You have sucessfuly made a new account!!")
    return user1
    
def write_users_to_txt(user1:Users,users_info_path: str):
    with open (users_info_path,"a") as txt_file:
        txt_file.write(f"First Name: {user1.first_name}\n")
        txt_file.write(f"Last Name: {user1.last_name}\n")
        txt_file.write(f"Username: {user1.username}\n")
        txt_file.write(f"Password: {user1.password}\n")
        txt_file.write(f"Zip Code: {user1.zip_code}\n")
        txt_file.write("\n")

def log_user_in(users_info_path: str):
    while True:
        print("Please type your username")
        username=input("Username: ")

        user_found=False
        password_line=""

        with open(users_info_path,"r") as txt_file:
            user_found=False
            for line in txt_file:
                if line.startswith("Username:"):
                    file_username=line.split(": ")[1].strip()
                    if file_username==username:
                        user_found=True
                        
                        password_line=next(txt_file).strip()
                        break
        if user_found:
                 print("Username found! please enter your password to log in")
                 user_password=input("Password: ")
                 if password_line.startswith("Password: "):
                     file_password=password_line.split(": ")[1].strip()
                     if file_password==user_password:
                         print("Login successful!")
                         break
                     else:
                         print("Incorrect password! Try again.")
        else:
            print("Username not found! Try again.")

                

                       



    

    

      
   