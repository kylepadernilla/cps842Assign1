import Search
import pprint
f1=open('query.text','r')
f2=open('qrels.text','r')
separators = ".A .N"
punctuations = '''!()[];:'",<>./?@#$%^&*_~+-`=1234567890'''
#For the qrels comparison
rel_query = dict()
mapArr = []
repArr = []

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
        rel_query[pos1]['rel'].append(pos2)
    else:
        rel_query[pos1] = {'rel':[]}
        rel_query[pos1]['rel'].append(pos2)
#Finish with a dict of query:[documents] pairs

#For the query texts.
query_num = ''
user_input = ''
uiB = False
status = True
w1 = 0.5
w2 = 0.5
while(status):
    w1 = input("Please input cossim weight(e.g 0.5):")
    if float(w1) >= 0 and float(w1) <= 1:
        status = False
status = True
while(status):
    w2 = input('please input pagerank weight(e.g 0.5):')
    if float(w2) >= 0 and float(w2) <= 1:
        status = False
for line in f1:
        line_parts = line.split()
        if uiB:
            if line_parts[0] not in separators:
                user_input += line
            else:
                uiB = False
                no_punct =""
                for char in user_input:
                    if char not in punctuations:
                        no_punct = no_punct + char
                    else:
                        no_punct = no_punct + " "
                no_punct.lower()
                user_input = ''
                if query_num in rel_query:
                    ret_doc = Search.search(no_punct, len(rel_query[query_num].get('rel')), w1, w2)
                    rel_query[query_num]['ret'] = ret_doc
                else:
                    ret_doc = Search.search(no_punct, 0, w1, w2)
                    rel_query[query_num] = {'rel':[],'ret': ret_doc}
        if line_parts != []:
            if line_parts[0] == '.I':
                if len(line_parts[1]) == 1:
                    query_num = '0' + line_parts[1]
                else:
                    query_num = line_parts[1]
            elif line_parts[0] == '.W':
                uiB = True

#UP TO THIS POINT, EVERY QUERY HAS A RETRIEVED AND RELATIVE LIST.

for q in rel_query:
    rel_doc = 0
    ret_doc = 0
    avg_prec = 0
    relative = len(rel_query[q]['rel'])
    num_docs = len(rel_query[q]['ret'])
    for ret in rel_query[q]['ret']:
        ret_doc += 1
        if ret in rel_query[q]['rel']:
            rel_doc += 1


        precision = rel_doc / ret_doc
        avg_prec = precision + avg_prec

    if relative == 0:
        r_precision = 1
    else:
        r_precision = rel_doc / relative

    if num_docs == 0:
        avg_prec = 0
    else:
        avg_prec = avg_prec / num_docs
    mapArr.append(avg_prec)
    repArr.append(r_precision)

def Average(lst):
    return sum(lst) / len(lst)

averageMap = Average(mapArr)
print("average MAP Values: " + str(round(averageMap,2)))

averageR = Average(repArr)
print("average R-Precision Values: " + str(round(averageR,2)))