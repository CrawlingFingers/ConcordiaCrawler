import lucene
import sys

def uquery():
    print("Query:\n")
    userin = sys.stdin.readline()
    return userin

def main():
    lucene.initVM()
    directory = lucene.SimpleFSDirectory(lucene.File(sys.argv[1]))
    analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_30)
    search = lucene.IndexSearcher(directory)

    userq = uquery()
    query = lucene.QueryParser("content", analyzer).parse(userq)
    maxhits = 5000
    hits = search.search(query, maxhits)

    print "Found %d document(s) that matched the query '%s':" % (hits.totalHits, query)

    for e in hits.scoreDocs:
        print e.score, e.doc, e.toString()
        doc = search.doc(e.doc)
        print doc.get("content").encode("utf-8")

if __name__ == "__main__":
    main()