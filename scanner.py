from token import Token

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

    
    def add_token(type, literal):
        lexeme = source[start:current]
        token_list.append(Token(type, lexeme, literal, line))

    ### INNER LOOP ###
    def scan_token():
        char = advance()
        match char:
            case '(':
                add_token(LEFT_PAREN)


    ### OUTER LOOP ###
    while not is_at_end():
        start = current
        scan_token()
    token_list.append(Token(EOF,'', None, line))

