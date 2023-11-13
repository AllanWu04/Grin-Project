from grin.readinput import *
from grin.location import GrinLocation
from grin.token import GrinTokenCategory, GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError


def let_conversion(lines):
    """Returns a dictionary that contain the variable and the value it's assigned"""
    values = {}
    for line in lines:
        if line[0].kind() == GrinTokenKind.LET:
            if line[2].kind() == GrinTokenKind.LITERAL_STRING:
                values.update({line[1].text(): line[2].value()})
            elif line[2].kind() == GrinTokenKind.LITERAL_INTEGER:
                values.update({line[1].text(): int(line[2].text())})
            elif line[2].kind() == GrinTokenKind.LITERAL_FLOAT:
                values.update({line[1].text(): float(line[2].text())})
            else:
                looping_copy = dict(values)
                for key, value in looping_copy.items():
                    if key == line[2].text():  # If LET wants a new variable to be another variable value
                        values.update({line[1].text(): value})
                    else:  # If LET is making an existing variable to be an existing value
                        values.update({line[1].text(): value})
    return values


def print_conversion(lines):
    """Returns a list of values that want to be printed and also prints values."""
    lst_of_prints = []
    all_variables_dict = let_conversion(lines)
    for line in lines:
        if line[0].kind() == GrinTokenKind.PRINT:
            if line[1].kind() == GrinTokenKind.LITERAL_FLOAT or line[1].kind() == GrinTokenKind.LITERAL_INTEGER or line[1].kind() == GrinTokenKind.LITERAL_STRING:
                lst_of_prints.append(line[1].value())
            else:
                for key, value in all_variables_dict.items():
                    if line[1].text() == key:
                        lst_of_prints.append(value)
    for i in lst_of_prints:
        print(i)
    return lst_of_prints


def instr_and_innum_conversion(lines):
    """Returns a list of inputs through INSTR and INNUM"""
    current_values = let_conversion(lines)
    for line in lines:
        if line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
            if line[0].kind() == GrinTokenKind.INNUM:
                take_int_float = input()
                if '.' in take_int_float:
                    convert_to_float = float(take_int_float)
                    current_values.update({line[1].text(): convert_to_float})
                else:
                    convert_to_int = int(take_int_float)
                    current_values.update({line[1].text(): convert_to_int})
            else:
                take_str = input()
                current_values.update({line[1].text(): take_str})
    return current_values
