import sys
import glob
import lucene
import afinn
from bs4 import BeautifulSoup
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version


# checks that the required command-line
# parameters were supplied
def check_params ():
  if len(sys.argv) < 3:
    print("Concordia Crawler.")
    print("")
    print("Usage: ")
    print("  python indexer.py <index_folder> <data_folder>")
    print("")
    sys.exit()

# parses a supplied file path
def parse_file (file_path, writer):
  f = open(file_path, 'r')
  soup = BeautifulSoup(f.read())
  f.close()
  doc = Document()
  content_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
  content = ""
  for tag in content_tags:
    matches = soup.find_all(tag)
    print(type(matches))
    for match in matches:
      if match.string:
        content += match.string + " "
  afinn_score = afinn.sentiment(content)
  doc.add(Field("filepath", file_path, Field.Store.YES, Field.Index.ANALYZED))
  doc.add(Field("content", content, Field.Store.YES, Field.Index.ANALYZED))
  doc.add(Field("sentiment", afinn_score, Field.Store.YES, Field.Index.ANALYZED))
  writer.addDocument(doc)

# initialize the lucene writer
def init_lucene (index_directory):
  d = SimpleFSDirectory(File(index_directory))
  analyzer = StandardAnalyzer(Version.LUCENE_30)
  return IndexWriter(d, analyzer, True, IndexWriter.MaxFieldLength(512))

def main ():
  lucene.initVM()
  check_params()
  files = glob.glob(sys.argv[2])
  directory = sys.argv[1]
  writer = init_lucene(directory)
  for f in files:
    parse_file(f, writer)
  writer.optimize()
  writer.close()




if __name__ == "__main__":
  main()