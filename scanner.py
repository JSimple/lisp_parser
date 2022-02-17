from test import plus, Plusser, Token, Types
from keyword import keywords

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
        nonlocal current
        if is_at_end():
            return False
        if source[current] != expected:
            return False
        current += 1
        return True
    
    def peek():
        if is_at_end(): return '\r' ## does any NPC work here? or do I need a null carachter?
        return source[current]
    
    def is_digit(char):
        digits = {'0','1','2','3','4','5','6','7','8','9'} # this will allow for non-zero numbers to start w 0
        return char in digits

    def is_letter(char):
        return char == '_' or (char >= 'a' and char <= 'z')
    
    def is_alphanumeric(char):
        return is_letter(char) or is_digit(char)

    # STRING SCANNING HELPER FUNCTION #
    def string():
        nonlocal current
        while peek() is not '"':
            if peek() is '\n' or is_at_end(): # this scanner does not allow for multi-line strings
                raise Exception(line, "Unterminated string.")
            else:
                advance() # make sure I'm clear on why this isn't just current += 1
        value = source[start + 1:current - 1]
        add_token(Types.STRING, value)

    # NUMBER SCANNING HELPER FUNCTION #
    def number():
        while is_digit(peek()):
            advance()
        if peek() == ' ' or ')': # what do do about \n?
            value = int(source[start:current - 1])
            add_token(Types.NUMBER, value)
        else:
            raise Exception(line, "Unexpected carachter.")

    # IDENTIFIER & KEYWORD SCANNING HELPER FUNCTION #
    def identifier():
        nonlocal current
        while is_alphanumeric(peek()):
            advance()
        text = source[start:current]
        if text in set(keywords.keys()):
            type = keywords[text]
        else: 
            type = Types.IDENTIFIER
        add_token(type)
        

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
                # NUMBERS
                if is_digit(char):
                    number()
                # IDENTIFIERS & KEYWORDS
                elif is_letter(char):
                    identifier()
                else:
                    raise Exception(line, "Unexpected character.")


    ### OUTER LOOP ###
    while not is_at_end():
        start = current
        scan_token()
    token_list.append(Token(Types.EOF,'', None, line))
