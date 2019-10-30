#List of requirements:
#1. Multiple word search, (no AND, OR, NOT)
#   - Tokenize and parse through input.
#2. cosine similarity Formula for query and documents
#   - Requires Weights (TF * IDF)
#       - Requires DocID lists(for weights of every word)
#           > Maybe created during after input of query?
#               > i.e. creates array for only terms in query, searches for documents with said queries.
#       - Requires TF (1 + log(F))
#       - Requires IDF (log(N/DF))
#   - 
#3. Top-K retrieval method (maybe) 
#   > Champion List?
#
#4. 