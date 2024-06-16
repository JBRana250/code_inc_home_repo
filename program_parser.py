import expressions
import exceptions

class Parser:  # figure out what statements are being made
    # we need to made parse_expression first, since expressions are a very important building block

    # these expressions are parsed in top-down order from lowest precedence to highest precedence.
    # the reason why is because in the AST we would want the highest precedence at the lowest points in the AST, and vice versa.
    # so therefore, we look for lower precedence first to put them at the higher points in the AST.

    def parse_expression(self, tokens):
        return self.parse_comparison(tokens)

    # For left-associativity, we basically need to find the LAST operator at the current precedence level, and split the token stream into 2 expressions: 1 to the LEFT of this operator, and 1 to the RIGHT.

    comparison_operators = [
        "==",
        "!=",
        ">",
        "<",
        ">=",
        "<="
    ]

    def parse_comparison(self, tokens):  
        #  Normally in python, comparison operators are able to be chained, eg x > y > z means x > y AND y > z. However, I do not think the implementation of this feature is not worth the trouble since I only have a limited amount of time
        #  and will only put in very simple things in this compiler, vs the usefullness of being able to chain comparison operators. So, I will have it work like x > y > z ==> (x > y) > z which is less useful.
        operators = []
        for token in tokens:
            if token.token_value in self.comparison_operators:
                operators.append(token)
        operators.reverse()
        if len(operators) > 0:
            for operator in operators:
                index = tokens.index(operator)  # get what index the token is at in the token stream
                left_expr_tokens = []
                right_expr_tokens = []
                for token in tokens:  # if current token's index less than index var, means it is to the left of operator.
                    if tokens.index(token) < index:
                        left_expr_tokens.append(token)
                    elif tokens.index(token) > index:  # if current token's index greater than index var, means it is to the right of operator.
                        right_expr_tokens.append(token)
                if len(left_expr_tokens) == 0 or len(right_expr_tokens) == 0:
                    raise exceptions.ExpectedExpressionError()   # we expect there to be an expression on both sides
                else:
                    left_expr = self.parse_comparison(left_expr_tokens)
                    right_expr = self.parse_comparison(right_expr_tokens)
                    return expressions.BinaryExpression(left_expr, right_expr, operator)
        else:
            return self.parse_term(tokens)

    def parse_term(self, tokens):
        operators = []
        for token in tokens:
            if token.token_value == '+' or token.token_value == "-":
                operators.append(token)
        operators.reverse()  # flip list order. we need to get the LAST operator, and work our way to the first operator.
        if len(operators) > 0:
            for operator in operators:
                index = tokens.index(operator)  # get what index the token is at in the token stream
                left_expr_tokens = []
                right_expr_tokens = []
                for token in tokens:  # if current token's index less than index var, means it is to the left of operator.
                    if tokens.index(token) < index:
                        left_expr_tokens.append(token)
                    elif tokens.index(token) > index:  # if current token's index greater than index var, means it is to the right of operator.
                        right_expr_tokens.append(token)
                if len(right_expr_tokens) == 0:
                    raise exceptions.ExpectedExpressionError()  # we definitely expect an expression on the right side of an operator, at least for this implementation. Even if such a suffix exists in the Python grammar, it should be implemented in a future version of this.
                elif len(left_expr_tokens) == 0:
                    # here, lets expect that this is instead an unary operator. In this case, continue working up the precedence ladder.
                    return self.parse_factor(tokens)
                else:
                    try:  # we try to parse the left expression tokens
                        self.parse_term(left_expr_tokens)
                    except exceptions.ParseError:  # if there is a parse error, we know that the left expression is not valid, so we check again using the operator to the left of this one.                 
                        pass
                    else:  # if there is no parse error with the left expression, we can finally proceed with the term expression, since now we know its not an unary.
                        left_expr = self.parse_term(left_expr_tokens)
                        right_expr = self.parse_term(right_expr_tokens)
                        return expressions.BinaryExpression(left_expr, right_expr, operator)
            # if we run out of operators and still not valid, move on to next higher precedence operator
            return self.parse_factor(tokens)
        else:
            return self.parse_factor(tokens)

    def parse_factor(self, tokens):
        operators = []
        for token in tokens:
            if token.token_value == '*' or token.token_value == "/":
                operators.append(token)
        operators.reverse()
        if len(operators) > 0:
            for operator in operators:
                index = tokens.index(operator)  # get what index the token is at in the token stream
                left_expr_tokens = []
                right_expr_tokens = []
                for token in tokens:  # if current token's index less than index var, means it is to the left of operator.
                    if tokens.index(token) < index:
                        left_expr_tokens.append(token)
                    elif tokens.index(token) > index:  # if current token's index greater than index var, means it is to the right of operator.
                        right_expr_tokens.append(token)
                if len(left_expr_tokens) == 0 or len(right_expr_tokens) == 0:
                    raise exceptions.ExpectedExpressionError()   # we expect there to be an expression on both sides (no unary for * or /)
                else:
                    left_expr = self.parse_factor(left_expr_tokens)
                    right_expr = self.parse_factor(right_expr_tokens)
                    return expressions.BinaryExpression(left_expr, right_expr, operator)
        else:
            return self.parse_unary(tokens)

    def parse_unary(self, tokens):
        # if we see an unary operator, recursively call self.parse_unary again (since it is possible to have multiple unary operators)
        first_token = tokens[0]
        if first_token.token_value == 'not' or first_token.token_value == '-' or first_token.token_value == '+':
            operator = first_token
            sliced_expr = tokens[1:]  # slice off the unary operator
            expr = self.parse_unary(sliced_expr)
            return expressions.UnaryExpression(expr, operator)

        return self.parse_primary(tokens)

    def parse_primary(self, tokens):
        first_token = tokens[0]
        if len(tokens) == 1:  # single terminal
            if first_token.token_value == "True":
                return expressions.LiteralExpression(first_token)
            elif first_token.token_value == "False":
                return expressions.LiteralExpression(first_token)
            elif first_token.token_value == "None":
                return expressions.LiteralExpression(first_token)
            elif tokens[0].token_type == "LITERAL_NUMBER":
                return expressions.LiteralExpression(first_token)
            elif tokens[0].token_type == "LITERAL_STRING":
                return expressions.LiteralExpression(first_token)
            else:
                raise exceptions.UnexpectedTokenError("Unexpected Token", _unexpected_tokens = [first_token])
        elif tokens[0].token_value == "(":  # follows pattern '(' expression ')'
            tokens_in_paren = []
            expr = None
            unexpected_tokens = []  # if encounter tokens after closing bracket, that is invalid
            open_paren_count = -1  # counts the number of opening parenthesis encountered after the first openening parenthesis. If more open paren are encountered, expects more closing paren.
            for token in tokens:
                if expr is None:
                    if token.token_value == ')':
                        if open_paren_count == 0:
                            expr = self.parse_expression(tokens_in_paren)
                        else:
                            open_paren_count -= 1
                            tokens_in_paren.append(token)
                    elif token.token_value == '(':
                        open_paren_count += 1
                        if open_paren_count != 0:
                            tokens_in_paren.append(token)
                    else:
                        tokens_in_paren.append(token)
                elif expr:
                    unexpected_tokens.append(token)
            if expr and len(unexpected_tokens) == 0:
                return expressions.GroupingExpression(expr)
            elif expr:
                raise exceptions.UnexpectedTokenError("Unexpected Tokens", _unexpected_tokens = unexpected_tokens)
            else:
                raise exceptions.ExpectedTokenError("Expected Token", _expected_tokens = [')'])
        else:
            raise exceptions.UnexpectedTokenError("Unexpected Tokens", _unexpected_tokens = tokens[1:])  # does not match any pattern for primary expression
        
