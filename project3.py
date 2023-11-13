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
    values_to_print = []
    if convert_commands is not None:
        for line in convert_commands:
            if line[0].kind() == grin.GrinTokenKind.LET:
                grin.let_conversion(line, all_var_values)
            elif line[0].kind() == grin.GrinTokenKind.PRINT:
                grin.print_conversion(line, all_var_values, values_to_print)
            elif line[0].kind() == grin.GrinTokenKind.INNUM or line[0].kind() == grin.GrinTokenKind.INSTR:
                grin.instr_and_innum_conversion(line, all_var_values)
            elif line[0].kind() == grin.GrinTokenKind.END or line[0].kind() == grin.GrinTokenKind.DOT:
                break
        for i in values_to_print:
            print(i)

if __name__ == '__main__':
    main()
