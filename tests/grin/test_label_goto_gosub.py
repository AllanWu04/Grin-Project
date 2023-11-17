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

    def test_encounter_label_line(self):
        user_values = ["TEST: LET A 5", "TEST2: LET B 10", "TEST3: ADD A B"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.IDENTIFIER and line[1].kind() == GrinTokenKind.COLON:
                get_label_command = line[2:]
                encountered_label_line(get_label_command, all_values)
        self.assertEqual(all_values, {"A": 15, "B": 10})

    def test2_encounter_label_line(self):
        user_values = ["TEST: LET A 5", "TEST2: PRINT A", "TEST3: MULT A 5",
                       "TEST4: INNUM B", "TEST5: DIV A B"]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        for line in convert_tokens:
            if line[0].kind() == GrinTokenKind.IDENTIFIER and line[1].kind() == GrinTokenKind.COLON:
                get_label_command = line[2:]
                encountered_label_line(get_label_command, all_values)
        self.assertEqual(all_values, {"A": 5, "B": 5})
