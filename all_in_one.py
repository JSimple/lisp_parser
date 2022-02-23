### IMPORTS ###
from enum import Enum, auto
import functools


###################################################
### DEFINING TOKENS AND TOKEN TYPES FOR SCANNER ###
###################################################

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


################################
### SCANNER / LEXER FUNCTION ###
################################

def scan(source):
    token_list = []
    start = 0
    current = 0
    line = 1

    ### HELPER FUNCTIONS ###
    def is_at_end():
        return current >= len(source)

    def advance():
        nonlocal current
        char = source[current]
        current += 1
        return char
    
    def add_token(type, literal = None):
        lexeme = source[start:current]
        token_list.append(Token(type, lexeme, literal, line))
    
    def peek():
        if is_at_end(): return '\r'
        return source[current]
    
    ### LOOK UP CORROSPONDING PY STRING METHODS
    
    def is_symbolic(char):
        return (
            char == "!" or 
            (char >= "~" and char <= "`") or
            (char >= "*" and char <= ":") or 
            (char >= "<" and char <= "~")
            )

    # STRING SCANNING HELPER FUNCTION #
    def string():
        while peek() != '"':
            if peek() == '\n' or is_at_end(): # this scanner does not allow for multi-line strings
                raise Exception(line, "Unterminated string.")
            else:
                advance() # make sure I'm clear on why this isn't just current += 1
        advance()
        value = source[start + 1:current - 1]
        add_token(Types.STRING, value)

    # NUMBER SCANNING HELPER FUNCTION #
    def number():
        while peek().isdigit():
            advance()
        if peek() == ' ' or ')': # what do do about \n?
            value = int(source[start:current])
            add_token(Types.NUMBER, value)
        else:
            raise Exception(line, "Unexpected carachter.")

    # IDENTIFIER & KEYWORD SCANNING HELPER FUNCTION #
    def symbol():
        nonlocal current
        while is_symbolic(peek()):
            advance()
        type = Types.SYMBOL
        add_token(type)

    ### INNER LOOP ###
    def scan_token():
        nonlocal line
        char = advance()
        match char:
            # SINGLE CHAR TOKENS
            case '(': add_token(Types.LEFT_PAREN)
            case ')': add_token(Types.RIGHT_PAREN)

            # WHITESPASES
            case ' ': pass
            case '\r': pass
            case '\t': pass
            case '\n': line += 1

            # COMMENTS
            case ';':
                while peek() != '\n' and not is_at_end():
                    advance()
            
            # STRINGS
            case '"': string()

            # DEFAULT CASE
            case _:
                # NUMBERS
                if char.isdigit():
                    number()
                # IDENTIFIERS & KEYWORDS
                elif is_symbolic(char):
                    symbol()
                else:
                    raise Exception(line, "Unexpected character.")


    ### OUTER LOOP ###
    while not is_at_end():
        start = current
        scan_token()
    token_list.append(Token(Types.EOF,'', None, line))

    return token_list


#####################################################
### DEFINING SYMBOL FUNCTION AND CLASS FOR PARSER ###
#####################################################

@functools.cache
def symbol(lexeme):
    return Symbol(lexeme)

class Symbol:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value


#######################
### PARSER FUNCTION ###
#######################
def parse(token_list):
    stack = [[]]
    for token in token_list:
        match token.type:
            case Types.LEFT_PAREN : 
                stack.append([])
            case Types.RIGHT_PAREN :
                temp = stack.pop()
                if stack == []:
                    raise Exception("Unbalanced parentheses!!")
                stack[-1].append(temp)
            case Types.NUMBER :
                stack[-1].append(token.literal)
            case Types.STRING :
                stack[-1].append(token.literal)
            case Types.SYMBOL :
                stack[-1].append(symbol(token.lexeme))
            case Types.EOF :
                pass
            case _:
                raise Exception( "line:", token.line, token , "I think this token is invalid...")
    parsed = stack.pop().pop()
    if stack != []:
        raise Exception("Unbalanced parentheses!!")
    return parsed
        #"("means start new list
        #")"means close current list and go to next index of parent list
        # everything else means push x into the current list
        # x, for nums and strs, is the token's literal
        # x, for symbols is an instance of the symbol class w the relevant lexeme as its 


###############################
### SCAN AND PARSE FUNCTION ###
###############################      
def scan_n_parse(source):
    return parse(scan(source))