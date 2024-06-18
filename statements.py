import exceptions


class PrintStatement:
    expr = None

    def __init__(self, _expr):
        self.expr = _expr

    def print_debug(self):
        print("Print Statement. Expression:")
        self.expr.print_debug()


class VarDeclaration:
    id = None
    expr = None

    def __init__(self, _id, _expr):
        self.id = _id
        self.expr = _expr

    def print_debug(self):
        print("VarDeclaration. id = {}. Expression:".format(self.id))
        self.expr.print_debug()
