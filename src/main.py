from compiler import Compiler
from utils import status

compiler = Compiler ()
res = compiler.compile_file ("test.c", "test")

if res == status.COMPILER_FILE_COMPILED_OK:
    print ("Compilation successful")
elif res == COMPILER_FAILED_WITH_ERRORS:
    print ("There's been an error compiling the specified file")
else:
    print ("The compiler returned an unknown response")
