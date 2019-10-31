import pprint
import time
import math
import ui
from nltk.stem import PorterStemmer

f1=open('./dictionary','r')
f2=open('./postings','r')
f3 = open('stopwords.txt','r')
stop_words = f3.read()
bool_operators = {'and', 'not', 'or'}
counter = 0
n = 0
word_dict = dict(eval(f1.read()))
query = dict()
ps = PorterStemmer()
for term in word_dict:
    word_dict[term]["doc_index"] = eval(f2.readline()) #read posting doc as well.
    doc_index = word_dict[term]["doc_index"].keys()
    for keys in doc_index:
        if(int(keys) > n):
            n = int(keys) + 1 ##############DONT FORGET THIS AINT RIGHT

#word_dict = eval(pprint.pformat(word_dict))
swB = False
scB = False
status = True
while(status):
    input1 = input("Would you like to stem words? (y/n): ")
    if(input1.lower() == 'y'):
        scB = True
        status = False
    elif(input1.lower() == 'n'):
        status = False
    else:
        print("Input Valid Response!")
while(counter <= 0):
    query = dict()
    query_mag = 0
    rel_docs = []
    rel = dict()
    termsInput = input("Please input terms: ") #get user input.
    termsInput = termsInput.lower().split()
    for terms in termsInput:
        #This ends the crap
        if(terms == "zzend"):
            counter = counter + 1
        #Prevents boolean operators from happening
        elif terms in bool_operators:
            print("No boolean operators allowed.")
            break
        #Stems query if necessary
        else:
            if(swB):
                if terms in stop_words:
                    continue
            if(scB):
                terms = ps.stem(terms)
            if terms not in word_dict:
                continue
            update = 1
            tf = 1
            if terms not in query:
                df = word_dict[terms].get("doc_freq")
                query[terms] = {"f":1, "tf": 1, "idf": math.log(n/df), "w": 0}
            else:
                update = query[terms].get('f') + 1
                tf = 1 + math.log(update)
            w = tf*query[terms].get('idf')
            query[terms].update({'f':update, 'tf':tf, 'w':w})

            rel_docs = list(set(rel_docs)|set(list(word_dict[terms]['doc_index'].keys())))
    for terms in word_dict:
        for doc in rel_docs:
            if doc in word_dict[terms]['doc_index']:
                df = word_dict[terms].get('doc_freq')
                f = word_dict[terms]['doc_index'][doc].get('term_freq')
                tf = 1 + math.log(f)
                idf = math.log(n/df)
                w = tf*idf
                if doc not in rel:
                    rel[doc] = {'terms':{terms:{"f":f, "tf": tf, "idf": idf, "w": w}}}
                else:
                    rel[doc]['terms'][terms]= {"f":f, "tf": tf, "idf": idf, "w": w}
    for terms in query:
        temp = query[terms].get('w')**2
        query_mag = query_mag + temp
    query_mag = math.sqrt(query_mag)

    for doc in rel:
        doc_mag = 0
        for terms in rel[doc]['terms']:
            temp = rel[doc]['terms'][terms].get('w')**2
            doc_mag = doc_mag + temp
        rel[doc].update({'mag':math.sqrt(doc_mag)})
        #COSSIM()
        temp = 0
        for terms in query:
            if terms in rel[doc]['terms']:
                temp = temp + (query[terms].get('w') * rel[doc]['terms'][terms].get('w'))
                cossim = temp/(rel[doc].get('mag') * query_mag)
                rel[doc].update({'cossim':cossim})
    ui.results(rel,query,word_dict)





        
        
#            getTermsP = word_dict.get(terms) #get terms from dictionary with user input.
#            if(getTermsP): #if term exists in dictionary, print its contents.
#                pprint.pprint(word_dict[termsInput])
#            elif(termsInput == 'ZZEND'): #if user input is ZZEND.
#                print("program terminate.") #program terminates.
#                average = Average(averageList)
#                print("Average execution time:", round(average, 2)) #Calculates average execution time.
#                counter = counter + 1 #adds one to counter to break loop.
#
#            else:
#                print("term does not exist in dictionary. Please try again!") #let user know term does not exist.