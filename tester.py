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

line = "dog cat moose cow ass dog moose dog"



words = line.split()
for index, terms in enumerate(words):
    doc_dict = {'Title':title, 'Author':author, 'Pub_Date':pubDate, 'Term_Freq': 1, 'Positions':[index]}
    if terms in word_dict:
        if doc_index in word_dict[terms]:
            word_dict[terms][doc_index]['Positions'].append(index)
            num = word_dict[terms][doc_index].get('Term_Freq') + 1
            word_dict[terms][doc_index].update({'Term_Freq':num})
        else:
            num = word_dict[terms].get('Doc_Freq') + 1
            word_dict[terms].update({doc_index:doc_dict, "Doc_Freq": num})
    else:
        word_dict[terms]={doc_index:doc_dict,"Doc_Freq": 1}

title = "animals in the wild"
pubDate = "2037"
doc_index = "2"
author = "Harley the 4th G"

line = "cat moose duck jaguar goat dog monkey dog"

words = line.split()
for index, terms in enumerate(words):
    doc_dict = {'Title':title, 'Author':author, 'Pub_Date':pubDate, 'Term_Freq': 1, 'Positions':[index]}
    if terms in word_dict:
        if doc_index in word_dict[terms]:
            word_dict[terms][doc_index]['Positions'].append(index)
            num = word_dict[terms][doc_index].get('Term_Freq') + 1
            word_dict[terms][doc_index].update({'Term_Freq':num})
        else:
            num = word_dict[terms].get('Doc_Freq') + 1
            word_dict[terms].update({doc_index:doc_dict, "Doc_Freq": num})
    else:
        word_dict[terms]={doc_index:doc_dict,"Doc_Freq": 1}

    
pprint.pprint(word_dict)