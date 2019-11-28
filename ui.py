from operator import itemgetter

def results(ret, query,word_dict):
    f= open('prScores')
    prScores = f.read()
    term_arr = []
    for doc in ret:
        for terms in ret[doc]['terms']:
            if terms in query:
                lsScore = (ret[doc].get('cossim') * 0.5) + (prScores.get('doc') * 0.5)
                doc_arr = [terms,doc,str(ret[doc].get('cossim')),word_dict[terms]["doc_index"][doc].get('author'),word_dict[terms]["doc_index"][doc].get('title'), prScores[doc], lsScore]
                term_arr.append(doc_arr)
            sorted_arr = sorted(term_arr, key=itemgetter(2), reverse=True) #sorts Array in descending order.

    i = 0
    print("Top 5 Documents:")
    while i < len(sorted_arr) and i <= 5:
        doc_id = 1
        rel_no = 2
        author_id = 3
        doc_title = 4
        pr_score = 5
        combined_score = 6
        rank_order = int(i) +1
        print("Term: " + sorted_arr[i][0] + "\nDoc Title: " + sorted_arr[i][doc_title] +  "\nAuthor: " + sorted_arr[i][author_id]
            + "\nDocument ID: " + sorted_arr[i][doc_id] + "\nRelevance Score: " + sorted_arr[i][rel_no] + "\nPageRank Score: " + sorted_arr[i][pr_score] + "\nCombined Score: " + sorted_arr[i][combined_score] + "\nRanking Order: " + (str(rank_order)) + "\n")
        i += 1
    f.close()
def ranking(ret, query, num, w1, w2):
    f= open('prScores')
    prScores = f.read()
    term_arr = []
    ranked = []
    if ret != {}:
        for doc in ret:
            lsScore = (ret[doc].get('cossim') * w1) + (prScores.get('doc') * w2)
            doc_arr = [doc, lsScore]
            term_arr.append(doc_arr)
            sorted_arr = sorted(term_arr, key=itemgetter(1), reverse=True)
        i = 0
        if num < 5:
            num = 5
        while i < len(sorted_arr) and i <= num:
            ranked.append(sorted_arr[i][0])
            i += 1
    f.close()
    return ranked