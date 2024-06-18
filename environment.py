import exceptions


class Environment:
    map = {}

    def get(self, name):
        if name in self.map.keys:
            return self.map[name]
        else:
            raise exceptions.InnerRuntimeError(_token=name, _message="Undefined variable '" + name.token_value + "'")
