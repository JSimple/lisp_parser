from test import plus, Plusser, Token, Types

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

    ### INNER LOOP ###
    def scan_token():
        char = advance()
        match char:
            # SINGLE CHAR TOKENS
            case '(': add_token(Types.LEFT_PAREN)
            case ')': add_token(Types.RIGHT_PAREN)
            case ',': add_token(Types.COMMA)
            case '.': add_token(Types.DOT)
            case '-': add_token(Types.MINUS)
            case '+': add_token(Types.PLUS)
            case "'": add_token(Types.SINGLE_QUOTE)
            case ';': add_token(Types.SEMICOLON)
            case '*': add_token(Types.STAR)

            # DEFAULT CASE
            case _:
                raise Exception(line, "Unexpected character.")


    ### OUTER LOOP ###
    while not is_at_end():
        start = current
        scan_token()
    token_list.append(Token(EOF,'', None, line))

