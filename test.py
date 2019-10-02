#We are going with the assumption that they want the stop word removal
#and stemming component to be implemented in the program test.
#e.g. Stemming and removing from the input provided
import pprint
import time
def Average(lst):
    return sum(lst) / len(lst)
f1=open('./documents','r')
f2=open('./postings','r')
counter = 0
averageList = []
word_dict = dict(eval(f1.read()))
for term in word_dict:
    word_dict[term]["doc_index"] = eval(f2.readline()) #read posting doc as well.

word_dict = eval(pprint.pformat(word_dict))

while(counter <= 0):
    termInput = input("Please input term: ") #get user input.
    getTermP = word_dict.get(termInput) #get term from dictionary with user input.
    start = time.time()

    if(getTermP): #if term exists in dictionary, print its contents.
        pprint.pprint(word_dict[termInput])
        my_list = [i for i in range(1000000)]
        elapsed_time_lc=(time.time()-start)
        print("Execution time: %d seconds" % elapsed_time_lc)
        averageList.append(elapsed_time_lc)

    elif(termInput == 'ZZEND'): #if user input is ZZEND.
        print("program terminate.") #program terminates.
        average = Average(averageList)
        print("Average execution time:", round(average, 2)) #Calculates average execution time.
        counter = counter + 1 #adds one to counter to break loop.

    else:
        print("term does not exist in dictionary. Please try again!") #let user know term does not exist.