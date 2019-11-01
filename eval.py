#import Search as search
f1=open('query.text','r')
f2=open('qrels.text','r')

#For the query texts.

for line in f1:
    print(line[0])
#For the qrels comparison
rel_query = dict()
for line in f2:
    pos1 = 0
    pos2 = 0
    position = 0
    for segment in line.split():
        if (position == 0):
            pos1 = segment
        elif (position == 1):
            pos2 = segment
        position += 1
    if pos1 in rel_query:
        rel_query[pos1].append(pos2)
    else:
        rel_query[pos1]= []
        rel_query[pos1].append(pos2)
#Finish with a dict of query:[documents] pairs