#!/usr/bin/env python3


''' 
- review code based on this standards: 
    https://opensource.com/article/17/5/30-best-practices-software-development-and-testing

# Features:
- Can determine if function can be tested based on:
    - Input / Output
    - State based predictions (globals are bad!!)

- Can extract functions
    - With inputs
    - Without inputs

- Can define the boundary scopes of functions (start and end line)
'''

import re

def is_function(codeline, without_input=False, with_input=True):
    if with_input or (with_input is None and without_input is None):
        func_rgx="^def \w*\([\w\s\d\S]*\)[\s]*:"
        return re.search(func_rgx, codeline) is not None
    
    if without_input:
        func_rgx="^def \w*\(\)[\s]*:"
        return re.search(func_rgx, codeline) is not None

    return None

def function_scope(codebase, start_line):
    # print(codebase)
    # scoped=[]
    scoped=[]
    scope_rgx="^\s"
    codebase=codebase.split('\n')[start_line + 1:]
    # print(fr"{codebase}")
    endline=None
    line_count=None
    for i in range(len(codebase)):
        code_line = codebase[i]
        if code_line == "":
            continue
        # print("+", codebase[i], re.search(scope_rgx, code_line, re.DEBUG) is not None)
        # print("+", codebase[i], re.search(scope_rgx, code_line) is not None)
        if re.search(scope_rgx, code_line) is not None:
            # scoped.append(code_line)
            scoped.append(code_line)
            endline=start_line + i + 2
            line_count=endline - start_line
        else:
            break

    return '\n'.join(scoped), endline, line_count

def function_extraction(codebase, without_input=None, with_input=None):
    functions=[]
    split_codebase = codebase.split('\n')
    for i in range(len(split_codebase)):
        codeline = split_codebase[i]
        if is_function(codeline, without_input=without_input, with_input=with_input):
            scoped, endline, line_count = function_scope(codebase, i)
            functions.append(
                    {
                        "start_line":i+1, 
                        "scoped":scoped, 
                        "endline":endline, 
                        "line_count":line_count, 
                        "name":codeline})

    return functions


def empty_function(): 
    pass


if __name__ == "__main__":
    test_function = '''def test_function():\n   print("hello world")'''
    split_test_function = test_function.split('\n')

    print("tab test", split_test_function[1][0] == '\t')
    print("space test", split_test_function[1][0] == ' ')
    print(">>", is_function(test_function.split('\n')[0]))

    functions=function_extraction(test_function)
    print(">>", len(functions) == 1)

    scoped, endline, line_count = function_scope(test_function, 0)
    print(">>", scoped=='\tprint("hello world")', f"endline={endline}", f"line_count={line_count}")

    codebase=None
    with open("review.py", 'r') as fd_review:
        codebase = fd_review.read()

    # print("\n* With input:", function_extraction(codebase))
    # print("\n* Without input:", function_extraction(codebase, without_input=True))


    func_ext = function_extraction(codebase)
    func_ext_without_input = function_extraction(codebase, without_input=True)

    for func in func_ext:
        print("------------------")
        print("name:", func['name'])
        print("scope:", func['scoped'], end='\n\n')
