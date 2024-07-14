class Parser:
    def __init__(self, code: str):
        self.code = code
        self.code = self.parse()

    def parse(self):
        self.parseInclude()
        self.parseFunctions()
        self.parseBuiltinFunctions()
        self.parseVariables()
        self.parseForLoop()

        with open('output.cpp', 'w') as f:
            f.write(self.code)
        return self.code
    
    def parseInclude(self):
        code_lines = self.code.splitlines()
        for i, line in enumerate(code_lines):
            words = line.split()
            for wordNo, word in enumerate(words):

                ###################  PARSING IMPORTAR ########################
                if word == "importar" and not self.isString(word, line):
                    code_lines[i] = code_lines[i].replace("importar", "#include", 1)
                    if (wordNo + 1 < len(words) and words[wordNo + 1] == "entradaSalida;" and not self.isString(words[wordNo + 1], line)):
                        code_lines[i] = code_lines[i].replace("entradaSalida;", "<iostream>", 1)
                    break  # Rompe el bucle para evitar múltiples reemplazos en una sola línea
        self.code = "\n".join(code_lines)

    def parseFunctions(self):
        codeLines = self.code.splitlines()
        for i, line in enumerate(codeLines):
            words = line.split()
            ################### PARSING FUNCTIONS AND TYPES #############
            for wordNo, word in enumerate(words):
                if word == "funcion" and not self.isString(word, line):
                    # INT FUNCTION
                    if words[wordNo + 1] == "entera" and not self.isString(words[wordNo + 1], line):
                        codeLines[i] = codeLines[i].replace("funcion", "int", 1)
                        codeLines[i] = codeLines[i].replace("entera", "", 1)
                    # MAIN FUNCTION
                    if words[wordNo + 1] == "principal()" and not self.isString(words[wordNo + 2], line):
                        codeLines[i] = codeLines[i].replace("funcion", "int", 1)
                        codeLines[i] = codeLines[i].replace("principal()", "main()")
                        break
                    
        self.code = "\n".join(codeLines)

    def parseBuiltinFunctions(self):
        codeLines = self.code.splitlines()
        for i, line in enumerate(codeLines):
            words = line.split()
            ################### PARSING FUNCTIONS AND TYPES #############
            for wordNo, word in enumerate(words):
                # COUT
                if word == "imprimir" and not self.isString(word, line):
                    # CHECKING NEXT SYMBOLS
                    if words[wordNo + 1] == "<<" and not self.isString(words[wordNo + 1], line):
                        codeLines[i] = codeLines[i].replace("imprimir", "std::cout", 1)
                # RETURN 0
                elif word == "terminarCorrectamente;" and not self.isString(word, line):
                    codeLines[i] = codeLines[i].replace("terminarCorrectamente;", "return 0;")
                # CIN
                if word == "leer" and not self.isString(word, line):
                    # CHECKING NEXT SYMBOLS
                    if words[wordNo + 1] == ">>" and not self.isString(words[wordNo + 1], line):
                        codeLines[i] = codeLines[i].replace('leer', 'std::cin')
                    
        self.code = "\n".join(codeLines)

    def parseVariables(self):
        codeLines = self.code.splitlines()
        for i, line in enumerate(codeLines):
            words = line.split()    
            for wordNo, word in enumerate(words):
                if word == "variable" and not self.isString(word, line):
                    # INT VARIABLES
                    if words[wordNo + 1] == "entera" and not self.isString(words[wordNo + 1], line):
                        codeLines[i] = codeLines[i].replace("variable", "int")
                        codeLines[i] = codeLines[i].replace("entera", "")

        self.code = "\n".join(codeLines)

    def parseForLoop(self):
        codeLines = self.code.splitlines()
        for i, line in enumerate(codeLines):
            words = line.split()    
            for wordNo, word in enumerate(words):
                if word == "para" and not self.isString(word, line):
                    codeLines[i] = codeLines[i].replace("para", "for")

        self.code = "\n".join(codeLines)
                    

    def isString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True