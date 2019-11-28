import pprint
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
f = open('cacm.all','r')
f3 = open('stopwords.txt','r')
stop_words = f3.read()
titleBool = False  #title
abstractBool = False  #abstract
pubdateBool = False  #publishing date
authorBool = False  #author
stopwordBool = False #stop word removal
stemBool = False #stemming component
linksBool = False #Page links
linksArr = []
punctuations = '''!()[];:'",<>./?@#$%^&*_~+-`=1234567890'''
identifiers = ".W .B .A .N .X .K "
word_dict = dict()
ps = PorterStemmer()
term_para = ""
author = ""
pubDate = ""
title = ""
doc_index = ""

status = True
while(status):
    input1 = input("Would you like to remove stop words? (y/n): ")
    if(input1.lower() == 'y'):
        stopwordBool = True
        status = False
    elif(input1.lower() == 'n'):
        status = False
    else:
        print("Input Valid Response!")
status = True
while(status):
    input1 = input("Would you like to stem words? (y/n): ")
    if(input1.lower() == 'y'):
        stemBool = True
        status = False
    elif(input1.lower() == 'n'):
        status = False
    else:
        print("Input Valid Response!")


for line in f:
    if(titleBool):
        if line.strip() in identifiers:
            titleBool = False
            term_para = title
            if (line.strip() == ".W"):
                abstractBool = True
            elif(line.strip() == ".B"):
                pubdateBool = True
            elif(line.strip() == ".A"):
                authorBool = True
                pubDate = "N/A"
            else:
                pubDate = "N/A"
                author = "N/A"
        else:
            title = title + line.strip()

    elif(abstractBool):
        if line.strip() in identifiers:
            abstractBool = False
            if(line.strip() == ".B"):
                pubdateBool = True
            elif(line.strip() == ".A"):
                authorBool = True
                pubDate = "N/A"
            else:
                pubDate = "N/A"
                author = "N/A"
        else:
            term_para = term_para + " " + line.strip()

    elif(pubdateBool):
        if line.strip() in identifiers:
            pubdateBool = False
            if(line.strip() == ".A"):
                authorBool = True
            else:
                author = "N/A"
        else:
            pubDate = pubDate + line.strip()

    elif(authorBool):
        if line.strip() in identifiers:
            authorBool = False
        else:
            author = author + line.strip()
    elif(linksBool):
        if line.split()[0] == ".I":
            linksBool = False
        else:
            if [line.split()[0],line.split()[2]] not in linksArr:
                linksArr.append([line.split()[0],line.split()[2]])
    else:
        if (".I" == line.split()[0]):
            #Converts term_para to a readable list no_punct
            no_punct =""
            for char in term_para:
                if char not in punctuations:
                    no_punct = no_punct + char
                else:
                    no_punct = no_punct + " "
            no_punct.lower()
            summary = no_punct.split()
            for index, terms in enumerate(summary):
                if(stemBool):
                    terms = ps.stem(terms)
                if(stopwordBool):
                    if terms not in stop_words:
                        doc_dict = {'title':title, 'author':author, 'pub_date':pubDate, 'term_freq': 1, 'positions':[index]}
                        if terms in word_dict:
                            if doc_index in word_dict[terms]["doc_index"]:
                                word_dict[terms]["doc_index"][doc_index]['positions'].append(index)
                                num = word_dict[terms]["doc_index"][doc_index].get('term_freq') + 1
                                word_dict[terms]["doc_index"][doc_index].update({'term_freq':num})
                            else:
                                num = word_dict[terms].get('doc_freq') + 1
                                word_dict[terms].update({"doc_freq": num})
                                word_dict[terms]["doc_index"].update({doc_index:doc_dict})
                        else:
                            word_dict[terms]={"doc_index":{doc_index:doc_dict},"doc_freq": 1}
                else:
                    doc_dict = {'title':title, 'author':author, 'pub_date':pubDate, 'term_freq': 1, 'positions':[index]}
                    if terms in word_dict:
                        if doc_index in word_dict[terms]["doc_index"]:
                            word_dict[terms]["doc_index"][doc_index]['positions'].append(index)
                            num = word_dict[terms]["doc_index"][doc_index].get('term_freq') + 1
                            word_dict[terms]["doc_index"][doc_index].update({'term_freq':num})
                        else:
                            num = word_dict[terms].get('doc_freq') + 1
                            word_dict[terms].update({"doc_freq": num})
                            word_dict[terms]["doc_index"].update({doc_index:doc_dict})
                    else:
                        word_dict[terms]={"doc_index":{doc_index:doc_dict},"doc_freq": 1}
                        

            term_para = ""
            author = ""
            pubDate = ""
            title = ""

            temp = line.split()
            doc_index = temp[1]
        elif ".T" in line:
            titleBool = True
        elif ".X" in line:
            linksBool = True

word_dict = eval(pprint.pformat(word_dict).lower())
f1=open('./dictionary','w+')
f2=open('./postings','w+')
f4=open('./links','w+')
for term in word_dict:
    print(word_dict[term]["doc_index"], file=f2)
    word_dict[term].pop("doc_index")
pprint.pprint(word_dict, f1)
pprint.pprint(linksArr, f4)
f.close()
f1.close()
f2.close()
f3.close()
f4.close()