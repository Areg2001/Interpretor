with open("file.txt", "r") as f:
    variable_namespace = {}
    file_text = [row.strip() for row in f.readlines()]
    j = 0
    counter = 0
    for i in range(len(file_text)):
        if "}" in file_text[i]:
            counter += 1

        elif "{" in file_text[i]:
            counter -= 1
    if counter != 0:
        raise SyntaxError('Bro! number of "{" and "}" must be equal:')

    def untill_if(idx):
        """This function do file line by line untill will reach line that starts with 'if'"""
        j = idx
        while j != len(file_text):
            if "if" in file_text[j]:
                break

            if "var" in file_text[j]:
                splitted_row = file_text[j].split()
                variable_namespace[splitted_row[1]] = splitted_row[-1]
    
            if "print" in file_text[j] and j <= len(file_text):
                splitted_row = (file_text[j].split("print("))[1].split(")")[0].split(" ")
                for i in range(len(splitted_row)):        
                    if splitted_row[i] in variable_namespace:
                        splitted_row[i] = variable_namespace[splitted_row[i]]     
                print(eval(' '.join(splitted_row)))
            j += 1
    untill_if(j)         
    index = 0
    def have_if():
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
                        splitted_row[i] = variable_namespace[splitted_row[i]]          
                            
                if eval(' '.join(splitted_row[1:])):
                    while file_text[ind] != "}":
                        if "var" in file_text[ind]:
                            splitted_row = file_text[ind].split()
                            variable_namespace[splitted_row[1]] = splitted_row[3]

                        if "print" in file_text[ind]:
                            splitted_row = list(''.join(list(file_text[ind])[6:-1]))
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
    have_if()

    if len(variable_namespace) != 0:
        print(variable_namespace)                                         