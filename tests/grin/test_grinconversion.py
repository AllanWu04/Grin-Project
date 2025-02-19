import unittest
from grin.grinconversion import *
from grin.readinput import *
class TestGrinConversion(unittest.TestCase):

    def test_let_conversion(self):
        user_values = ["LET NAME \"Boo\"", "LET AGE 13.015625"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"NAME": 'Boo', "AGE": 13.015625}
        self.assertEqual(all_values, compare)

    def test2_let_conversion(self):
        user_values = ["LET TEST \"DOG\"", "LET X 10", "LET TEST X"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"TEST": 10, "X": 10}
        self.assertEqual(all_values, compare)

    def test3_let_conversion(self):
        user_values = ["LET T1 0", "LET T2 5", "LET T3 T1"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"T1": 0, "T2": 5, "T3": 0}
        self.assertEqual(all_values, compare)

    def test4_let_conversion(self):
        user_values = ["LET A \"Hello\"", "LET B 10", "LET C B", "LET D \"Dog\"", "LET E D"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"A": "Hello", "B": 10, "C": 10, "D": "Dog", "E": "Dog"}
        self.assertEqual(all_values, compare)

    def test5_let_conversion(self):
        user_values = ["LET A B"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
        compare = {"A": 0, "B": 0}
        self.assertEqual(all_values, compare)
    def test_print_conversion(self):
        user_values = ["PRINT \"Hello Boo!\""]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                values_to_print.append(print_conversion(line, all_values))
        compare = ["Hello Boo!"]
        self.assertEqual(values_to_print, compare)

    def test2_print_conversion(self):
        user_values = ["LET X \"Boo\"", "LET Y 13.015625", "PRINT X", "PRINT Y"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                values_to_print.append(print_conversion(line, all_values))
        compare = ["Boo", 13.015625]
        self.assertEqual(values_to_print, compare)

    def test3_print_conversion(self):
        user_values = ["PRINT 4", "PRINT 11.25", "PRINT \"Dog\"", "PRINT \"Cat\"", "PRINT \"Hi\""]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                values_to_print.append(print_conversion(line, all_values))
        compare = [4, 11.25, "Dog", "Cat", "Hi"]
        self.assertEqual(values_to_print, compare)

    def test4_print_conversion(self):
        user_values = ["PRINT 4", "PRINT 11.25", "PRINT 0", "PRINT \"Hi\""]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                values_to_print.append(print_conversion(line, all_values))
        compare = [4, 11.25, 0, "Hi"]
        self.assertEqual(values_to_print, compare)
    def test_instr_innum_conversion(self):
        user_values = ["INNUM X"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": 11}
        self.assertEqual(all_values, compare)

    def test2_instr_innum_conversion(self):
        user_values = ["INSTR X"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": "Hello"}
        self.assertEqual(all_values, compare)

    def test3_instr_innum_conversion(self):
        user_values = ["INNUM X"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.LET:
                let_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.PRINT:
                print_conversion(line, all_values)
            elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
                instr_and_innum_conversion(line, all_values)
        compare = {"X": 92.3}
        self.assertEqual(all_values, compare)