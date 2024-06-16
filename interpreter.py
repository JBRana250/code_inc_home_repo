import exceptions

class Interpreter:

    def interpret_ast(self, ast):
        pass

    def interpret_expression(self, expr):
        pass

    def interpret_literal_expr(self, expr):
        return expr.value

    def interpret_grouping_expr(self, expr):
        return self.interpret_expression(expr.expression)

    def interpret_unary_expr(self, expr):
        right_expr = self.interpret_expression(expr.expression)
        
        match expr.operator.token_value:
            case '-':
                self.check_number_operand(right_expr)
                return -right_expr
            case 'not':
                return not(self.is_truthy(right_expr))

    def check_number_operand(self, operand):
        if isinstance(operand.token_value, [int, float, complex]):  # if variable type is numeric
            return True
        else:
            raise exceptions.InnerRuntimeError(_token = operand, _message = "Operand must be a number")
    
    def is_truthy(self, thing):
        if isinstance(thing, bool):
            return thing
        elif thing == 0:
            return False
        elif thing == None:
            return False
        elif thing == "":
            return False
        else:
            return True
        
