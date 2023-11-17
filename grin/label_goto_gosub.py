from grin.token import GrinTokenKind

def label_line(lines):
    """Returns a dictionary of labels with corresponding line number its on"""
    dict_of_labels = dict()
    for line in lines:
        if line[0].kind() == GrinTokenKind.IDENTIFIER and line[1].kind() == GrinTokenKind.COLON:
            dict_of_labels.update({line[0].text(): line[0].location().line()})
    return dict_of_labels
