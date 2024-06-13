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

    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def tokenize_line(self, line, line_num):
        new_line = []
        current_element_pos = 1
        in_string = False
        in_string_punctuator = None
        current_string = ""
        for element in line:
            if not in_string:
                if element == " ":  # skip whitespace
                    continue
                if element in self.assignment_operators:  # is element an operator?
                    new_line.append(Token(self.assignment_operators[element], element, line_num, current_element_pos))
                    current_element_pos += 1
                    continue
                if element in self.comparison_operators:
                    new_line.append(Token(self.comparison_operators[element], element, line_num, current_element_pos))
                    current_element_pos += 1
                    continue
                if element in self.arithmetic_operators:
                    new_line.append(Token(self.arithmetic_operators[element], element, line_num, current_element_pos))
                    current_element_pos += 1
                    continue
                if element in self.keywords:  # is element a keyword?
                    new_line.append(Token(self.keywords[element], element, line_num, current_element_pos))
                    current_element_pos += 1
                    continue
                if element in self.special_literals:  # is element a special literal? (true/false)
                    new_line.append(Token(self.keywords[element], element, line_num, current_element_pos))
                    current_element_pos += 1
                    continue
                if element in self.punctuators:  # is element a punctuator?
                    if element == "\"" or element == "'":  # is it quotation marks? if so, enter string
                        in_string = True
                        in_string_punctuator = element
                        current_element_pos += 1
                        continue
                    else:  # if not, just append punctuator.
                        new_line.append(Token(self.punctuators[element], element, line_num, current_element_pos))
                        current_element_pos += 1
                        continue

                # at this point, element is either a number or an identifier (all other options were tested)
                if element.isnumeric():  # is a number
                    new_line.append(Token("NUMBER", element, line_num, current_element_pos))
                    current_element_pos += 1
                elif element[0] not in self.digits:  # is an identifier
                    new_line.append(Token("IDENTIFIER", element, line_num, current_element_pos))
                    current_element_pos += 1
                else:
                    return "SyntaxError: at line {line}, token {token}: Invalid Token".format(line=line_num, token=current_element_pos)

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
            if type(new_line) is str:
                return new_line
            else:
                new_lines_list.append(new_line)
                current_line_pos += 1
        return new_lines_list
