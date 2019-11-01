from operator import itemgetter

def results(ret, query,word_dict):
    term_arr = []
    for doc in ret:
        for terms in ret[doc]['terms']:
            if terms in query:
                doc_arr = [terms,doc,str(ret[doc].get('cossim')),word_dict[terms]["doc_index"][doc].get('author'),word_dict[terms]["doc_index"][doc].get('title')]
                term_arr.append(doc_arr)
            sorted_arr = sorted(term_arr, key=itemgetter(2), reverse=True) #sorts Array in descending order.

    i = 0
    print("Top 5 Documents:")
    while i < len(sorted_arr) and i <= 5:
        doc_id = 1
        rel_no = 2
        author_id = 3
        doc_title = 4
        rank_order = int(i) +1
        print("Term: " + sorted_arr[i][0] + "\nDoc Title: " + sorted_arr[i][doc_title] +  "\nAuthor: " + sorted_arr[i][author_id]
            + "\nDocument ID: " + sorted_arr[i][doc_id] + "\nRelevant Score: " + sorted_arr[i][rel_no] + "\nRanking Order: " + (str(rank_order)) + "\n")
        i += 1

def ranking(ret, query):
    term_arr = []
    ranked = []
    if ret != {}:
        for doc in ret:
            doc_arr = [doc, str(ret[doc].get('cossim))'))]
            term_arr.append(doc_arr)
            sorted_arr = sorted(term_arr, key=itemgetter(1), reverse=True)
        i = 0
        while i < len(sorted_arr) and i <= 5:
            ranked.append(sorted_arr[i][0])
            i += 1
    return ranked