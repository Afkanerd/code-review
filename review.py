#!/usr/bin/env python3


''' 
- review code based on this standards: 
    https://opensource.com/article/17/5/30-best-practices-software-development-and-testing

# Features:
- Test code based on 
    - Input / Output
    - State based predictions (globals are bad!!)
'''

import re

def is_function(codeline, without_input=False, with_input=True):
    """
    if not without_input and not with_input:
        if is_function(codeline, with_input=True):
            return True
        elif is_function(codeline, without_input=True):
            return True
    """

    if with_input or (with_input is None and without_input is None):
        func_rgx="def \w*\([\w\s\d\S]*\)[\s\t]*:"
        return re.fullmatch(func_rgx, codeline) is not None
    
    if without_input:
        func_rgx="def \w*\(\)[\s\t]*:"
        return re.fullmatch(func_rgx, codeline) is not None

    return None


def function_extraction(codebase, without_input=None, with_input=None):
    functions={}
    codebase = codebase.split('\n')
    for i in range(len(codebase)):
        codeline = codebase[i]
        if is_function(codeline, without_input=without_input, with_input=with_input):
           functions[i+1] = codeline


    return functions

def empty_function():
    pass


if __name__ == "__main__":
    test_function = '''def test_function():
    print("hello world")'''

    print(test_function)
    print(">>", is_function(test_function.split('\n')[0]))
    # list_functions = function_extract(codebase)


    functions=function_extraction(test_function)
    print(">>", len(functions) == 1)


    codebase=None
    with open("review.py", 'r') as fd_review:
        codebase = fd_review.read()

    print("* With input:", function_extraction(codebase))
    print("* Without input:", function_extraction(codebase, without_input=True))
