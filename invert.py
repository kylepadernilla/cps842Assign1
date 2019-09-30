with open('test.txt','r') as f:
    titleBool = False
    abstractBool = False
    pubDateBool = False
    authorBool = False

    word_dict = dict() #essentially the dictionary, holding every single term.
        #Term Dictionary (terms):
            #Document Frequency //Essentially Dictionary.txt *along with terms*
            #Document Dictionary (doc_ID) //Essentially Postings_Lists.txt
                #Title
                #Term Frequency
                #Positions
                #Summary (4 words prior first Term position, 5 words after?)

    term_para = "" #Holds the entire paragraph (Will be split into words) temporarily
    author = "" #Holds the authors temporarily
    pubDate = "" #Holds the publication date temporarily
    title = "" #Holds the title temporarily
    doc_index = "" #Holds the current document index
    for line in f:

        if(titleBool):
            if(line.strip() == ".B"): #Checks to see if you're finished with the title
                titleBool = False
                pubDateBool = True
                term_para = title
            elif(line.strip() == ".W"): #Checks to see if you're finished with the title.
                titleBool = False
                abstractBool = True
                term_para = title
            elif (line.strip() == ".A"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
                authorBool = True

            else:
                title = title + line
        
        elif(pubDateBool):
            if (line.strip() == ".N"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False

            elif (line.strip() == ".A"):  # Checks to see if you're finished with the publication date.
                pubDateBool = False
                authorBool = True
            
            else:
                pubDate = pubDate + line

        elif(abstractBool):
            if (line.strip() == ".B"):  # Checks to see if you're finished with the abstrac
                abstractBool = False
                pubDateBool = True
            else:
                term_para = term_para + line

        elif(authorBool):
            if (line.strip() == ".N"):  # Checks to see if you're finished with the author.
                authorBool = False
            else:
                author = author + "," + line  # returns the author.

        else:
            if (line.strip() == ".T"):  # Looks for Title.
                titleBool = True

            else: #Really only happens on a new index.
                
                #Begin dictionary filling process here!!!
                    #
                    #
                    #
                    #
                    #
                    #

                #Resetting the terms for the next document to handle.
                term_para = "" #Holds the entire paragraph (Will be split into words) temporarily
                author = "" #Holds the authors temporarily
                pubDate = "" #Holds the publication date temporarily
                title = "" #Holds the title temporarily
                doc_index = "" #Holds the current document index
                
                list = line.split()
                for word in list:
                    if(word == ".I"): #Checks the split line list to see if it contains the index.
                        doc_index = list[1] #returns the document ID.

#B is similar to abstract bool.
#.A authorList is similar to .A authorlist.