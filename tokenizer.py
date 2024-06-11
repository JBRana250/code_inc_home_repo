class Token:
    token_type = None
    token_value = None
    token_line_num = None
    token_element_num = None

    def __init__(self, _token_type, _token_value, _token_line_num, _token_element_num):
        self.token_type = _token_type
        self.token_value = _token_value
        self.token_line_num = _token_line_num
        self.token_element_num = _token_element_num


class Tokenizer:
    def __init__(self):
        pass

    assignment_operators = {
        "=": "OPERATOR_ASSIGN",
        "+=": "OPERATOR_ADD_ASSIGN",
        "-=": "OPERATOR_SUB_ASSIGN",
        "*=": "OPERATOR_MULT_ASSIGN",
        "/=": "OPERATOR_DIV_ASSIGN"
    }

    comparison_operators = {
        "==": "OPERATOR_EQUALS",
        "!=": "OPERATOR_NOT_EQUALS",
        ">": "OPERATOR_GREATER_THAN",
        "<": "OPERATOR_LESS_THAN",
        ">=": "OPERATOR_GREATER_OR_EQUALS",
        "<=": "OPERATOR_LESS_OR_EQUALS"
    }

    arithmetic_operators = {
        "+": "OPERATOR_ADD",
        "-": "OPERATOR_SUB",
        "*": "OPERATOR_MULT",
        "/": "OPERATOR_DIV"
    }

    punctuators = {
        "(": "OPEN_PAREN",
        ")": "CLOSED_PAREN",
        ",": "COMMA",
        '[': "OPEN_SQUARE_B",
        "]": "CLOSED_SQUARE_B",
        "{": "OPEN_CURLY_B",
        "}": "CLOSED_CURLY_B",
        "\"": "DOUBLE_QUOTE",
        "'": "SINGLE_QUOTE"
    }

    keywords = {
        "print": "KEYWORD_PRINT"
    }

    special_literals = {
        "True": "LITERAL_TRUE",
        "False": "LITERAL_FALSE"
    }

    def tokenize_line(self, line, line_num):
        new_line = []
        current_element_pos = 1
        in_string = False
        in_string_punctuator = None
        current_string = ""
        for element in line:
            if not in_string:
                if element in self.assignment_operators:
                    new_line.append(Token(self.assignment_operators[element], element, line_num, current_element_pos))
                if element in self.comparison_operators:
                    new_line.append(Token(self.comparison_operators[element], element, line_num, current_element_pos))
                if element in self.arithmetic_operators:
                    new_line.append(Token(self.arithmetic_operators[element], element, line_num, current_element_pos))
                if element in self.keywords:
                    new_line.append(Token(self.keywords[element], element, line_num, current_element_pos))
                if element in self.special_literals:
                    new_line.append(Token(self.keywords[element], element, line_num, current_element_pos))
                if element in self.punctuators:
                    if element == "\"" or "'":
                        in_string = True
                        in_string_punctuator = element
                        current_element_pos += 1
                    else:
                        new_line.append(Token(self.punctuators[element], element, line_num, current_element_pos))
                        current_element_pos += 1
            else:
                if element == in_string_punctuator:
                    new_line.append(Token("LITERAL", current_string, line_num, current_element_pos))
                    in_string = False
                    in_string_punctuator = None
                    current_element_pos += 1
                else:
                    current_string += element
                    current_element_pos += 1
        return new_line

    def tokenize_lines_list(self, lines_list):
        new_lines_list = []
        current_line_pos = 1
        for line in lines_list:
            new_line = self.tokenize_line(line, current_line_pos)
            new_lines_list.append(new_line)
            current_line_pos += 1
