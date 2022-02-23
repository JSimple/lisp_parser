from .token import Token, Types
from .scanner import scan
import functools

@functools.cache
def symbol(lexeme):
    return Symbol(lexeme)

class Symbol:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value

def parse(token_list):
    stack = [[]]
    for token in token_list:
        match token.type:
            case Types.LEFT_PAREN : 
                stack.append([])
            case Types.RIGHT_PAREN :
                temp = stack.pop()
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
        
def scan_n_parse(source):
    return parse(scan(source))