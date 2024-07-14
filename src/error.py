import sys

def generalError(string: str):
    print(string)
    sys.exit(1)

def parserError(string: str):
    generalError('Esplang Parser Error: ' + string)

def syntaxError(string: str):
    generalError('Esplang Syntax Error: ' + string)