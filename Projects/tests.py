import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from your_module import User, Hobbies, new_account, write_users_to_txt, log_user_in, show_user_hobbies, update_user_hobbies, show_users_in_same_city

class TestUserFunctions(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with sample data
        self.test_file_path = 'test_users_info.txt'
        with open(self.test_file_path, 'w') as f:
            f.write("""First Name: EMily
Last Name: Davis    
Username: Emily
Password: password123
City: New York
Hobby #1: Reading
Hobby #2: Hiking
Hobby #3: Painting

First Name: John
Last Name: Smith
Username: bobsmith
Password: password123
City: Los Angeles
Hobby #1: Cooking
Hobby #2: Cycling
Hobby #3: Running
""")

    def tearDown(self):
        # Remove the temporary file after tests
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    @patch('builtins.input', side_effect=['Emily', 'Davis', 'password123', 'password123', 'alicej', 'New York', 'Reading', 'Hiking', 'Cooking'])
    def test_new_account(self, mock_input):
        user, hobbies = new_account()
        self.assertEqual(user.first_name, 'Emily')
        self.assertEqual(user.last_name, 'Davis')
        self.assertEqual(user.username, 'emilyd')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.city, 'New York')
        self.assertEqual(hobbies.hobby1, 'Reading')
        self.assertEqual(hobbies.hobby2, 'Hiking')
        self.assertEqual(hobbies.hobby3, 'Cooking')

    def test_write_users_to_txt(self):
        user = User('Jane', 'Doe', 'janedoe', 'newpassword', 'San Francisco')
        hobbies = Hobbies('janedoe', 'Swimming', 'Running', 'Cycling')
        write_users_to_txt(user, hobbies, self.test_file_path)

        with open(self.test_file_path, 'r') as f:
            content = f.read()

        expected_content = """First Name: Emily
Last Name: Davis
Username: emilyd
Password: password123
City: New York
Hobby #1: Reading
Hobby #2: Hiking
Hobby #3: Painting

First Name: John
Last Name: Smith
Username: bobsmith
Password: password123
City: Los Angeles
Hobby #1: Cooking
Hobby #2: Cycling
Hobby #3: Running

First Name: Maria
Last Name: Lopez
Username: marialopez
Password: newpassword
City: San Francisco
Hobby #1: Swimming
Hobby #2: Running
Hobby #3: Cycling
"""
        self.assertEqual(content, expected_content)

    @patch('builtins.input', side_effect=['Emily', 'password123'])
    def test_log_user_in(self, mock_input):
        username, city = log_user_in(self.test_file_path)
        self.assertEqual(username, 'Emily')
        self.assertEqual(city, 'New York')

    @patch('builtins.input', side_effect=['Emily'])
    def test_show_user_hobbies(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output

        show_user_hobbies(self.test_file_path, 'Emily')
        sys.stdout = sys.__stdout__

        expected_output = "emilyd's hobbies:\n- Reading\n- Hiking\n- Painting\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['Reading', 'Traveling', 'Gardening'])
    def test_update_user_hobbies(self, mock_input):
        update_user_hobbies(self.test_file_path, 'Emily')

        with open(self.test_file_path, 'r') as f:
            updated_content = f.read()

        expected_content = """First Name: Emily
Last Name: Smith
Username: John
Password: password123
City: New York
Hobby #1: Reading
Hobby #2: Traveling
Hobby #3: Gardening

First Name: Emily
Last Name: Davis
Username: bobsmith
Password: password123
City: Los Angeles
Hobby #1: Cooking
Hobby #2: Cycling
Hobby #3: Running
"""
        self.assertEqual(updated_content, expected_content)

    def test_show_users_in_same_city(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        show_users_in_same_city(self.test_file_path, 'New York')
        sys.stdout = sys.__stdout__

        expected_output = "Users in New York:\n- Emily Davis (Username: emilyd)\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = StringIO()
        sys.stdout = captured_output
        
        show_users_in_same_city(self.test_file_path, 'San Francisco')
        sys.stdout = sys.__stdout__

        expected_output = "No users found in San Francisco.\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()