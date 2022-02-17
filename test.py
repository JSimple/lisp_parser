from enum import Enum, auto

def plus(a,b):
    return a+b

class Plusser:
    def __init__(self, a, b) -> None:
        self.added = a + b

class Token:
    def __init__(self, type, lexeme, literal, line ) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def toString(self):
        return f"{self.type} {self.lexeme} {self.literal}"

class Types(Enum):
    
    # SINGLE CHAR TOKENS
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SINGLE_QUOTE = auto()
    SEMICOLON = auto()
    STAR = auto()

    #TOKENS THAT CAN BE ONE OR TWO CHARS
    EQUAL = auto()
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