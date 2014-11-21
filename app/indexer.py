import sys
import glob
import lucene
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

# parses a supplied file path
def parse_file (file_path):
  f = open(file_path, 'r')
  soup = BeautifulSoup(f.read())
  f.close()
  doc = Document()
  content_tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
  content = ""
  for tag in content_tags:
    matches = soup.find_all(tag)
    for match in matches:
      content += match.string + " "
  doc.add(Field("content", content, Field.Store.YES, Field.Index.ANALYZED))
  writer.addDocument(doc)

# initialize the lucene writer
def init_lucene (index_directory):
  d = SimpleFSDirectory(File(index_directory))
  analyzer = StandardAnalyzer(Version.LUCENE_30)
  return IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))

def main ():
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