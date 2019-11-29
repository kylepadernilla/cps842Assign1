from operator import itemgetter

def results(ret, query,word_dict):
    f= open('prScores')
    prScores = []
    prScores = eval(f.read())
    term_arr = []
    min_cossim = 1
    min_prscore = 1
    max_cossim = 0
    max_prscore = 0
    for doc in prScores:
        if prScores.get(doc) > max_prscore:
            max_prscore = prScores.get(doc)
        if prScores.get(doc) < min_prscore:
            min_prscore = prScores.get(doc)
    for doc in ret:
        if ret[doc].get('cossim') > max_cossim:
            max_cossim = ret[doc].get('cossim')
        if ret[doc].get('cossim') < min_cossim:
            min_cossim = ret[doc].get('cossim')
    dif_cossim = max_cossim - min_cossim
    if dif_cossim == 0:
        min_cossim = 0
        dif_cossim = 1

    dif_prscore = max_prscore - min_prscore
    if dif_prscore == 0:
        min_prscore = 0
        dif_prscore = 1
    for doc in ret:
        for terms in ret[doc]['terms']:
            if terms in query:
                lsScore = (((ret[doc].get('cossim') - min_cossim)/dif_cossim) * 0.5) + (((prScores.get(doc) - dif_prscore) / dif_prscore) * 0.5)
                doc_arr = [terms,doc,str(ret[doc].get('cossim')),word_dict[terms]["doc_index"][doc].get('author'),word_dict[terms]["doc_index"][doc].get('title'), prScores[doc], lsScore]
                term_arr.append(doc_arr)
            sorted_arr = sorted(term_arr, key=itemgetter(6), reverse=True) #sorts Array in descending order.

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
    prScores = eval(f.read())
    term_arr = []
    ranked = []
    min_cossim = 1
    min_prscore = 1
    max_cossim = 0
    max_prscore = 0
    for doc in prScores:
        if prScores.get(doc) > max_prscore:
            max_prscore = prScores.get(doc)
        if prScores.get(doc) < min_prscore:
            min_prscore = prScores.get(doc)
    for doc in ret:
        if ret[doc].get('cossim') > max_cossim:
            max_cossim = ret[doc].get('cossim')
        if ret[doc].get('cossim') < min_cossim:
            min_cossim = ret[doc].get('cossim')
    dif_cossim = max_cossim - min_cossim
    if dif_cossim == 0:
        min_cossim = 0
        dif_cossim = 1

    dif_prscore = max_prscore - min_prscore
    if dif_prscore == 0:
        min_prscore = 0
        dif_prscore = 1
    if ret != {}:
        for doc in ret:
            lsScore = (((ret[doc].get('cossim') - min_cossim)/dif_cossim) * w1) + (((prScores.get(doc) - dif_prscore) / dif_prscore) * w2)
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