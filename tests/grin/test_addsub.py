import unittest
from grin.grinconversion import *
from grin.readinput import *
from grin.addsub import *


class ArithmeticTesting(unittest.TestCase):

    def test_add_values(self):
        user_values = ["LET X 10", "ADD X 5", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": 15}
        self.assertEqual(compare, all_values)

    def test2_add_values(self):
        user_values = ["LET X 10", "LET Y 5", "ADD X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": 15, "Y": 5}
        self.assertEqual(compare, all_values)

    def test3_add_values(self):
        user_values = ["LET X 10", "ADD X 4.52", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": 14.52}
        self.assertEqual(compare, all_values)

    def test4_add_values(self):
        user_values = ["LET X 4.52", "LET Y 10", "ADD X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": 14.52, "Y": 10}
        self.assertEqual(compare, all_values)

    def test5_add_values(self):
        user_values = ["LET X \"DOG\"", "ADD X \"CAT\"", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": "DOGCAT"}
        self.assertEqual(compare, all_values)

    def test6_add_values(self):
        user_values = ["LET X \"DOG\"", "LET Y \"CAT\"", "ADD X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
        compare = {"X": "DOGCAT", "Y": "CAT"}
        self.assertEqual(compare, all_values)

    def test7_add_values(self):
        user_values = ["ADD X Y", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
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
            self.assertEqual({"X": 0, "Y": 0}, all_values)
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test_subtract_values(self):
        user_values = ["LET X 15", "SUB X 30", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
            elif line[0].kind() == GrinTokenKind.SUB:
                sub = Subtraction(line, all_values)
                sub.subtract_values()
        self.assertEqual({"X": -15}, all_values)
        for i in values_to_print:
            print(i)

    def test2_subtract_values(self):
        user_values = ["LET X 15", "LET Y 30", "SUB X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
            elif line[0].kind() == GrinTokenKind.SUB:
                sub = Subtraction(line, all_values)
                sub.subtract_values()
        self.assertEqual({"X": -15, "Y": 30}, all_values)
        for i in values_to_print:
            print(i)

    def test3_subtract_values(self):
        user_values = ["LET X 35", "SUB X 40.5", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
            elif line[0].kind() == GrinTokenKind.SUB:
                sub = Subtraction(line, all_values)
                sub.subtract_values()
        self.assertEqual({"X": -5.5}, all_values)
        for i in values_to_print:
            print(i)

    def test4_subtract_values(self):
        user_values = ["LET X 35", "LET Y 40.5", "SUB X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
            elif line[0].kind() == GrinTokenKind.SUB:
                sub = Subtraction(line, all_values)
                sub.subtract_values()
        self.assertEqual({"X": -5.5, "Y": 40.5}, all_values)
        for i in values_to_print:
            print(i)

    def test5_subtract_values(self):
        user_values = ["SUB X Y", "."]
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
            elif line[0].kind() == GrinTokenKind.ADD:
                add = Addition(line, all_values)
                add.add_values()
            elif line[0].kind() == GrinTokenKind.SUB:
                sub = Subtraction(line, all_values)
                sub.subtract_values()
        self.assertEqual({"X": 0, "Y": 0}, all_values)
        for i in values_to_print:
            print(i)

    def test6_subtract_values(self):
        user_values = ["LET X \"BOO\"", "SUB X Y", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
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
        except RuntimeError:
            self.assertRaises(RuntimeError)

    def test7_subtract_values(self):
        user_values = ["LET X \"BOO\"", "SUB X \"DOG\"", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        values_to_print = []
        try:
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
        except RuntimeError:
            self.assertRaises(RuntimeError)