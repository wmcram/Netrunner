class Action:
    pass

class EscapeAction(action):
    pass

class MovementAction(action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy
