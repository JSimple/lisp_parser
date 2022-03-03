from .token import Token, Types
from .scanner import scan
import functools


#####################################################
### DEFINING SYMBOL FUNCTION AND CLASS FOR PARSER ###
#####################################################

# caching because symbols are unique in Lisp
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

# stack:
# [[]]

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


###############################
### SCAN AND PARSE FUNCTION ###
############################### 

def scan_n_parse(source):
    return parse(scan(source))


##################
### TEST CASES ###
##################

lisp1 = '(defun foo (a b c d) (+ a b c d))'

print(scan_n_parse(lisp1))

# example: 
# input: '(+(+ 1 2 ) 3 )'
# output: ['+',['+', 1, 2], 3]