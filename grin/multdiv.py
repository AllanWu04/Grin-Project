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