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


class InvalidLineError(Exception):
    pass
class GoTo:
    """Performs a jump according to a given label, line number, or int variable"""
    def __init__(self, line, total_commands, line_pointer):
        self._value = line
        self._total_commands = total_commands
        self._line_pointer = line_pointer
        if len(self._value) == 2:
            self._condition = False
        else:
            self._condition = self._value[2:]

    def jump_lines(self, dict_of_values, dict_of_labels) -> None:
        """Performs a jump to a value"""
        if self._value[1].kind() == GrinTokenKind.LITERAL_INTEGER:
            pass_max_lines = self._line_pointer + self._value[1].value() > len(self._total_commands)
            too_negative_line = self._line_pointer + self._value[1].value() < 0
            print(self._line_pointer + self._value[1].value())
            if self._value[1].value() == 0 or pass_max_lines or too_negative_line:
                raise InvalidLineError
            else:
                self._line_pointer += self._value[1].value()
                get_line_jumped = self._total_commands[self._line_pointer:]
                for line in get_line_jumped:
                    encountered_label_line(line, dict_of_values)
                    self._line_pointer = line[0].location().line()
                    if line[0].kind() == GrinTokenKind.IDENTIFIER and line[1].kind() == GrinTokenKind.COLON:
                        encountered_label_line(line, self._total_commands)
                    elif line[0].kind() == GrinTokenKind.GOTO:
                        self.jump_lines(dict_of_values, dict_of_labels)
                    elif line[0].kind() == GrinTokenKind.END or line[0].kind() == GrinTokenKind.DOT:
                        break
