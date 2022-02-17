from enum import Enum, auto
### TOKEN CLASS DEFINITION ###

class Token:
    def __init__(self, type, lexeme, literal, line ) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def toString(self):
        return f"{self.type} {self.lexeme} {self.literal}"

### TOKEN TYPES ###
class Types(Enum):  ## why not just create a dictionary right off the bat?
    # SINGLE CHAR TOKENS
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    COMMA = auto()
    DOT = auto()
    EQUAL = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SINGLE_QUOTE = auto()
    STAR = auto()

    #TOKENS THAT CAN BE ONE OR TWO CHARS
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    SLASH = auto()
    SLASH_EQUAL = auto()

    #LITERALS
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    #KEYWORDS
    AND = auto()
    DEFCONSTANT = auto()
    DEFUN = auto()
    DEFVAR = auto()
    LET = auto()
    MAX = auto()
    MIN = auto()
    NIL = auto()
    NOT = auto()
    OR = auto()
    PRINT = auto()
    VAR = auto()
    WRITE = auto()

    #END OF FILE
    EOF = auto()