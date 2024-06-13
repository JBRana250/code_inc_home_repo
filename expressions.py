class BinaryExpression:
    left = None
    right = None
    operator = None

    def __init__(self, _left, _right, _operator):
        self.left = _left
        self.right = _right
        self.operator = _operator


class LiteralExpression:
    value = None

    def __init__(self, _value):
        self.value = _value


class GroupingExpression:
    expression = None

    def __init__(self, _expression):
        self.expression = _expression
