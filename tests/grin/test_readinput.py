from grin.lexing import to_tokens, GrinLexError, KEYWORDS
from grin.location import GrinLocation
from grin.token import GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError
from grin.readinput import *
from typing import Iterable
import unittest

class TestInputValues(unittest.TestCase):
    def test_take_user_grin_input(self):
        print_message = take_user_grin_input()
        compare = ["LET a \"Boo\"", "PRINT a"]
        self.assertEqual(print_message, compare)

    def test2_take_user_grin_input(self):
        print_message = take_user_grin_input()
        compare = []
        self.assertEqual(print_message, compare)

    def test_convert_grin_token(self):
        grin_values = take_user_grin_input()
        convert = convert_to_grin_tokens(grin_values)
        check_if_token_obj = convert[0][0]
        self.assertEqual(type(check_if_token_obj), GrinToken)

    def test2_convert_grin_token(self):
        grin_values = take_user_grin_input()
        convert = convert_to_grin_tokens(grin_values)
        self.assertRaises(GrinParseError)