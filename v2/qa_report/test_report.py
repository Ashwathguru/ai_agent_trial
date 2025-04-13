#Positive test case:
import unittest
from unittest.mock import patch
from my_module import greet_user
class TestGreetUser(unittest.TestCase):
    @patch('builtins.input', side_effect=['Alice', '25'])
    def test_greet_user(self, mock_input):
        expected_output = "Hello Alice, you are 25 years old."
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            greet_user()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
#Negative test case:
import unittest
from unittest.mock import patch
from my_module import greet_user
class TestGreetUser(unittest.TestCase):
    @patch('builtins.input', side_effect=['', ''])
    def test_greet_user_empty_input(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            greet_user()
            self.assertEqual(mock_stdout.getvalue().strip(), "Hello , you are  years old.")