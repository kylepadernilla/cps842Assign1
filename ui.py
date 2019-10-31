def results(ret, query):
    for doc in ret:
        for terms in ret[doc]['terms']:
            if terms in query:
                print("Document ID: " + doc + ", Relevance: " + str(ret[doc].get('cossim')))