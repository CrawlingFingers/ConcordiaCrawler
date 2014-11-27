from classify import Classify

def get_sentiment_classifier ():
    return Classify({(lambda x: (x > 0.2)): ("positive", 1),
    (lambda x: (x < -0.2)): ("negative", -1),
    (lambda x: (x >= -0.2 and x <= 0.2)): ("neutral", 0)
    })

