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

    def test_goto(self):
        user_values = ["LET A 1", "GOTO 2", "LET A 2", "PRINT A", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        all_labels = label_line(convert_tokens)
        line_pointer = 0
        while line_pointer < len(convert_tokens):
            if convert_tokens[line_pointer][0].kind() == GrinTokenKind.LET:
                let_conversion(convert_tokens[line_pointer], all_values)
                line_pointer += 1
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.PRINT:
                print_conversion(convert_tokens[line_pointer], all_values)
                line_pointer += 1
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.GOTO:
                goto_command = GoTo(convert_tokens[line_pointer], convert_tokens, line_pointer)
                new_index = goto_command.jump_lines(all_values, all_labels)
                line_pointer = new_index
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.END or convert_tokens[line_pointer][0].kind() == GrinTokenKind.DOT:
                break
        self.assertEqual(all_values, {"A": 1})

    def test2_goto(self):
        user_values = ["LET Z 5", "GOTO 5", "LET C 4", "PRINT C",
                       "PRINT Z", "END", "PRINT C", "PRINT Z", "GOTO -6", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        all_labels = label_line(convert_tokens)
        line_pointer = 0
        while line_pointer < len(convert_tokens):
            if convert_tokens[line_pointer][0].kind() == GrinTokenKind.LET:
                let_conversion(convert_tokens[line_pointer], all_values)
                line_pointer += 1
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.PRINT:
                print_conversion(convert_tokens[line_pointer], all_values)
                line_pointer += 1
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.GOTO:
                goto_command = GoTo(convert_tokens[line_pointer], convert_tokens, line_pointer)
                new_index = goto_command.jump_lines(all_values, all_labels)
                line_pointer = new_index
            elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.END or convert_tokens[line_pointer][0].kind() == GrinTokenKind.DOT:
                break
        self.assertEqual(all_values, {"C": 4, "Z": 5})

    def test3_goto(self):
        user_values = ["LET Z 5", "GOTO 10", "LET C 4", "PRINT C",
                       "PRINT Z", "END", "PRINT C", "PRINT Z", "GOTO -6", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        all_labels = label_line(convert_tokens)
        line_pointer = 0
        try:
            while line_pointer < len(convert_tokens):
                if convert_tokens[line_pointer][0].kind() == GrinTokenKind.LET:
                    let_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.PRINT:
                    print_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.GOTO:
                    goto_command = GoTo(convert_tokens[line_pointer], convert_tokens, line_pointer)
                    new_index = goto_command.jump_lines(all_values, all_labels)
                    line_pointer = new_index
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.END or convert_tokens[line_pointer][0].kind() == GrinTokenKind.DOT:
                    break
        except InvalidLineError:
            self.assertRaises(InvalidLineError)

    def test4_goto(self):
        user_values = ["LET Z 5", "GOTO \"CZ\"", "CCZ: LET C 4", "PRINT C",
                       "PRINT Z", "END", "CZ: PRINT C", "PRINT Z", "GOTO \"CCZ\"", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        all_labels = label_line(convert_tokens)
        line_pointer = 0
        try:
            while line_pointer < len(convert_tokens):
                if convert_tokens[line_pointer][0].kind() == GrinTokenKind.LET:
                    let_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.PRINT:
                    print_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.IDENTIFIER and convert_tokens[line_pointer][1].kind() == GrinTokenKind.COLON:
                    get_command_label = convert_tokens[line_pointer][2:]
                    encountered_label_line(get_command_label, all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.GOTO:
                    goto_command = GoTo(convert_tokens[line_pointer], convert_tokens, line_pointer)
                    new_index = goto_command.jump_lines(all_values, all_labels)
                    line_pointer = new_index
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.END or convert_tokens[line_pointer][0].kind() == GrinTokenKind.DOT:
                    break
            self.assertEqual(all_values, {"C": 4, "Z": 5})
        except InvalidLineError:
            self.assertRaises(InvalidLineError)

    def test5_goto(self):
        user_values = ["LET Z 5", "GOTO \"ABC\"", "."]
        convert_tokens = convert_to_grin_tokens(user_values)
        all_values = dict()
        all_labels = label_line(convert_tokens)
        line_pointer = 0
        try:
            while line_pointer < len(convert_tokens):
                if convert_tokens[line_pointer][0].kind() == GrinTokenKind.LET:
                    let_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.PRINT:
                    print_conversion(convert_tokens[line_pointer], all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.IDENTIFIER and convert_tokens[line_pointer][1].kind() == GrinTokenKind.COLON:
                    get_command_label = convert_tokens[line_pointer][2:]
                    encountered_label_line(get_command_label, all_values)
                    line_pointer += 1
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.GOTO:
                    goto_command = GoTo(convert_tokens[line_pointer], convert_tokens, line_pointer)
                    new_index = goto_command.jump_lines(all_values, all_labels)
                    line_pointer = new_index
                elif convert_tokens[line_pointer][0].kind() == GrinTokenKind.END or convert_tokens[line_pointer][0].kind() == GrinTokenKind.DOT:
                    break
        except InvalidLineError:
            self.assertRaises(InvalidLineError)