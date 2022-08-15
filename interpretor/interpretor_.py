from sys import argv

variable_namespace = {}
counter = 0
j = 0
file_text = []

with open(argv[1], "r") as f:
    list_of_lines = [row.strip() for row in f.readlines()]

    for row in list_of_lines:
        if row != "":
            file_text.append(row)

    def Counter(txt, counter):
        """This Function is cheking count of '{' and '}'. They must be equal:"""   

        for line in txt:
            if "}" in line:
                counter += 1

            elif "{" in line:
                counter -= 1

        if counter != 0:
            raise SyntaxError('Bro! number of "{" and "}" must be equal:')

    def printing(txt, row, idx):
        if "print" in txt[idx] and j <= len(txt):
            row = ' '.join(list(txt[idx]))
            if row[5] != "[" and row[-1] != "]":
                raise SyntaxError("Bro! after print you must start with '[' and finish with']'")

            row = (file_text[idx].split("print["))[1].split("]")[0].split(" ")

            for i in range(len(row)):        
                if row[i] in variable_namespace:
                    row[i] = str(variable_namespace[row[i]])

            print(eval(' '.join(row)))    

    def VariableAfterDeclaring(arg, idx):
        arg = file_text[idx].split()
        if arg[0] in variable_namespace and arg[1] == "=":
            for i in range(2, len(arg)):
                if arg[i] in variable_namespace:
                    arg[i] = str(variable_namespace[arg[i]])
            variable_namespace[arg[0]] = eval(" ".join(arg[2:]))

    def alreadyDeclared(row, idx):
        "This function is cheking, that declared variables were not been declared. "
        
        row = file_text[idx].split()
        if row[1] in variable_namespace:
            raise SyntaxError(f"Bro! {(row[1])} already declared.")


    def CreatingVariable(arg):
        """This function assign value in variable."""

        for i in range(3, len(arg)):
            if arg[i] in variable_namespace:
                arg[i] = str(variable_namespace[arg[i]])
        variable_namespace[arg[1]] = eval(" ".join(arg[3:]))


    def variableName(row):
        """This function is cheking or does it starts with ascii letter?"""

        if not row[1][0].isalpha():
            raise SyntaxError("Bro! variables must start with ascii letter.")

    def variableValue(row):
        for i in range(len(row)):
            if row[i] in variable_namespace:
                row[i] = str(variable_namespace[row[i]])

    def isDeclared(row, idx):
        row = file_text[idx].split()
        for i in range(5):
            if row[0] in variable_namespace or ["if", "print", "var", "}", "{"][i] in row[0]:
                return True

        raise NameError(f"Bro! Name ({str(row[0])})' is unrecognizable.")    
                           
    def afterIf(idx):
        """This function is checking, or does it starts with '{' and ends with '}'?"""

        if(file_text[idx + 1].split())[0] != "{":
            raise SyntaxError("Bro! after if you must start with {") 

        if "}" not in file_text[idx:]:
            raise SyntaxError("Bro! after if you mast end with }")                

    def untill_if(ind):
        """This function do file line by line untill will reach a line that starts with 'if'"""

        j = ind

        while j != len(file_text):
            if "if" in file_text[j]:
                break

            splitted_row = file_text[j].split()

            if "var" in file_text[j]:
                variableName(splitted_row)
                alreadyDeclared(splitted_row, j)
                CreatingVariable(splitted_row)

            VariableAfterDeclaring(splitted_row, j)
            isDeclared(splitted_row, j)        
            printing(file_text, splitted_row, j)

            j += 1
            
    def have_if():
        """This function do file line by line when reach a line that starts 'if'
         and will do untill will reach line that ends with '}':}'"""

        ind = 0

        while ind != len(file_text):
            if "if" in file_text[ind]:
                splitted_row = file_text[ind].split()
                afterIf(ind)
                variableValue(splitted_row)         
                            
                if eval(' '.join(splitted_row[1:])):
                    while file_text[ind] != "}":
                        if "var" in file_text[ind]:
                            splitted_row = file_text[ind].split()
                            variableName(splitted_row) 
                            alreadyDeclared(splitted_row, ind)
                            CreatingVariable(splitted_row)  

                        VariableAfterDeclaring(splitted_row, ind)
                        isDeclared(splitted_row, ind)     
                        printing(file_text, splitted_row, ind)
                    
                        ind += 1

                    if ind != len(file_text):
                        untill_if(ind)   

                else:
                    while "}" not in file_text[ind]:
                        ind += 1
                    untill_if(ind)
            ind += 1

    Counter(file_text, counter)
    untill_if(j)                        
    have_if()

    if len(variable_namespace) != 0:
        print(variable_namespace)                                          