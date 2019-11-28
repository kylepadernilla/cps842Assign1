Harley Guanlao
Kyle Padernilla

Assignment 2: CPS 842

Details of our Program:
1. Postings lists is ordered alphabetically by term.
2. We have implemented top-K retrieval method particularly 
Champions list that gets the top 5 most relevant documents.
3. We used 1 + log(Term Frequency) * log(Number of Documents/Document Freqquency) as our variation of TF-IDF scheme for both documents and queries.

To run program:
1. First make sure you have nltk installed in your computer. On the command prompt in windows with python installed, type in: 
-m ensurepip --default-pip
This will ensure pip is installed in your pc/laptop. You are now ready to open the files.
2.Run the invert.py file.
3.It will ask you if you would you like to remove stop words, type in y for yes and n for no.
4.Then, it will ask you if you want to stem all the words, type in y for yes and n for no.
5.It will then create the postings and dictionary files and exit the program.
6. next run the search.py file. It automatically runs the ui.py which asks for user input. It will retrieve the top 5 relevant documents basing it off the user input.
7. Run the eval.py file to list the average MAP and R-precision values over all queries.