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
def is_function(codeline):
    func_rgx="def \w*\([\w\s\d]*\)[\s\t]*:"
    return re.fullmatch(func_rgx, codeline) is not None


def function_extraction(codebase):
    functions={}
    for i in range(len(codebase)):
        codeline = codebase[i]
        if is_function(codeline):
           functions[i] = codeline


    return functions


if __name__ == "__main__":
    test_function = '''def test_function():
    print("hello world")'''

    print(test_function)
    print(is_function(test_function.split('\n')[0]))
    # list_functions = function_extract(codebase)
