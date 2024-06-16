import exceptions


def check_number_operand(operand):
    if isinstance(operand, int | float | complex):  # if variable type is numeric
        return True
    else:
        raise exceptions.InnerRuntimeError(_token=operand, _message="Operand(s) must be a number")


def is_number(operand):  # the difference with this function is that it doesn't raise an error if it fails
    if isinstance(operand, int | float | complex):  # if variable type is numeric
        return True
    else:
        return False


def check_string_operand(operand):
    if isinstance(operand, str):
        return True
    else:
        raise exceptions.InnerRuntimeError(_token=operand, _message="Operand(s) must be a string")


def is_string(operand):
    if isinstance(operand, str):
        return True
    else:
        return False


def is_truthy(thing):
    if isinstance(thing, bool):
        return thing
    elif thing == 0:
        return False
    elif thing is None:
        return False
    elif thing == "":
        return False
    else:
        return True


class BinaryExpression:
    left_expr = None
    right_expr = None
    operator = None

    def __init__(self, _left, _right, _operator):
        self.left_expr = _left
        self.right_expr = _right
        self.operator = _operator

    def print_debug(self):
        print("type: BinaryExpression, operator = {}".format(self.operator.token_value))
        print("Left expression:")
        self.left_expr.print_debug()
        print("Right expression:")
        self.right_expr.print_debug()

    def interpret(self):
        lexpr = self.left_expr.interpret()
        rexpr = self.right_expr.interpret()

        match self.operator.token_value:
            case "*":
                check_number_operand(lexpr)
                check_number_operand(rexpr)
                return lexpr * rexpr
            case "/":
                check_number_operand(lexpr)
                check_number_operand(rexpr)
                return lexpr / rexpr
            case "-":
                check_number_operand(lexpr)
                check_number_operand(rexpr)
                return lexpr - rexpr
            case "+":
                if is_string(lexpr) and is_string(rexpr):
                    return lexpr + rexpr
                elif is_number(lexpr) and is_number(rexpr):
                    return lexpr + rexpr
                else:
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Operands need to be either both numbers or both strings")
            case ">":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    return lexpr > rexpr
            case "<":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    return lexpr > rexpr
            case ">=":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    return lexpr > rexpr
            case "<=":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    return lexpr > rexpr
            case "==":
                return lexpr == rexpr
            case "!=":
                return lexpr != rexpr


class LiteralExpression:
    value = None

    def __init__(self, _value):
        self.value = _value
    
    def print_debug(self):
        print("type: LiteralExpression, value = {}".format(self.value.token_value))

    def interpret(self):
        return self.value.token_value


class GroupingExpression:
    expression = None

    def __init__(self, _expression):
        self.expression = _expression
    
    def print_debug(self):
        print("type: GroupingExpression")
        print("Inner expression:")
        self.expression.print_debug()

    def interpret(self):
        return self.expression.interpret()


class UnaryExpression:
    unary_operator = None
    expression = None

    def __init__(self, _expression, _operator):
        self.unary_operator = _operator
        self.expression = _expression
    
    def print_debug(self):
        print("type: UnaryExpression, operator = {}".format(self.unary_operator.token_value))
        print("Inner expression:")
        self.expression.print_debug()

    def interpret(self):
        right_expr = self.expression.interpret()

        match self.unary_operator.token_value:
            case '-':
                check_number_operand(right_expr)
                return -right_expr
            case 'not':
                return not (is_truthy(right_expr))
