from dataclasses_functions import *



print("Welcome to HobbyHotspot!")
print("A place where you can input your zipcode")
print("and be shown a list of all current users with the same hobbies as you!")

users_info_path="users_info.txt"

while True:
    print("Would you like to make a new account[New account] or log in? [Log in]")
    user_input=input("> ").capitalize()
    if user_input=="New account":
        user,hobbies=new_account()
        write_users_to_txt(user,hobbies,users_info_path)

    elif user_input=="Log in":
        current_user,city=log_user_in(users_info_path)
        print(f"Current User {current_user}")
        logged_in=True

        while logged_in:
            print("Would You Like to View all users near you with the same hobbies [View],Look at your hobbies [Look], or log out [Logout]?")
            user_input=input("> ").capitalize()
            if user_input=="Look":
                show_user_hobbies(users_info_path,current_user)
                while True:
                    print("Would you like to update your hobbies? Yes[Yes] or No[No].")
                    user_input=input("> ").capitalize()
                    if user_input=="Yes":
                        update_user_hobbies(users_info_path,current_user)
                    elif user_input=="No":
                        break
    
            elif user_input=="Logout":
                print("Logging out...")
                logged_in=False

            elif user_input=="View":
                show_users_in_same_city(users_info_path,city)

            
         

        
        

















    else:
        print("invalid option please type New account or Log in")
    