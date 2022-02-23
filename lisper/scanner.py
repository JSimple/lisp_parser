from .token import Token, Types

### SCANNER / LEXER FUNCTION ###
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
        if is_at_end(): return '\r' ## does any NPC work here? or do I need a null carachter?
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

## TEST CASES ##

source1 = '(write 1 2 3 "string")'
source2 = '(0(3(1(+->='
source3 = '(list 1 (* 3 2) nil)'

parsed = scan(source3)

#print(parsed)
