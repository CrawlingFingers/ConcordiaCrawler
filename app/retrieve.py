import lucene
import sys

def query():
    print("Query:\n")
    userin = sys.stdin.readline()
    return userin

def main():
    lucene.initVM()
    directory = lucene.SimpleFSDirectory(File(sys.argv[1]))
    analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_30)
    search = lucene.IndexSearcher(directory)

    query = lucene.QueryParser("content", analyzer).parse(query())
    maxhits = 1000
    hits = search.search(query, maxhits)


if __name__ == "__main__":
    main()