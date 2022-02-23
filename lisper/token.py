from enum import Enum, auto

class Token:
    def __init__(self, type, lexeme, literal, line ) -> None:
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __repr__(self):
        return f" |type:{self.type} lexeme:{self.lexeme} literal:{self.literal}| "

class Types(Enum):
    
    # SINGLE CHAR TOKENS
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    SEMICOLON = auto()

    #LITERALS
    STRING = auto()
    NUMBER = auto()

    # SYMBOLS
    SYMBOL = auto()

    #END OF FILE
    EOF = auto()
