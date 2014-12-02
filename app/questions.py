from retrieve import Retriever
from classifier import Classifier
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
all_docs = reduce((lambda x, y: x + y), [v for k,v in collections.iteritems()], [])
all_sentiments = [float(doc.get("sentiment")) for doc in all_docs]
classifier = Classifier(all_sentiments)

reduce_lambda = lambda sum, val: sum + (classifier.classify(float(val.get("sentiment")))[1])
sentiments_t = { k: reduce(reduce_lambda, v, 0.0) for k, v in collections.iteritems() }

sentiments = {k: v/len(collections[k]) for k, v in sentiments_t.iteritems() }

# intro printer
print("")
print("COMP479 Final Project")
print(" by ")
print("Connor Bode, Greg Houle, Michael bla")
print("")

# question 1
print("Q1. Which is the most positive Department in ENCS at Concordia?")
most_positive_tuple = lambda current_highest, current_tuple: current_highest if current_highest[1] > current_tuple[1] else current_tuple
positive = reduce(most_positive_tuple, [(k, v) for k, v in sentiments.iteritems()])
print("A:  The most positive department is " + positive[0])
print("")

# question 2
print("Q2. Is Computer Science and Software Engineering more positive or less positive than Electrical and Computer Engineering?")
if sentiments['computer-science-software-engineering'] > sentiments['electrical-computer']:
  print("A:  Computer Science and Software Engineering is more positive than Electrical and Computer Engineering")
else:
  print("A:  Computer Science and Software Engineering is less positive than Electrical and Computer Engineering")
print("")

# question 3
print("Q3. Rank the departments in ENCS by sentiment of their web documents")
print("A:")
ordered_sentiments = sorted(sentiments.items(), key=lambda x: x[1], reverse=True)
for i, s in enumerate(ordered_sentiments):
  print(str(i) + "       " + s[0] + "    " + str(s[1]))
print("")

# question 4
print("Q4. Classify the departments in ENCS with a three way classifier into positive, negative, and neutral")
dept_sentiments = [v for k, v in ordered_sentiments]
dept_classifier = Classifier(dept_sentiments)
print("A:")
for i, s in enumerate(ordered_sentiments):
  print(str(i) + "       " + s[0] + "    " + dept_classifier.classify(s[1])[0])
print("")
print("Original centroids: ")
for centroid in classifier.centroids:
  print(centroid)
print("")
print("Department centroids: ")
for centroid in dept_classifier.centroids:
  print(centroid)



# finally
print("")
print("Bye! :)")
print("")