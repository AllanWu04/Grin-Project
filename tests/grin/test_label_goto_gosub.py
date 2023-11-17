import unittest
from grin.label_goto_gosub import *
from grin.readinput import *

class TestLabelGoSubGoTo(unittest.TestCase):

    def test_label_line(self):
        user_values = ["LET A 5", "LET B 4", "ADD A B", "TEST: LET X 4.25"]
        convert_tokens = convert_to_grin_tokens(user_values)
        label_dict = label_line(convert_tokens)
        self.assertEqual(label_dict, {"TEST": 4})

    def test2_label_line(self):
        user_values = ["LET A 5", "TEST: LET B 4", "ADD A B", "TEST2: LET X 4.25"]
        convert_tokens = convert_to_grin_tokens(user_values)
        label_dict = label_line(convert_tokens)
        self.assertEqual(label_dict, {"TEST": 2, "TEST2": 4})

