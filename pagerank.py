import pprint
f = open('links','r')
unmatched_links = eval(f.read())
links = dict()
n = 3204
for link in unmatched_links:
    #if link[0] != link[1]: #ensures the page referencing itself does not get added.
    if link[1] in links: 
        links[link[1]]['incoming'].append(link[0])
    else:
        links[link[1]] = {'outgoing': 0, 'incoming': [], 'pagerank': 1/3204}
        links[link[1]]['incoming'].append(link[0])
    if link[0] in links:
        temp = int(links[link[1]].get('outgoing')) + 1
        links[link[0]].update({'outgoing':temp})
    else:
        links[link[0]] = {'outgoing': 1, 'incoming': [], 'pagerank': 1/3204}

for link in unmatched_links:
    if link[0] not in links:
        links[link[0]] = {'outgoing': 0, 'incoming': [link[1]], 'pagerank': 1/3204}

#AT THIS POINT, ALL THE DOCUMENTS HAVE INCOMING/OUTGOING/INITIAL PAGERANK //ITERATION 0 COMPLETE

def iteration():
    dampener = 0.85
    for link in links:
        if links[link]['incoming'] == [link]:
            #links[link].update({'pagerank': 0})
            continue #ignores pages with no outgoing as the pagerank will likely not change.
        t_incoming = links[link].get('incoming')
        pagerank = 0
        for doc in t_incoming:
            pagerank += links[doc].get('pagerank') / links[doc].get('outgoing')
        pagerank = (1-dampener) / links[link].get('outgoing') + dampener*pagerank
        links[link].update({'pagerank':pagerank})

iteration() #iteration 1
iteration() #iteration 2

prScore = dict()
for link in links:
    score = links[link].get('pagerank')
    prScore[link] = score
f2=open('prScores', 'w+')
pprint.pprint(prScore, f2)