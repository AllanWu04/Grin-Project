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
    var_assignment = grin.let_conversion(convert_commands)
    display_values = grin.print_conversion(convert_commands)

if __name__ == '__main__':
    main()
