import exceptions


def check_number_operand(operand_type):
    if operand_type == "LITERAL_NUMBER":
        return True
    else:
        raise exceptions.InnerRuntimeError(_token=operand_type, _message="Operand(s) must be a number")


def is_number(operand_type):  # the difference with this function is that it doesn't raise an error if it fails
    if operand_type == "LITERAL_NUMBER":
        return True
    else:
        return False


def check_string_operand(operand_type):
    if operand_type == "LITERAL_STRING":
        return True
    else:
        raise exceptions.InnerRuntimeError(_token=operand_type, _message="Operand(s) must be a string")


def is_string(operand_type):
    if operand_type == "LITERAL_STRING":
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

    expr_type = ""

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
        lexpr_type = self.left_expr.get_type()
        rexpr_type = self.right_expr.get_type()

        match self.operator.token_value:
            case "*":
                check_number_operand(lexpr_type)
                check_number_operand(rexpr_type)
                self.expr_type = "LITERAL_NUMBER"
                return float(lexpr) * float(rexpr)
            case "/":
                check_number_operand(lexpr_type)
                check_number_operand(rexpr_type)
                self.expr_type = "LITERAL_NUMBER"
                return float(lexpr) / float(rexpr)
            case "-":
                check_number_operand(lexpr_type)
                check_number_operand(rexpr_type)
                self.expr_type = "LITERAL_NUMBER"
                return float(lexpr) - float(rexpr)
            case "+":
                if is_string(lexpr_type) and is_string(rexpr_type):
                    self.expr_type = "LITERAL_STRING"
                    return str(lexpr) + str(rexpr)
                elif is_number(lexpr_type) and is_number(rexpr_type):
                    self.expr_type = "LITERAL_NUMBER"
                    return float(lexpr) + float(rexpr)
                else:
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Operands need to be either both numbers or both strings")
            case ">":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    self.expr_type = "LITERAL_BOOL"
                    return lexpr > rexpr
            case "<":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    self.expr_type = "LITERAL_BOOL"
                    return lexpr > rexpr
            case ">=":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    self.expr_type = "LITERAL_BOOL"
                    return lexpr > rexpr
            case "<=":  # ONLY none is unsupported operand.
                if (lexpr is None) or (rexpr is None):
                    raise exceptions.InnerRuntimeError(_token=self.operator, _message="Unsupported operand None")
                else:
                    self.expr_type = "LITERAL_BOOL"
                    return lexpr > rexpr
            case "==":
                self.expr_type = "LITERAL_BOOL"
                return lexpr == rexpr
            case "!=":
                self.expr_type = "LITERAL_BOOL"
                return lexpr != rexpr

    def get_type(self):
        return self.expr_type


class LiteralExpression:
    token = None

    def __init__(self, _token):
        self.token = _token
    
    def print_debug(self):
        print("type: LiteralExpression, value = {}".format(self.token.token_value))

    def interpret(self):
        if is_number(self.token.token_type):
            return float(self.token.token_value)
        else:
            return self.token.token_value

    def get_type(self):
        return self.token.token_type


class GroupingExpression:
    expression = None
    expr_type = ""

    def __init__(self, _expression):
        self.expression = _expression
    
    def print_debug(self):
        print("type: GroupingExpression")
        print("Inner expression:")
        self.expression.print_debug()

    def interpret(self):
        expr = self.expression.interpret()
        self.expr_type = self.expression.get_type()
        return expr
    
    def get_type(self):
        return self.expr_type
    



class UnaryExpression:
    unary_operator = None
    expression = None
    expr_type = ""

    def __init__(self, _expression, _operator):
        self.unary_operator = _operator
        self.expression = _expression
    
    def print_debug(self):
        print("type: UnaryExpression, operator = {}".format(self.unary_operator.token_value))
        print("Inner expression:")
        self.expression.print_debug()

    def interpret(self):
        right_expr = self.expression.interpret()
        right_expr_type = self.expression.get_type()

        match self.unary_operator.token_value:
            case '-':
                check_number_operand(right_expr_type)
                self.expr_type = "LITERAL_NUMBER"
                return -float(right_expr)
            case 'not':
                self.expr_type = "LITERAL_BOOL"
                return not (is_truthy(right_expr))
    
    def get_type(self):
        return self.expr_type
