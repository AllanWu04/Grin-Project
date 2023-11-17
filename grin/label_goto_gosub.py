from grin.token import GrinTokenKind
from grin.grinconversion import *
from grin.addsub import *
from grin.multdiv import *

def label_line(lines):
    """Returns a dictionary of labels with corresponding line number its on"""
    dict_of_labels = dict()
    for line in lines:
        if line[0].kind() == GrinTokenKind.IDENTIFIER and line[1].kind() == GrinTokenKind.COLON:
            dict_of_labels.update({line[0].text(): line[0].location().line()})
    return dict_of_labels

def encountered_label_line(line, dict_of_values):
    """Interprets what occurs after the label"""
    if line[0].kind() == GrinTokenKind.LET:
        let_conversion(line, dict_of_values)
    elif line[0].kind() == GrinTokenKind.PRINT:
        print_conversion(line, dict_of_values)
    elif line[0].kind() == GrinTokenKind.INNUM or line[0].kind() == GrinTokenKind.INSTR:
        instr_and_innum_conversion(line, dict_of_values)
    elif line[0].kind() == GrinTokenKind.ADD:
        add = Addition(line, dict_of_values)
        add.add_values()
    elif line[0].kind() == GrinTokenKind.MULT:
        mult = Multiplication(line, dict_of_values)
        mult.multiply_values()
    elif line[0].kind() == GrinTokenKind.DIV:
        div = Division(line, dict_of_values)
        div.divide_values()



