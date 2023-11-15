from grin.addsub import Arithmetic
from grin.token import GrinTokenKind

class Multiplication(Arithmetic):
    """Performs multiplication operation with two values"""
    def __init__(self, line, dict_of_values):
        super().__init__(line)
        self._dict_of_values = dict_of_values
        self._multvalue1kind = self._line[0].kind()
        self._multvalue2kind = self._line[0].kind()

