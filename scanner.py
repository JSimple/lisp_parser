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

    def char_matches(expected):
        if is_at_end():
            return False
        if source[current] != expected:
            return False
        current += 1
        return True
    
    def peek():
        if is_at_end(): return '\r' ## does any NPC work here? or do I need a null carachter?

    ### STRING SCANNING HELPER FUNCTION ###
    def string():
        pass

    ### NUMBER SCANNING HELPER FUNCTION ###
    def number():
        pass

    ### INNER LOOP ###
    def scan_token():
        nonlocal line
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
            case '*': add_token(Types.STAR)

            # TOKENS THAT CAN BE SINGLE OR DOUBLE CHAR
            case '>': add_token(Types.GREATER_EQUAL if char_matches('=') else Types.GREATER)
            case '<': add_token(Types.LESS_EQUAL if char_matches('=') else Types.LESS)
            case '/': add_token(Types.SLASH_EQUAL if char_matches('=') else Types.SLASH)

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
                raise Exception(line, "Unexpected character.")


    ### OUTER LOOP ###
    while not is_at_end():
        start = current
        scan_token()
    token_list.append(Token(Types.EOF,'', None, line))

