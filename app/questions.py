from retrieve import Retriever
import sys

##############################################
# 
# The purpose of this script is to provide 
# explicit answers for all the questions in
# the project.
# 
##############################################


# check for provided args

if len(sys.argv) < 2:
  print("")
  print("Usage:")
  print("  python questions.py <index_location>")
  print("")
  sys.exit()



# initialize Retriever
retriever = Retriever(sys.argv[1])
collections = retriever.get_collections()