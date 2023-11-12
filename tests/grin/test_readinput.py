from grin.lexing import to_tokens, GrinLexError, KEYWORDS
from grin.location import GrinLocation
from grin.token import GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError
from grin.readinput import *
import unittest

class TestInputValues(unittest.TestCase):
    def test_input_print_message(self):
        print_message = take_user_grin_input()
        compare = ["LET a \"Boo\"", "PRINT a"]
        self.assertEqual(print_message, compare)

    def test2_input_print_message(self):
        print_message = take_user_grin_input()
        compare = []
        self.assertEqual(print_message, compare)

