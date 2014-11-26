import lucene
import sys

#This works (the deprecated code)

class Retriever:

  # initializes a retriever
  #
  # @param {string} dir_file_path   The path to the index directory
  def __init__ (self, dir_file_path):
    lucene.initVM()
    self.directory = lucene.SimpleFSDirectory(lucene.File(dir_file_path))
    self.analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_30)
    self.search = lucene.IndexSearcher(self.directory)


  # performs a query on the "content" field
  # 
  # @param {string} query_string  The query to perform on the "content" field
  # @param {integer} max_hits     The maximum number of results to return
  # @return {object}              A lucene.TopDocs object representing the top results
  def query_content (self, query_string, max_hits=5000):
    query_parser = lucene.QueryParser(lucene.Version.LUCENE_30, "content", self.analyzer)
    query = query.parse(query_string)
    return self.search.search(query, max_hits)



def uquery():
  print("Enter a query, or type \"quit\" to quit:")
  userin = sys.stdin.readline()
  return userin


def main():

  # check for args
  if len(sys.argv) < 2:
    print("")
    print("Usage: ")
    print("  python retrieve.py <index_directory>")
    print("")
    sys.exit()

  # init retriever
  retriever = Retriever(sys.argv[1])

  # init query loop
  while True:
    userq = uquery()
    
    if userq == "quit":
      print("Bye :)")
      sys.exit()
    
    hits = retriever.query_content(userq)
    print "Found %d document(s) that matched the query '%s':" % (hits.totalHits, qq)

    for e in hits.scoreDocs:
      # print e.score, e.doc, e.toString()
      # doc = search.doc(e.doc)
      # print doc.get("content").encode("utf-8")
      doc = search.doc(e.doc)
      print doc.get("filepath")

if __name__ == "__main__":
  main()