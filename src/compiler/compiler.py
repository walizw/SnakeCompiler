from .compile_process import CompileProcess
from .lexer import LexProcess

from utils import status

class Compiler:
    def __init__ (self):
        self.compile_process = None

    def compile_file (self, fname, out="", config={}) -> int:
        self.compile_process = CompileProcess (fname, out, config)

        # TODO: Perform lexical analysis
        lex_process = LexProcess (self.compile_process)

        if lex_process.lex () != status.LEXICAL_ANALYSIS_ALL_OK:
            return status.COMPILER_FAILED_WITH_ERRORS

        # TODO: Perform parsing
        # TODO: Perform code generation

        return status.COMPILER_FILE_COMPILED_OK
