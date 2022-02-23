def parse(token_list):
    parsed = []
    for token in token_list:
        pass
        #"("means start new list
        #")"means close current list and go to next index of parent list
        # everything else means push x into the current list
        # x, for nums and strs, is the token's literal
        # x, for symbols is an instance of the symbol class w the relevant lexeme as its value