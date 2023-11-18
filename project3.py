# project3.py
#
# ICS 33 Fall 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin


def main() -> None:
    commands = grin.take_user_grin_input()
    convert_commands = grin.convert_to_grin_tokens(commands)
    all_var_values = dict()
    all_label_lines = grin.label_line(convert_commands)
    line_tracker = 0
    gosub_return_line = []
    if convert_commands is not None:
        try:
            while line_tracker < len(convert_commands):
                if convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.LET:
                    grin.let_conversion(convert_commands[line_tracker], all_var_values)
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.PRINT:
                    grin.print_conversion(convert_commands[line_tracker], all_var_values)
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.INNUM or convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.INSTR:
                    grin.instr_and_innum_conversion(convert_commands[line_tracker], all_var_values)
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.ADD:
                    add = grin.Addition(convert_commands[line_tracker], all_var_values)
                    add.add_values()
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.SUB:
                    sub = grin.Subtraction(convert_commands[line_tracker], all_var_values)
                    sub.subtract_values()
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.MULT:
                    mult = grin.Multiplication(convert_commands[line_tracker], all_var_values)
                    mult.multiply_values()
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.DIV:
                    div = grin.Division(convert_commands[line_tracker], all_var_values)
                    div.divide_values()
                    line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.IDENTIFIER and convert_commands[line_tracker][1].kind() == grin.GrinTokenKind.COLON:
                    get_label_command = convert_commands[line_tracker][2:]
                    if get_label_command[0].kind() == grin.GrinTokenKind.END or get_label_command[0].kind() == grin.GrinTokenKind.DOT:
                        break
                    elif get_label_command[0].kind() == grin.GrinTokenKind.GOTO:
                        goto_command = grin.GoTo(convert_commands[line_tracker], convert_commands, line_tracker)
                        if goto_command.check_condition(all_var_values):
                            line_num = goto_command.jump_lines(all_var_values, all_label_lines)
                            line_tracker = line_num
                        else:
                            line_tracker += 1
                            continue
                    elif get_label_command[0].kind() == grin.GrinTokenKind.GOSUB:
                        gosub_command = grin.GoSub(convert_commands[line_tracker], convert_commands, line_tracker,
                                                   gosub_return_line)
                        if gosub_command.check_condition(all_var_values):
                            line_num = gosub_command.jump_lines(all_var_values, all_label_lines)
                            gosub_command.add_line_of_gosub()
                            line_tracker = line_num
                        else:
                            line_tracker += 1
                            continue
                    elif get_label_command[0].kind() == grin.GrinTokenKind.RETURN:
                        if len(gosub_return_line) == 0:
                            raise grin.ReturnWithNoGoSubError
                        else:
                            line_tracker = gosub_return_line[len(gosub_return_line) - 1]
                            gosub_return_line.pop(len(gosub_return_line) - 1)
                    else:
                        grin.encountered_label_line(get_label_command, all_var_values)
                        line_tracker += 1
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.GOTO:
                    goto_command = grin.GoTo(convert_commands[line_tracker], convert_commands, line_tracker)
                    if goto_command.check_condition(all_var_values):
                        line_num = goto_command.jump_lines(all_var_values, all_label_lines)
                        line_tracker = line_num
                    else:
                        line_tracker += 1
                        continue
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.GOSUB:
                    gosub_command = grin.GoSub(convert_commands[line_tracker], convert_commands, line_tracker, gosub_return_line)
                    if gosub_command.check_condition(all_var_values):
                        line_num = gosub_command.jump_lines(all_var_values, all_label_lines)
                        gosub_command.add_line_of_gosub()
                        line_tracker = line_num
                    else:
                        line_tracker += 1
                        continue
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.RETURN:
                    if len(gosub_return_line) == 0:
                        raise grin.ReturnWithNoGoSubError
                    else:
                        line_tracker = gosub_return_line[len(gosub_return_line) - 1]
                        gosub_return_line.pop(len(gosub_return_line) - 1)
                elif convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.END or convert_commands[line_tracker][0].kind() == grin.GrinTokenKind.DOT:
                    break
        except RuntimeError:
            print("Sorry, a runtime error has occurred. Please try again!")
        except grin.InvalidLineError:
            print("Sorry, the line you inputted is out of bounds or is an invalid value!")
        except grin.ReturnWithNoGoSubError:
            print("Sorry, there is no GOSUB value to return to!")

if __name__ == '__main__':
    main()
