import expressions


class Parser:  # figure out what statements are being made
    # we need to made parse_expression first, since expressions are a very important building block

    def parse_expression(self, tokens):
        return self.parse_equality(tokens)

    def parse_equality(self, tokens):
        pass

    def parse_primary(self, tokens):
        if len(tokens) == 1:  # single terminal
            if tokens[0].token_value == "True":
                return expressions.LiteralExpression(True)
            elif tokens[0].token_value == "False":
                return expressions.LiteralExpression(False)
            elif tokens[0].token_value == "None":
                return expressions.LiteralExpression(None)
            elif tokens[0].token_type == "LITERAL_NUMBER":
                return expressions.LiteralExpression(tokens[0])
            elif tokens[0].token_type == "LITERAL_STRING":
                return expressions.LiteralExpression(tokens[0])
            else:
                return "invalid token"
        elif tokens[0].token_value == "(":  # follows pattern '(' expression ')'
            pass
        else:
            return "error_message"  # does not match any pattern for primary expression
