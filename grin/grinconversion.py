from grin.readinput import *
from grin.location import GrinLocation
from grin.token import GrinTokenCategory, GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError


def let_conversion(line, values) -> dict:
    """Returns a dictionary that contain the variable and the value it's assigned"""
    if line[2].kind() == GrinTokenKind.LITERAL_STRING:
        values.update({line[1].text(): line[2].value()})
    elif line[2].kind() == GrinTokenKind.LITERAL_INTEGER:
        values.update({line[1].text(): int(line[2].text())})
    elif line[2].kind() == GrinTokenKind.LITERAL_FLOAT:
        values.update({line[1].text(): float(line[2].text())})
    else:
        looping_copy = dict(values)
        if line[2].text() in looping_copy.keys():
            for key, value in looping_copy.items():
                if key == line[2].text():
                    values.update({line[1].text(): value})
        else:
            values.update({line[1].text(): 0})
            values.update({line[2].text(): 0})
    return values


def print_conversion(line, dict_of_values):
    """Prints value according to the line value"""
    if line[1].kind() == GrinTokenKind.LITERAL_FLOAT or line[1].kind() == GrinTokenKind.LITERAL_INTEGER or line[1].kind() == GrinTokenKind.LITERAL_STRING:
        print(line[1].value())
        return line[1].value()
    else:
        if line[1].text() in dict_of_values.keys():
            for key, value in dict_of_values.items():
                if line[1].text() == key:
                    print(value)
                    return value
        else:
            print(0)
            return 0


def instr_and_innum_conversion(line, dict_of_values) -> None:
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
