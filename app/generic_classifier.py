class GenericClassifier:

    def __init__(self, rules):
        self.rules = rules

    def classify(self, value):
        for k, v in self.rules.iteritems():
            if k(value):
                return v
