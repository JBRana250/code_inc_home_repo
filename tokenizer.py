class Tokenizer:
    def __init__(self):
        pass

    assignment_operators = {
        "=": "ASSIGN",
        "+=": "ADD_ASSIGN",
        "-=": "SUB_ASSIGN",
        "*=": "MULT_ASSIGN",
        "/=": "DIV_ASSIGN"
    }

    comparison_operators = {
        "==": "EQUALS",
        "!=": "NOT_EQUALS",
        ">": "GREATER_THAN",
        "<": "LESS_THAN",
        ">=": "GREATER_OR_EQUALS",
        "<=": "LESS_OR_EQUALS"
    }

    arithmetic_operators = {
        "+": "ADD",
        "-": "SUB",
        "*": "MULT",
        "/": "DIV"
    }

    misc_map = {
        "(": "OPEN_PAREN",
        ")": "CLOSED_PAREN",
        ",": "COMMA"
    }

    def tokenize(self, lines_list):
        new_lines_list = []
        for line in lines_list:
            new_line = []
            for element in line:
                if element in self.assignment_operators.keys:
                    new_line.append(self.assignment_operators[element])
                if element in self.comparison_operators.keys:
                    new_line.append(self.comparison_operators[element])
                if element in self.arithmetic_operators.keys:
                    new_line.append(self.arithmetic_operators[element])
            new_lines_list.append(new_line)

class Token:
    token_type = None
    token_value = None
    token_line_num = None
    




