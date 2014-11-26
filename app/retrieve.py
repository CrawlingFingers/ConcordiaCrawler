import lucene
import sys

#This works (the deprecated code)

def uquery():
    print("Query:")
    userin = sys.stdin.readline()
    return userin

def main():
    lucene.initVM()
    directory = lucene.SimpleFSDirectory(lucene.File(sys.argv[1]))
    analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_30)
    search = lucene.IndexSearcher(directory)

    userq = uquery()
    query = lucene.QueryParser(lucene.Version.LUCENE_30, "content", analyzer)
    qq = query.parse(userq)
    maxhits = 5000
    hits = search.search(qq, maxhits)

    print "Found %d document(s) that matched the query '%s':" % (hits.totalHits, qq)

    for e in hits.scoreDocs:
        # print e.score, e.doc, e.toString()
        # doc = search.doc(e.doc)
        # print doc.get("content").encode("utf-8")
        doc = search.doc(e.doc)
        print doc.get("filepath")

if __name__ == "__main__":
    main()