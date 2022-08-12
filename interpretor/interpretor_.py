import sys

variable_namespace = {}
counter = 0
j = 0
file_text = []

with open(sys.argv[1], "r") as f:
    list_of_lines = [row.strip() for row in f.readlines()]

    for row in list_of_lines:
        if row != "":
            file_text.append(row)

    for i in range(len(file_text)):
        if "}" in file_text[i]:
            counter += 1

        elif "{" in file_text[i]:
            counter -= 1

    if counter != 0:
        raise SyntaxError('Bro! number of "{" and "}" must be equal:')

    def untill_if(ind):
        """This function do file line by line untill will reach a line that starts with 'if'"""
        j = ind
        while j != len(file_text):
            if "if" in file_text[j]:
                break

            splitted_row = file_text[j].split()

            if "var" in file_text[j]:
                if not splitted_row[1][0].isalpha(): 
                    raise SyntaxError("Bro! variables must start with ascii letter:")
                
                variable_namespace[splitted_row[1]] = splitted_row[3]

            if splitted_row[0] in variable_namespace and splitted_row[1] == "=":
                if splitted_row[2] in variable_namespace:
                    splitted_row[2] = variable_namespace[splitted_row[2]]
                variable_namespace[splitted_row[0]] = splitted_row[2]       
    
            if "print" in file_text[j] and j <= len(file_text):
                splitted_row = ' '.join(list(file_text[j]))
                if splitted_row[5] != "[" and splitted_row[-1] != "]":
                    raise SyntaxError("Bro! after print you must start with '[' and finish with']'")

                splitted_row = (file_text[j].split("print["))[1].split("]")[0].split(" ")

                for i in range(len(splitted_row)):        
                    if splitted_row[i] in variable_namespace:
                        splitted_row[i] = variable_namespace[splitted_row[i]]     
                print(eval(' '.join(splitted_row)))
            j += 1
            
    def have_if():
        """This function do file line by line when reach a line that starts 'if'
         and will do untill will reach line that ends with '}':}'"""

        ind = 0

        while ind != len(file_text):
            if "if" in file_text[ind]:
                splitted_row = file_text[ind].split()
                if (file_text[ind + 1].split())[0] != "{":
                    raise SyntaxError("Bro! after if you must start with {")

                if "}" not in file_text[ind:]:
                    raise SyntaxError("Bro! after if you mast end with }") 

                for i in range(len(splitted_row)):
                    if splitted_row[i] in variable_namespace:
                        splitted_row[i] = str(variable_namespace[splitted_row[i]])          
                            
                if eval(' '.join(splitted_row[1:])):
                    while file_text[ind] != "}":
                        if "var" in file_text[ind]:
                            splitted_row = file_text[ind].split()
                            if not splitted_row[1][0].isalpha():
                                raise SyntaxError("Bro! variables must start with ascii letter:")

                            for i in range(3, len(splitted_row)):
                                if splitted_row[i] in variable_namespace:
                                    splitted_row[i] = str(variable_namespace[splitted_row[i]])
                            variable_namespace[splitted_row[1]] = eval(" ".join(splitted_row[3:]))    

                        splitted_row = file_text[ind].split()

                        if splitted_row[0] in variable_namespace and splitted_row[1] == "=":
                            for i in range(2, len(splitted_row)):
                                if splitted_row[i] in variable_namespace:
                                    splitted_row[i] = str(variable_namespace[splitted_row[i]])
                            variable_namespace[splitted_row[0]] = eval(" ".join(splitted_row[2:])) 

                        if "print" in file_text[ind]:
                            splitted_row = ' '.join(list(file_text[ind]))
                            if splitted_row[5] != "[" and splitted_row[-1] != "]":
                                raise SyntaxError("Bro! after print you must start with '[' and finish with']'")

                            splitted_row = (file_text[ind].split("print["))[1].split("]")[0].split(" ")
                            
                            for i in range(len(splitted_row)):       
                                if splitted_row[i] in variable_namespace:
                                    splitted_row[i] = variable_namespace[splitted_row[i]]     
                            print(eval(''.join(splitted_row)))     
                        ind += 1

                    if ind != len(file_text):
                        untill_if(ind)   

                else:
                    while "}" not in file_text[ind]:
                        ind += 1
                    untill_if(ind)
            ind += 1

    untill_if(j)                        
    have_if()

    if len(variable_namespace) != 0:
        print(variable_namespace)                                             