class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_commands = []
        self.redo_commands = []

    def add(self, num: int):
        self.value += num
        self.undo_commands.append(num)

    def subtract(self, num: int):
        self.value -= num
        self.undo_commands.append(-num)

    def undo(self):
        try:
            num = self.undo_commands.pop()
            self.value -= num
            self.redo_commands.append(num)
        except:
            pass

    def redo(self):
        try:
            num = self.redo_commands.pop()
            self.value += num
            self.undo_commands.append(num)
        except:
            pass

    def bulk_undo(self, steps: int):
        for x in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for x in range(steps):
            self.redo()
