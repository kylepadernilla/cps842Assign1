with open('test.txt','r') as f:
    titleBool = False
    abstractBool = False
    for line in f:
        if(abstractBool):
            if(line.strip() == ".B"): #Checks to see if you're finished with the abstract paragraph
                abstractBool = False
            else:
                print(line) #returns abstract/continues printing abstract
        elif(titleBool):
            if(line.strip() == ".B"): #Checks to see if you're finished with the title
                titleBool = False
            elif(line.strip() == ".W"): #Checks to see if you're finished with the title
                titleBool = False
                abstractBool = True
            else:
                print(line) #returns the title
        else:
            if(line.strip() == ".T"): #Looks for title paragraph
                titleBool = True
            list = line.split()    
            for word in list:   
                if(word == ".I"): #Checks the split line list to see if it contains the index.
                    print(list[1]) #returns the document ID.
