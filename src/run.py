#Native
import os.path
import subprocess
import sys
import shutil

#Custom
from parser import Parser

version = "0.0.1"

class Interpreter:
    def Interpret(self, code : str) -> None:
        subprocess.call(["g++", "-o", "result", "output.cpp"])
        subprocess.call(["./result"])


def GetCode(filePath) -> str:
    if os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            return file.read()
    else:
        print("Input file not found")

def HandleArgs() -> None:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print('''
        Command line arguments:
        --help -h: Prints this message
        --version -b: Prints the version of the interpreter
        --run -r (default) [file]: Runs the interpreter on the file specified
            ''')
    elif sys.argv[1] == "--run" or sys.argv[1] == "-r":
        if len(sys.argv) < 3:
            print("Invalid number of arguments")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode((sys.argv[2])))
                interpreter = Interpreter()
                interpreter.Interpret(parser.code)
            else:
                print("File not found")
    elif os.path.isfile(sys.argv[1]):
        parser = Parser(GetCode(sys.argv[1]))
        interpreter = Interpreter()
        interpreter.Interpret(parser.code)
    else:
        print("Invalid argument")

    if (os.path.isfile("output.cpp")):
        os.remove("output.cpp")

def CheckArgs() -> str:
    if len(sys.argv) < 2:
        print("Invalid number of arguments")
    HandleArgs()
    
if __name__ == "__main__":
    CheckArgs()