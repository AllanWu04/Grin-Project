import unittest
from grin.grinconversion import *
from grin.readinput import *
from grin.addsub import *
from grin.multdiv import *


def test_mult_skeleton(convert_tokens, values_to_print, all_values):
    for line in convert_tokens:
        if line[0].kind() == GrinTokenKind.LET:
            let_conversion(line, all_values)
        elif line[0].kind() == GrinTokenKind.PRINT:
            print_conversion(line, all_values)
        elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
            instr_and_innum_conversion(line, all_values)
        elif line[0].kind() == GrinTokenKind.ADD:
            add = Addition(line, all_values)
            add.add_values()
        elif line[0].kind() == GrinTokenKind.SUB:
            sub = Subtraction(line, all_values)
            sub.subtract_values()
        elif line[0].kind() == GrinTokenKind.MULT:
            mult = Multiplication(line, all_values)
            mult.multiply_values()


class TestMultDiv(unittest.TestCase):

    def test_multiply_values(self):
        user_values = ["LET X 2", "MULT X 3", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": 6}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test2_multiply_values(self):
        user_values = ["LET X 3", "MULT X 7.2", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": 21.6}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test3_multiply_values(self):
        user_values = ["LET X 3", "MULT X \"BOO\"", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": "BOOBOOBOO"}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test4_multiply_values(self):
        user_values = ["LET X \"BOO\"", "MULT X 4.3", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test5_multiply_values(self):
        user_values = ["LET X 5.3", "MULT X \"BOO\"", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test6_multiply_values(self):
        user_values = ["LET X \"DOG\"", "MULT X 2", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": "DOGDOG"}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test7_multiply_values(self):
        user_values = ["LET X DOG", "MULT X 3.4", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test8_multiply_values(self):
        user_values = ["MULT X Y", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": 0, "Y": 0}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test9_multiply_values(self):
        user_values = ["LET X 1.25", "LET Y 2", "MULT X Y", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": 2.5, "Y": 2}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test10_multiply_values(self):
        user_values = ["LET X \"BOO\"", "LET Y 4", "MULT X Y"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
            self.assertEqual({"X": "BOOBOOBOOBOO", "Y": 4}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test11_multiply_values(self):
        user_values = ["LET X \"BOO\"", "LET Y 4.32", "MULT X Y", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
            test_mult_skeleton(convert_tokens, values_to_print, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)