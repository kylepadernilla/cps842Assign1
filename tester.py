#Inside the hashmap we need:
#Dictionary file:
#   Term
#   Document Frequency
#Postings File:
#   Document ID
#       Term Frequency
#       Positions
#
#

import pprint
word_dict = dict()

title = "animals in theory"
pubDate = "1997"
doc_index = "1"
author = "Harley G"
f1=open('./documents','w+')
f2=open('./postings','w+')
line = "dog cat moose cow ass dog moose dog"



words = line.split()
for index, terms in enumerate(words):
    doc_dict = {'Title':title, 'Author':author, 'Pub_Date':pubDate, 'Term_Freq': 1, 'Positions':[index]}
    if terms in word_dict:
        if doc_index in word_dict[terms]["Doc_Index"]:
            word_dict[terms]["Doc_Index"][doc_index]['Positions'].append(index)
            num = word_dict[terms]["Doc_Index"][doc_index].get('Term_Freq') + 1
            word_dict[terms]["Doc_Index"][doc_index].update({'Term_Freq':num})
        else:
            num = word_dict[terms].get('Doc_Freq') + 1
            word_dict[terms].update({"Doc_Freq": num})
            word_dict[terms]["Doc_Index"].update({doc_index:doc_dict})
    else:
        word_dict[terms]={"Doc_Index":{doc_index:doc_dict},"Doc_Freq": 1}

title = "animals in the wild"
pubDate = "2037"
doc_index = "2"
author = "Harley the 4th G"

line = "cat moose duck jaguar goat dog monkey dog"

words = line.split()
for index, terms in enumerate(words):
    doc_dict = {'Title':title, 'Author':author, 'Pub_Date':pubDate, 'Term_Freq': 1, 'Positions':[index]}
    if terms in word_dict:
        if doc_index in word_dict[terms]["Doc_Index"]:
            word_dict[terms]["Doc_Index"][doc_index]['Positions'].append(index)
            num = word_dict[terms]["Doc_Index"][doc_index].get('Term_Freq') + 1
            word_dict[terms]["Doc_Index"][doc_index].update({'Term_Freq':num})
        else:
            num = word_dict[terms].get('Doc_Freq') + 1
            word_dict[terms].update({"Doc_Freq": num})
            word_dict[terms]["Doc_Index"].update({doc_index:doc_dict})
    else:
        word_dict[terms]={"Doc_Index":{doc_index:doc_dict},"Doc_Freq": 1}

word_dict = eval(pprint.pformat(word_dict))
x = word_dict.copy()
for term in x:
    print(x[term]["Doc_Index"], file=f2)

y = word_dict.copy()
for term in y:
    y[term].pop("Doc_Index")
pprint.pprint(y, f1)
f1.close()
f2.close()
