import pprint
f1=open('./documents','r')
f2=open('./postings','r')
word_dict = dict(eval(f1.read()))
for term in word_dict:
    word_dict[term]["Doc_Index"] = eval(f2.readline())

word_dict = eval(pprint.pformat(word_dict))
print(word_dict['ass'])