import unittest
from grin.grinconversion import *
from grin.readinput import *
class TestGrinConversion(unittest.TestCase):

    def test_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"NAME": 'Boo', "AGE": 13.015625}
        self.assertEqual(all_values, compare)

    def test2_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"TEST": 10, "X": 10}
        self.assertEqual(all_values, compare)

    def test3_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"T1": 0, "T2": 5, "T3": 0}
        self.assertEqual(all_values, compare)

    def test4_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"A": "Hello", "B": 10, "C": 10, "D": "Dog", "E": "Dog"}
        self.assertEqual(all_values, compare)

    def test5_let_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"A": 0}
        self.assertEqual(all_values, compare)
    def test_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
        compare = ["Hello Boo!"]
        self.assertEqual(values_to_print, compare)

    def test2_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
        compare = ["Boo", 13.015625]
        self.assertEqual(values_to_print, compare)

    def test3_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
        compare = [4, 11.25, "Dog", "Cat", "Hi"]
        self.assertEqual(values_to_print, compare)

    def test4_print_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
        compare = [4, 11.25, 0, "Hi"]
        self.assertEqual(values_to_print, compare)
    def test_instr_innum_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": 11}
        self.assertEqual(all_values, compare)

    def test2_instr_innum_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": "Hello"}
        self.assertEqual(all_values, compare)

    def test3_instr_innum_conversion(self):
        user_values = take_user_grin_input()
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values, values_to_print)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": 92.3}
        self.assertEqual(all_values, compare)