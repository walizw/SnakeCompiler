from .token import Position

class CompileProcess:
    def __init__ (self, fname, out, config):
        self.file = open (fname, "r")
        self.out = None

        if out:
            self.out = open (out, "w")

        self.pos = Position ()
        self.config = config
