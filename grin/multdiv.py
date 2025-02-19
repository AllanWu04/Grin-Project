from grin.addsub import Arithmetic
from grin.token import GrinTokenKind

class Multiplication(Arithmetic):
    """Performs multiplication operation with two values"""
    def __init__(self, line, dict_of_values):
        super().__init__(line)
        self._dict_of_values = dict_of_values
        self._multvalue1kind = self._line[1].kind()
        self._multvalue2kind = self._line[2].kind()

    def multiply_values(self):
        """Multiplies corresponding values as long as they follow designated rules"""
        if self.operation() == GrinTokenKind.MULT:
            if self._line[1].text() not in self._dict_of_values.keys() and self._multvalue1kind == GrinTokenKind.IDENTIFIER:
                self._dict_of_values.update({self._line[1].text(): 0})
            if self._line[2].text() not in self._dict_of_values.keys() and self._multvalue2kind == GrinTokenKind.IDENTIFIER:
                self._dict_of_values.update({self._line[2].text(): 0})
            if self._multvalue2kind == GrinTokenKind.LITERAL_FLOAT or self._multvalue2kind == GrinTokenKind.LITERAL_INTEGER:
                dict_copy = dict(self._dict_of_values)
                if self._multvalue2kind == GrinTokenKind.LITERAL_INTEGER:
                    for key, value in dict_copy.items():
                        if key == self._line[1].text():
                            self._dict_of_values.update({key: value * self._line[2].value()})
                else:
                    check_str = type(dict_copy.get(self._line[1].text())) == str
                    if check_str:
                        raise RuntimeError
                    for key, value in dict_copy.items():
                        if key == self._line[1].text():
                            self._dict_of_values.update({key: value * self._line[2].value()})
            elif self._multvalue2kind == GrinTokenKind.LITERAL_STRING:
                dict_copy = dict(self._dict_of_values)
                check_float = type(dict_copy.get(self._line[1].text())) == float
                if check_float:
                    raise RuntimeError
                for key, value in dict_copy.items():
                    if key == self._line[1].text():
                        self._dict_of_values.update({key: value * self._line[2].value()})
            else:
                dict_copy = dict(self._dict_of_values)
                check_invalid1 = type(dict_copy.get(self._line[1].text())) == float and type(
                    dict_copy.get(self._line[2].text())) == str
                check_invalid2 = type(dict_copy.get(self._line[1].text())) == str and type(
                    dict_copy.get(self._line[2].text())) == float
                if check_invalid1 or check_invalid2:
                    raise RuntimeError
                for key, value in dict_copy.items():
                    if key == self._line[1].text():
                        self._dict_of_values.update({key: value * self._dict_of_values.get(self._line[2].text())})

class Division(Arithmetic):
    """Performs division operation with two values"""
    def __init__(self, line, dict_of_values):
        super().__init__(line)
        self._dict_of_values = dict_of_values
        self._multvalue1kind = self._line[1].kind()
        self._multvalue2kind = self._line[2].kind()

    def divide_values(self):
        if self.operation() == GrinTokenKind.DIV:
            if self._line[1].text() not in self._dict_of_values.keys() and self._multvalue1kind == GrinTokenKind.IDENTIFIER:
                self._dict_of_values.update({self._line[1].text(): 0})
            not_existing_identifier = self._line[2].text() not in self._dict_of_values and self._multvalue2kind == GrinTokenKind.IDENTIFIER
            if self._multvalue2kind == GrinTokenKind.LITERAL_STRING or not_existing_identifier:
                raise RuntimeError
            elif self._multvalue2kind == GrinTokenKind.LITERAL_FLOAT or self._multvalue2kind == GrinTokenKind.LITERAL_INTEGER:
                dict_copy = dict(self._dict_of_values)
                str_first_val = type(dict_copy.get(self._line[1].text())) == str
                check_if_zero = self._line[2].value() == 0 or self._line[2].value == 0.0
                check_int = type(dict_copy.get(self._line[1].text())) == int or type(dict_copy.get(self._line[2].text())) == int
                if check_if_zero or str_first_val:
                    raise RuntimeError
                for key, value in dict_copy.items():
                    if key == self._line[1].text():
                        if check_int:
                            self._dict_of_values.update({key: value // self._line[2].value()})
                        else:
                            self._dict_of_values.update({key: value / self._line[2].value()})
            else:
                dict_copy = dict(self._dict_of_values)
                str_val = type(dict_copy.get(self._line[1].text())) == str or type(dict_copy.get(self._line[2].text())) == str
                check_int = type(dict_copy.get(self._line[1].text())) == int or type(dict_copy.get(self._line[2].text())) == int
                check_zero = dict_copy.get(self._line[2].text()) == 0 or dict_copy.get(self._line[2].text()) == 0.0
                if str_val or check_zero:
                    raise RuntimeError
                for key, value in dict_copy.items():
                    if key == self._line[1].text():
                        if check_int:
                            self._dict_of_values.update({key: value // self._dict_of_values.get(self._line[2].text())})
                        else:
                            self._dict_of_values.update({key: value / self._dict_of_values.get(self._line[2].text())})
