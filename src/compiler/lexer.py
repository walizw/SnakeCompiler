from .token import Position
from utils import status

class LexProcess:
    def __init__ (self, compiler):
        self.pos = Position ()
        self.tokens = []
        self.compiler = compiler # the compiler process this lexer is part of

        # how many brackets are there at the moment
        self.current_expression_count = 0
        self.parentheses_buffer = ""

        # hold private data
        self.private = None

    def lex (self):
        return status.LEXICAL_ANALYSIS_ALL_OK

    def next_char (self):
        if not self.compiler:
            return

        self.compiler.pos.col += 1
        c = compiler.file.read (1)

        if c == "\n":
            self.compiler.pos.line += 1
            self.compiler.pos.col = 1

        return c

    def peek_char (self):
        if not self.compiler:
            return

        cur_pos = self.compiler.file.tell ()
        c = self.compiler.file.read (1)
        self.compiler.file.seek (cur_pos)

        return c

    def push_char (self):
        if not self.compiler:
            return

        cur_pos = self.compiler.file.tell ()
        if cur_pos - 1 < 0:
            return

        self.compiler.file.seek (cur_pos - 1)
