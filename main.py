# inputs as strings
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#convert strings into integer and float
weight_new = int(weight)
height_new = float(height)

# Formula
# Using the exponent operator **
bmi = weight_new / height_new ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)



























#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open("testing_copy.py", "w") as file:
  file.write("def test_func():\n")
  with open("main.py", "r") as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer=['2', '8'], expected_print='2\n')

  def test_2(self):
    self.run_test(given_answer=['1.8', '85'], expected_print='26\n')

  def test_3(self):
    self.run_test(given_answer=['1.6', '90'], expected_print='35\n')


print("\n\n\n.\n.\n.")
print('Checking if you are printing a single number: \n The BMI as an integer (using meters and kilograms)...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 
