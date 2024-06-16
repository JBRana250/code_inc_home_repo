class ParseError(Exception):
    def print_debug(self):
        print("unspecified error")


class ExpectedTokenError(ParseError):
    expected_tokens = []

    def __init__(self, *args: object, _expected_tokens) -> None:
        super().__init__(*args)
        self.expected_tokens = _expected_tokens
    
    def print_debug(self):
        tokens = ', '.join(self.expected_tokens)
        print("Expected Tokens {}".format(tokens))
        

class UnexpectedTokenError(ParseError):
    unexpected_tokens = []

    def __init__(self, *args: object, _unexpected_tokens) -> None:
        super().__init__(*args)
        self.unexpected_tokens = _unexpected_tokens
    
    def print_debug(self):
        tokens_list = []
        for token in self.unexpected_tokens:
            tokens_list.append(str(token.token_value))
        tokens = ', '.join(tokens_list)
        print("Unexpected Tokens {}".format(tokens))


class ExpectedExpressionError(ParseError):
    def print_debug(self):
        print("Expected Expression")


class InnerRuntimeError(Exception):  # runtime error encountered when interpreting the user's code
    token = None
    message = "no message detected"

    def __init__(self, *args: object, _token, _message) -> None:
        super().__init__(*args)
        self.token = _token
        self.message = _message
    
    def print_debug(self):
        print(self.message)
