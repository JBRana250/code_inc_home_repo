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


class LiteralExpression:
    value = None

    def __init__(self, _value):
        self.value = _value
    
    def print_debug(self):
        print("type: LiteralExpression, value = {}".format(self.value.token_value))


class GroupingExpression:
    expression = None

    def __init__(self, _expression):
        self.expression = _expression
    
    def print_debug(self):
        print("type: GroupingExpression")
        print("Inner expression:")
        self.expression.print_debug()


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