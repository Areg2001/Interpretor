import sys
variable_namespace = {}


with open("file.txt", "r") as f:
    file_text = [row.strip() for row in f.readlines()]
    j = 0
    if not file_text:
        sys.exit()
    while "if" not in file_text[j].split() and j <= len(file_text):
        if "var" in file_text[j]:
            splitted_row = file_text[j].split()
            variable_namespace[splitted_row[1]] = splitted_row[-1]
    
        if "print" in file_text[j] and j <= len(file_text):
            splitted_row = list(''.join(list(file_text[j])[6:-1]))
            for i in range(len(splitted_row)):        
                if splitted_row[i] in variable_namespace:
                    splitted_row[i] = variable_namespace[splitted_row[i]]     
            print(eval(''.join(splitted_row)))
        j += 1   

    for ind in range(len(file_text)):
        if "if" in file_text[ind]:
            splitted_row = file_text[ind].split()
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
                

            
                
    print(variable_namespace)        
        
    