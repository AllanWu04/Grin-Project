import unittest
from grin.grinconversion import *
from grin.readinput import *
class TestGrinConversion(unittest.TestCase):

    def test_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = let_conversion(convert_tokens)
        compare = {"NAME": 'Boo', "AGE": 13.015625}
        self.assertEqual(dict_of_values, compare)

    def test2_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = let_conversion(convert_tokens)
        compare = {"TEST": 10, "X": 10}
        self.assertEqual(dict_of_values, compare)

    def test3_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = let_conversion(convert_tokens)
        compare = {"T1": 0, "T2": 5, "T3": 0}
        self.assertEqual(dict_of_values, compare)

    def test4_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = let_conversion(convert_tokens)
        compare = {"A": "Hello", "B": 10, "C": 10, "D": "Dog", "E": "Dog"}
        self.assertEqual(dict_of_values, compare)

    def test_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        print_lines = print_conversion(convert_tokens)
        compare = ["Hello Boo!"]
        self.assertEqual(print_lines, compare)

    def test2_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        print_lines = print_conversion(convert_tokens)
        compare = ["Boo", 13.015625]
        self.assertEqual(print_lines, compare)

    def test3_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        print_lines = print_conversion(convert_tokens)
        compare = [4, 11.25, "Dog", "Cat", "Hi"]
        self.assertEqual(print_lines, compare)

    def test_instr_innum_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = instr_and_innum_conversion(convert_tokens)
        compare = {"X": 11}
        self.assertEqual(dict_of_values, compare)

    def test2_instr_innum_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        dict_of_values = instr_and_innum_conversion(convert_tokens)
        compare = {"X": 13.5}
        self.assertEqual(dict_of_values, compare)