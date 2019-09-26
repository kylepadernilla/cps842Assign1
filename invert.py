with open('test.txt','r') as f:
    titleBool = False
    abstractBool = False
    pubDateBool = False
    authorBool = False
    for line in f:
        if(titleBool):
            if(line.strip() == ".B"): #Checks to see if you're finished with the title
                titleBool = False
            elif(line.strip() == ".W"): #Checks to see if you're finished with the title
                titleBool = False
                abstractBool = True
            else:
                print(line) #returns the title

        elif (pubDateBool):
            if (line == ".N"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
            elif (line.strip() == ".A"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
                authorBool = True
            else:
                print(line)  # returns the pubDate.
        else:
            if(line.strip() == ".T"): #Looks for title paragraph
                titleBool = True

            elif(line.strip() == ".B"): #Looks for publication date.
                pubDateBool = True

            list = line.split()    
            for word in list:   
                if(word == ".I"): #Checks the split line list to see if it contains the index.
                    print(list[1]) #returns the document ID.

#B is similar to abstract bool.
#.A authorList is similar to .A authorlist.