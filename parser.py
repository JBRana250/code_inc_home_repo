class Parser:  # figure out what statements are being made
    def __init__(self):
        pass

    identifiers = []  # list of already declared identifiers

    def parse_expression(self, tokens):  # where tokens is a list of the tokens involved in the expression
        pass

    def parse_line(self, line):
        first_token = line[0]  # this will be used to check grammar since many different statements that can be made in python hinge on the first token being correct.

        # variable declarations are in the format {0} OPERATOR_ASSIGN {1} where {0} must be a variable and {1} is an expression. (which can just be a literal)
        if first_token.token_type == "IDENTIFIER":
            if first_token in self.identifiers:  # check if the current identifier has already been declared
                pass
            else:  # current identifier not already declared, expect that this must then be the declaration, so expects next token to be '='
                if line[1].token_type == "OPERATOR_ASSIGN":  # '=' is only valid token at this point since no existing value to be augmented (so NO augmented assignment)
                    # if the stream so far follows the pattern IDENTIFIER OPERATOR_ASSIGN, it is expected that the next tokens will be an expression
                    pass
                else:
                    return "error_message"

    def parse_lines_list(self, token_lines):
        program = []  # a program is a list of statements being made.
        for line in token_lines:
            statement = self.parse_line(line)
            program.append(statement)