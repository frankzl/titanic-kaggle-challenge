from sklearn.tree import DecisionTreeClassifier
from .classifier import Classifier

class DecisionTree (Classifier):

    def __init__(self, features, max_depth=None):
        self.features = features
        self.model = DecisionTreeClassifier(max_depth = max_depth)

    def train(self, data, labels):
        super().train(data, labels)
        self.model.fit( data [ self.features], labels )

    def predict(self, test_data):
        return (self.model.predict( test_data [ self.features ] ))


