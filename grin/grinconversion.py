from grin.readinput import *
from grin.location import GrinLocation
from grin.token import GrinTokenCategory, GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError


def let_conversion(line, values):
    """Returns a dictionary that contain the variable and the value it's assigned"""
    if line[2].kind() == GrinTokenKind.LITERAL_STRING:
        values.update({line[1].text(): line[2].value()})
    elif line[2].kind() == GrinTokenKind.LITERAL_INTEGER:
        values.update({line[1].text(): int(line[2].text())})
    elif line[2].kind() == GrinTokenKind.LITERAL_FLOAT:
        values.update({line[1].text(): float(line[2].text())})
    else:
        looping_copy = dict(values)
        for key, value in looping_copy.items():
            values.update({line[1].text(): value})
    return values


def print_conversion(line, dict_of_values, values_to_print):
    """Returns a list of values that want to be printed and also prints values."""
    if line[1].kind() == GrinTokenKind.LITERAL_FLOAT or line[1].kind() == GrinTokenKind.LITERAL_INTEGER or line[1].kind() == GrinTokenKind.LITERAL_STRING:
        values_to_print.append(line[1].value())
    else:
        for key, value in dict_of_values.items():
            if line[1].text() == key:
                values_to_print.append(value)
    return values_to_print


def instr_and_innum_conversion(line, dict_of_values):
    """Returns a list of inputs through INSTR and INNUM"""
    if line[0].kind() == GrinTokenKind.INNUM:
        take_int_float = input()
        if '.' in take_int_float:
            convert_to_float = float(take_int_float)
            dict_of_values.update({line[1].text(): convert_to_float})
        else:
            convert_to_int = int(take_int_float)
            dict_of_values.update({line[1].text(): convert_to_int})
    else:
        take_str = input()
        dict_of_values.update({line[1].text(): take_str})
    return dict_of_values
