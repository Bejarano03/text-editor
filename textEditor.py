class TexOperation:
    def __init__(self, type, character) -> None:
        self.type = type
        self.character = character

class Under:
    def __init__(self) -> None:
        self.operation = []
        self.test_str = ""

    def add(self, character):
        add_operation = TexOperation("add", character)
        self.operation.append(add_operation)
        self.test_str += character

    def delete(self):
        delete_operation = TexOperation("delete", self.operation[-1])
        self.operation.append(delete_operation)
        self.test_str = slice(0, len(self.test_str))

    def undo(self):
        top = self.operation.pop(-1)
        if top.type == "add":
            self.test_str = slice(0, len(self.test_str))
        elif top.type == "delete":
            self.test_str += top.character

    
