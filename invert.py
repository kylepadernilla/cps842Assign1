with open('test.txt','r') as f:
    titleBool = False
    abstractBool = False
    pubDateBool = False
    authorBool = False

    for line in f:
        if(titleBool or pubDateBool):
            if(line.strip() == ".B" or line.strip() == "N"): #Checks to see if you're finished with the title
                titleBool = False
                pubDateBool = False
            elif(line.strip() == ".W"): #Checks to see if you're finished with the title
                titleBool = False
                pubDateBool = False
                abstractBool = True

            elif(line.strip() == ".A"):
                titleBool = False
                pubDateBool = False
                authorBool = True
            else:
                print(line) #returns the title.

        else:
            if(line.strip() == ".T"): #Looks for title paragraph
                titleBool = True

            elif (line.strip() == ".B"):  # Looks for publication date.
                pubDateBool = True

            list = line.split()
            for word in list:
                if(word == ".I"): #Checks the split line list to see if it contains the index.
                    print(list[1]) #returns the document ID.

#B is similar to abstract bool.
#.A authorList is similar to .A authorlist.