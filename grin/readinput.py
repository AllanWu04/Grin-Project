from grin.location import GrinLocation
from grin.token import GrinTokenCategory, GrinTokenKind, GrinToken


def take_user_grin_input():
    """Returns a list of user grin commands through console"""
    lines = []
    while True:
        user = input()
        if user == '.' or user == 'END':
            break
        lines.append(user)
    return lines

