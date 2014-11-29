from generic_classifier import GenericClassifier
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
import math

class Classifier:

  def __init__ (self, documents):

    # add all sentiments to a single array
    sentiments = []
    for doc in documents:
      sentiment_float = float(doc.get("sentiment"))
      sentiment_vector = [sentiment_float]
      sentiments.append(sentiment_vector)

    # compute centroids
    features = array(sentiments)
    centroids = kmeans(features, 3)[0]
    self.centroids = sorted(centroids)



  def classify (self, sentiment):

    # check the closes centroid
    distances = map(lambda x: math.fabs(x - sentiment), self.centroids)
    closest_centroid = min((v, i) for i, v in enumerate(distances))
    if closest_centroid[1] == 0:
      return ("negative", -1)
    elif closest_centroid[1] == 1:
      return ("neutral", 0)
    else:
      return ("positive", 1)