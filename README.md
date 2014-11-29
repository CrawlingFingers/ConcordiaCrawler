Application Flow
================

Indexing 
--------

The following steps illustrate retrieval & indexing.

1. Choose a folder for your data.  For the remainder of these steps, assume the data folder is `data/`.  The immediate subfolders of the data folder are the __categories__.

2. Use [Websphinx](http://www.cs.cmu.edu/~rcm/websphinx/) to crawl pages & save them in your `data/` folder.

3. Choose a folder for your index.  For the remainder of these steps, assume the index folder is `index/`.

4. Run `python app/indexer.py index "data/**/*"`.  The first parameter represents the index folder.  The second parameter is a unix glob pattern representing all the files to index.


Retrieval
---------

The following steps illustrate running a search query.  Retrieval is done using Lucene's [TFIDFSimilarity class](https://lucene.apache.org/core/4_0_0/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html).

1. Run `python app/retrieve.py <index_folder>` where `<index_folder>` is the path to your index.

2. Enter a query.


Questions
---------

The questions for the assignment are answered by running `python app/questions.py <index_folder>`, where `<index_folder>` is the path to the index.  

The general flow of the `questions.py` script follows:

1. Initialize retriever

2. Retrieve all documents organized by category, the original subfolder that the file was contained in.  For example, if the file was originally saved in `data/ece` then the category of the file is `ece`. 

3. Perform KMeans clustering on the sentiments of all documents, producing 3 sentiment centroids ("negative", "neutral", "positive").  

4. Give each category a sentiment ranking by:
    
    i. Classify each document as "negative", "neutral", "positive".
    
    ii. Assign each negative document a value of -1; each neutral document a value of 0; each positive document a value of 1.
    
    iii. Sum the values for a category.

5. Perform KMeans clustering on the overall sentiments of the categories, producing 3 centroids ("negative", "neutral", "positive").

6. Classify each category as "negative", "neutral" or "positive".

This method classifies a category as "negative", "neutral" or "positive" by examining how many docs in the category are "negative", "neutral" or "positive".  The docs themselves influence the class boundaries because the boundaries are computed using KMeans.