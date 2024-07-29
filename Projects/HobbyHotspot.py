from dataclasses_functions import *

print("Welcome to HobbyHotspot!")
print("A place where you can input your zipcode")
print("and be shown a list of all current users with the same hobbies as you!")
print()
users_info_path="users_info.txt"
while True:
    print("Would you like to make a new account[New account] or log in? [Log in]")
    user_input=input("> ").capitalize()
    if user_input=="New account":
        user1=new_account()
        write_users_to_txt(user1,users_info_path)

    elif user_input=="Log in":
        log_user_in(users_info_path)
        while True:
            print("Woud you like to add hobbies to your account[Add], View all users near you with the same hobbies [View]")
            user_input=input("> ")
            if user_input=="Add":
                


        
        

















    else:
        print("invalid option please type New account or Log in")
    