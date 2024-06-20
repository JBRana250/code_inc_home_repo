import tkinter
import exceptions


class PrintStatement:
    expr = None
    output_panel = None

    def __init__(self, _expr, _output_panel):
        self.expr = _expr
        self.output_panel = _output_panel

    def print_debug(self):
        print("Print Statement. Expression:")
        self.expr.print_debug()

    def interpret(self):
        expr_value = self.expr.interpret()
        # prints out to output terminal
        self.output_panel.config(state="normal")
        self.output_panel.insert(tkinter.END, "\n" + str(expr_value))
        self.output_panel.config(state="disabled")


class VarDeclaration:
    identifier = None
    expr = None
    program = None

    def __init__(self, _id, _expr, _program):
        self.identifier = _id
        self.expr = _expr
        self.program = _program

    def print_debug(self):
        print("VarDeclaration. id = {}. Expression:".format(self.identifier))
        self.expr.print_debug()

    def interpret(self):
        env = self.program.environment
        expr_value = self.expr.interpret()
        env.map[self.identifier.token_value] = expr_value

