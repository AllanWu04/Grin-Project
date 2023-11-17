from grin.location import GrinLocation
from grin.token import GrinTokenCategory, GrinTokenKind, GrinToken
from grin.parsing import parse, GrinParseError
from grin.lexing import to_tokens, GrinLexError


def take_user_grin_input():
    """Returns a list of user grin commands through console"""
    lines = []
    while True:
        user = input()
        if user == '.':
            lines.append(user)
            break
        lines.append(user)
    return lines


def convert_to_grin_tokens(lines):
    """Takes grin input and converts to tokens"""
    try:
        iterable_list_token = list(parse(lines))
        return iterable_list_token
    except GrinParseError:
        print("Sorry, an error has occurred while parsing your statements.")
    except GrinLexError:
        print("Sorry, a lexing error has occurred on this statement.")


