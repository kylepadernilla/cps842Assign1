with open('test.txt','r') as f:
    titleBool = False
    abstractBool = False
    pubDateBool = False
    authorBool = False

    for line in f:

        if(titleBool or pubDateBool):
            if(line.strip() == ".B"): #Checks to see if you're finished with the title
                titleBool = False
                pubDateBool = True
            elif(line.strip() == ".W"): #Checks to see if you're finished with the title
                titleBool = False
                abstractBool = True
            elif (line.strip() == ".N"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
            elif (line.strip() == ".A"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
                authorBool = True
            else:
                print(line) #returns the title.

        elif(abstractBool):
            if (line.strip() == ".B"):  # Checks to see if you're finished with the abstract
                abstractBool = False
                pubDateBool = True
            else:
                print(line)  # returns the title.

        elif(authorBool):
            if (line.strip() == ".N"):  # Checks to see if you're finished with the abstract
                authorBool = False
            else:
                print(line)  # returns the title.

        else:
            if (line.strip() == ".T"):  # Looks for Title.
                titleBool = True

            list = line.split()
            for word in list:
                if(word == ".I"): #Checks the split line list to see if it contains the index.
                    print(list[1]) #returns the document ID.

#B is similar to abstract bool.
#.A authorList is similar to .A authorlist.