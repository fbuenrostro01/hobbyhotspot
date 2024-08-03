import unittest
import os
from io import StringIO
from unittest.mock import patch

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
        "Running", "Cycling", "Swimming", "Knitting or crocheting", "Playing sports",
        "Playing video games", "Bird watching", "Dancing", "Yoga", "Crafting"
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

class TestUserFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with sample data
        self.test_file_path = 'test_users_info.txt'
        with open(self.test_file_path, 'w') as f:
            f.write("""Username: alice
Hobby #1: Reading
Hobby #2: Hiking

Username: bob
Hobby #1: Cooking
Hobby #2: Cycling

First Name: Charlie
Last Name: Brown
Username: charlieb
City: New York

First Name: Alice
Last Name: Johnson
Username: alicej
City: New York

First Name: David
Last Name: Davis
Username: davidd
City: Chicago
""")

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_show_user_hobbies(self):
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        show_user_hobbies(self.test_file_path, 'alice')
        sys.stdout = sys.__stdout__

        expected_output = "alice's hobbies:\n- Reading\n- Hiking\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_user_hobbies(self.test_file_path, 'bob')
        sys.stdout = sys.__stdout__

        expected_output = "bob's hobbies:\n- Cooking\n- Cycling\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_user_hobbies(self.test_file_path, 'charlie')
        sys.stdout = sys.__stdout__

        expected_output = "No hobbies found for charlie.\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['Reading', 'Traveling', 'Cooking'])
    def test_update_user_hobbies(self, mock_input):
        update_user_hobbies(self.test_file_path, 'alicej')

        with open(self.test_file_path, 'r') as f:
            updated_content = f.read()
        
        expected_content = """Username: alice
Hobby #1: Reading
Hobby #2: Traveling
Hobby #3: Cooking

Username: bob
Hobby #1: Cooking
Hobby #2: Cycling

First Name: Charlie
Last Name: Brown
Username: charlieb
City: New York

First Name: Alice
Last Name: Johnson
Username: alicej
City: New York

First Name: David
Last Name: Davis
Username: davidd
City: Chicago
"""
        self.assertEqual(updated_content, expected_content)

    def test_show_users_in_same_city(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        show_users_in_same_city(self.test_file_path, 'New York')
        sys.stdout = sys.__stdout__

        expected_output = "Users in New York:\n- Charlie Brown (Username: charlieb)\n- Alice Johnson (Username: alicej)\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_users_in_same_city(self.test_file_path, 'San Francisco')
        sys.stdout = sys.__stdout__

        expected_output = "No users found in San Francisco.\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()