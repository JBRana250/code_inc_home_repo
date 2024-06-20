import environment


class Program:
    statements_list = []
    environment = None

    def __init__(self):
        self.statements_list.clear()
        self.environment = environment.Environment()
        self.environment.map.clear()
