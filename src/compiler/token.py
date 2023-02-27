class Position:
    def __init__ (self):
        self.line = 1
        self.col = 1
        self.fname = ""

class Token:
    def __init__ (self):
        self.type = 0
        self.config = {}

        self.val = 0

        # is there a whitespace between this and the next token?
        # i.e * a for operator token `*' whitespace would be True
        self.whitespace = False

        # (5 + 10 + 20) between brackets would contain all the tokens between
        # the brackets (as a string)
        self.between_brackets = ""

        self.pos = Position ()
