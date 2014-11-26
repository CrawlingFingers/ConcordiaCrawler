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


# rank collections by sentiment
sentiments = { k: reduce(lambda sum, val: sum + float(val.get("sentiment")), v, 0.0) for k, v in collections.iteritems() }


# question 1
print("1. Which is the most positive Department in ENCS at Concordia?")
most_positive_tuple = lambda current_highest, current_tuple: current_highest if current_highest[1] > current_tuple[1] else current_tuple
postive = reduce(most_positive_tuple, [(k, v) for k, v in sentiments])
print(" A: The most positive department is " + positive[0])