import expressions


class Parser:  # figure out what statements are being made
    # we need to made parse_expression first, since expressions are a very important building block

    def parse_expression(self, tokens):
        return self.parse_equality(tokens)

    def parse_equality(self, tokens):
        return self.parse_comparison(tokens)

    def parse_comparison(self, tokens):
        return self.parse_term(tokens)

    def parse_term(self, tokens):
        return self.parse_factor(tokens)

    def parse_factor(self, tokens):
        return self.parse_unary(tokens)

    def parse_unary(self, tokens):
        return self.parse_primary(tokens)

    def parse_primary(self, tokens):
        first_token = tokens[0]
        if len(tokens) == 1:  # single terminal
            if first_token.token_value == "True":
                return expressions.LiteralExpression(True)
            elif first_token.token_value == "False":
                return expressions.LiteralExpression(False)
            elif first_token.token_value == "None":
                return expressions.LiteralExpression(None)
            elif tokens[0].token_type == "LITERAL_NUMBER":
                return expressions.LiteralExpression(tokens[0])
            elif tokens[0].token_type == "LITERAL_STRING":
                return expressions.LiteralExpression(tokens[0])
            else:
                return "invalid token"
        elif tokens[0].token_value == "(":  # follows pattern '(' expression ')'
            tokens_in_paren = []
            for token in tokens:
                if token.token_value == ')':
                    expr = self.parse_expression(tokens_in_paren)
                    return expressions.GroupingExpression(expr)
                else:
                    tokens_in_paren.append(token)
        else:
            return "error_message"  # does not match any pattern for primary expression
