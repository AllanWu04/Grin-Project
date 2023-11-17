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

    def jump_lines(self, dict_of_values, dict_of_labels) -> int:
        """Performs a jump to a value"""
        if self._value[1].kind() == GrinTokenKind.LITERAL_INTEGER:
            pass_max_lines = self._line_pointer + self._value[1].value() > len(self._total_commands)
            too_negative_line = self._line_pointer + self._value[1].value() < 0
            if self._value[1].value() == 0 or pass_max_lines or too_negative_line:
                raise InvalidLineError
            else:
                self._line_pointer += self._value[1].value()
                return self._line_pointer
        elif self._value[1].kind() == GrinTokenKind.LITERAL_STRING:
            valid_label = self._value[1].value() in dict_of_labels.keys()
            get_line_of_label = dict_of_labels.get(self._value[1].value())
            if not valid_label:
                raise InvalidLineError
            else:
                self._line_pointer = get_line_of_label - 1
                return self._line_pointer
        elif self._value[1].kind() == GrinTokenKind.IDENTIFIER:
            identifier_exists = self._value[1].text() in dict_of_values.keys()
            if not identifier_exists:
                raise InvalidLineError
            check_identifier = dict_of_values.get(self._value[1].text())
            if type(check_identifier) == float:
                raise InvalidLineError
            elif type(check_identifier) == int:
                if check_identifier == 0:
                    raise InvalidLineError
                else:
                    self._line_pointer += check_identifier
                    return self._line_pointer
            else:
                not_in_label_dict = check_identifier not in dict_of_labels.keys()
                if not_in_label_dict:
                    raise InvalidLineError
                else:
                    self._line_pointer = dict_of_labels.get(check_identifier) - 1
                    return self._line_pointer

    def perform_operation_with_literal(self, get_comparison_operator, dict_copy) -> bool:
        """Returns a Boolean of the comparison of values"""
        if get_comparison_operator == GrinTokenKind.GREATER_THAN:
            return dict_copy.get(self._condition[1].text()) > self._condition[3].value()
        elif get_comparison_operator == GrinTokenKind.LESS_THAN:
            return dict_copy.get(self._condition[1].text()) < self._condition[3].value()
        elif get_comparison_operator == GrinTokenKind.GREATER_THAN_OR_EQUAL:
            return dict_copy.get(self._condition[1].text()) >= self._condition[3].value()
        elif get_comparison_operator == GrinTokenKind.LESS_THAN_OR_EQUAL:
            return dict_copy.get(self._condition[1].text()) <= self._condition[3].value()
        elif get_comparison_operator == GrinTokenKind.EQUAL:
            return dict_copy.get(self._condition[1].text()) == self._condition[3].value()
        elif get_comparison_operator == GrinTokenKind.NOT_EQUAL:
            return dict_copy.get(self._condition[1].text()) != self._condition[3].value()

    def perform_operation_with_identifier(self, get_comparison_operator, dict_copy) -> bool:
        """Returns a Boolean of comparison of identifiers"""
        if get_comparison_operator == GrinTokenKind.GREATER_THAN:
            return dict_copy.get(self._condition[1].text()) > dict_copy.get(self._condition[3].text())
        elif get_comparison_operator == GrinTokenKind.LESS_THAN:
            return dict_copy.get(self._condition[1].text()) < dict_copy.get(self._condition[3].text())
        elif get_comparison_operator == GrinTokenKind.GREATER_THAN_OR_EQUAL:
            return dict_copy.get(self._condition[1].text()) >= dict_copy.get(self._condition[3].text())
        elif get_comparison_operator == GrinTokenKind.LESS_THAN_OR_EQUAL:
            return dict_copy.get(self._condition[1].text()) <= dict_copy.get(self._condition[3].text())
        elif get_comparison_operator == GrinTokenKind.EQUAL:
            return dict_copy.get(self._condition[1].text()) == dict_copy.get(self._condition[3].text())
        elif get_comparison_operator == GrinTokenKind.NOT_EQUAL:
            return dict_copy.get(self._condition[1].text()) != dict_copy.get(self._condition[3].text())


    def check_condition(self, dict_of_values) -> bool:
        """Checks to see what condition has to be met to execute."""
        if self._condition is False:
            return True
        if self._condition[0].kind() == GrinTokenKind.IF:
            dict_copy = dict(dict_of_values)
            get_comparison_operator = self._condition[2].kind()
            check_value1_exist = self._condition[1].text() not in dict_copy.keys() and self._condition[1].kind() == GrinTokenKind.IDENTIFIER
            check_value2_exist = self._condition[3].text() not in dict_copy.keys() and self._condition[3].kind() == GrinTokenKind.IDENTIFIER
            if check_value1_exist:
                dict_of_values.update({self._condition[1].text(): 0})
            if check_value2_exist:
                dict_of_values.update({self._condition[3].text(): 0})
            if type(dict_of_values.get(self._condition[1].text())) == str or self._condition[1].kind() == GrinTokenKind.LITERAL_STRING:
                get_kind_compare_value = self._condition[3].kind()
                if get_kind_compare_value == GrinTokenKind.LITERAL_STRING:
                    return self.perform_operation_with_literal(get_comparison_operator, dict_of_values)
                elif get_kind_compare_value == GrinTokenKind.IDENTIFIER:
                    get_identifier_value = dict_of_values.get(self._condition[3].text())
                    if type(get_identifier_value) == str:
                        return self.perform_operation_with_identifier(get_comparison_operator, dict_of_values)
                    else:
                        raise RuntimeError
                else:
                    raise RuntimeError
            else:
                get_kind_compare_value = self._condition[3].kind()
                if get_kind_compare_value == GrinTokenKind.LITERAL_INTEGER or get_kind_compare_value == GrinTokenKind.LITERAL_FLOAT:
                    return self.perform_operation_with_literal(get_comparison_operator, dict_of_values)
                elif get_kind_compare_value == GrinTokenKind.IDENTIFIER:
                    get_identifier_value = dict_of_values.get(self._condition[3].text())
                    if type(get_identifier_value) == int or type(get_identifier_value) == float:
                        return self.perform_operation_with_identifier(get_comparison_operator, dict_of_values)
                    else:
                        raise RuntimeError
                else:
                    raise RuntimeError

