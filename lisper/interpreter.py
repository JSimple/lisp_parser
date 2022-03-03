from .parser import scan_n_parse


# example: 
# input: '(+(+ 1 2 ) 3 )'
# output: ['+',['+', 1, 2], 3]
# input: [5]
# output: 

def interp(expr):
    
    if not isinstance(expr, list):
        return expr

    interp_args = []

    for arg in expr[1:]:
        evaled = interp(arg)
        interp_args.append(evaled)
    
    return(sum(interp_args))

def s_p_i(lisp):
    return interp(scan_n_parse(lisp))


#### TEST CASE ###
print(s_p_i('(+(+ 1 2 ) 3 )'))