# lisp_parser

This parser uses the following rules for a Lisp CFG:

S-expression    ->  atom | list
atom            ->  NUMBER | STRING | SYMBOL
list            ->  "(" S-expression+ ")"



(print (list (+ 1 2) 4 5 6))