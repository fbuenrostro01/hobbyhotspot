from dataclasses_functions import *
import time
import os
def print_computer_with_text(text):
    """Print the ASCII art and scrolling text.
    Parameters: text (str:)The display on the screen of the ASCII Art computer"""
    ascii_art = """
        ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     |         |      |
     |  |                 |  |  |     |         |      |
     |  |                 |  |  |/----|         |      |
     |  |                 |  |  |   ,/|         |      ;
     |  |                 |  |  |  // |         |    ,"
     |  `-----------------'  |," .;'| |         |  ,"
     +-----------------------+  ;;  | |         |,"     -Amanda-
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \\,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________
    """
  #Print the ASCII art and the scrolling text
    print(ascii_art)
    print(text)
def scroll_text(text, width=80, delay=0.1):
    """Scroll the text across the screen.
    Parameters:
    text (str): The text to scroll.
    width (int): The width of the terminal screen (in characters.)
    delay (float): The delay between frames (in seconds)to control the scroll speed."""
    
    #Add spaced to both sides of the text to ensure it scrolls smoothly.
    
    padded_text = ' ' * width + text + ' ' * width
    for i in range(len(padded_text) - width + 1): #Padded text is text that has extra characters (usually spaces) 
        #clear terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        #print the ascii art with the current segment of the scrolling text
        print_computer_with_text(padded_text[i:i + width])
        time.sleep(delay)  # Wait before printing the next frame
if __name__ == "__main__":
    #start scrolling the text "Where all loners can be lonely together"
    scroll_text("Where all loners can be lonely together", width=80, delay=0.1)
#ACTUAL CODE STARTS HERE!!
print("Welcome to HobbyHotspot!")
print("Feel free to input your City")
print("and be shown a list of all current users with the same hobbies as you!")
users_info_path = "users_info.txt"
while True:
    print("Would you like to make a new account[New account] or log in? [Log in]")
    user_input=input("> ").capitalize()
    if user_input == "New account":
        user , hobbies = new_account()
        write_users_to_txt(user,hobbies,users_info_path)
    elif user_input == "Log in":
        current_user,city=log_user_in(users_info_path)
        print(f"Current User {current_user}")
        logged_in=True
        while logged_in:
            print("Would You Like to View all users near you with the same hobbies [View],Look at your hobbies [Look], or log out [Logout]?")
            user_input = input("> ").capitalize()
            if user_input == "Look":
                show_user_hobbies(users_info_path,current_user)
                while True:
                    print("Would you like to update your hobbies? Yes[Yes] or No[No].")
                    user_input = input("> ").capitalize()
                    if user_input == "Yes":
                        update_user_hobbies(users_info_path,current_user)
                    elif user_input == "No":
                        break
    
            elif user_input == "Logout":
                print("Logging out...")
                logged_in = False
            elif user_input == "View":
                show_users_in_same_city(users_info_path,city)