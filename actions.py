# -----------------------------------------------------------------------------
# A Clone of Rogue
# Change Log (Who, What, When)
# KMcGuire, Created script, 7/28/25
#------------------------------------------------------------------------------

class Action:
    pass


class EscapeAction(Action):
    pass

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy