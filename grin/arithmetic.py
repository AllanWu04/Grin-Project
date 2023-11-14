from grin.token import GrinTokenKind, GrinToken


class Arithmetic:
    """Performs operation according to first token"""
    def __init__(self, line):
        self._line = line

    def operation(self):
        return self._line[0].kind()


class Addition(Arithmetic):
    """Performs the addition operator with two values"""
    def __init__(self, line, dict_of_values):
        super().__init__(line)
        self._dict_of_values = dict_of_values
        self._addvalue1kind = line[1].kind()
        self._addvalue2kind = line[2].kind()

    def add_values(self):
        """Adds corresponding values as long as they follow designated rules"""
        if self.operation() == GrinTokenKind.ADD:
            if self._line[1].text() not in self._dict_of_values.keys() and self._addvalue1kind == GrinTokenKind.IDENTIFIER:
                if type(self._line[2].value()) == str:
                    raise RuntimeError
                else:
                    self._dict_of_values.update({self._line[1].text(): 0})
            if self._line[2].text() not in self._dict_of_values.keys() and self._addvalue2kind == GrinTokenKind.IDENTIFIER:
                self._dict_of_values.update({self._line[2].text(): 0})
            if self._addvalue2kind == GrinTokenKind.LITERAL_INTEGER or self._addvalue2kind == GrinTokenKind.LITERAL_FLOAT:
                dict_copy = dict(self._dict_of_values)
                for key, value in dict_copy.items():
                    if key == self._line[1].text() and (type(value) == int or type(value) == float):
                        self._dict_of_values.update({key: value + self._line[2].value()})
            elif self._addvalue2kind == GrinTokenKind.LITERAL_STRING:
                dict_copy = dict(self._dict_of_values)
                for key, value in dict_copy.items():
                    if key == self._line[1].text() and type(value) == str:
                        self._dict_of_values.update({key: value + self._line[2].value()})
            else:
                dict_copy = dict(self._dict_of_values)
                for key, value in dict_copy.items():
                    if key == self._line[1].text() and (type(self._dict_of_values.get(self._line[2].text())) == type(value)
                                                        or (type(self._dict_of_values.get(self._line[2].text())) == int and type(value) == float)
                                                        or (type(self._dict_of_values.get(self._line[2].text())) == float and type(value) == int)):
                        self._dict_of_values.update({key: value + self._dict_of_values.get(self._line[2].text())})







