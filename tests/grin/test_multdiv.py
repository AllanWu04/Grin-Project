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
            print_conversion(line, all_values, values_to_print)
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


class TestMultDiv(unittest.TestCase):
    pass
