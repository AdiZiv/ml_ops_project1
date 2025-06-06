import pickle
from sklearn.ensemble import RandomForestClassifier


class TransformModel():
    def __init__(self, config):
        self.config = config
        self.__load_dependency()

    def __validation(self, dataset):
        pass

    def __load_dependency(self):
        with open(self.config.MODEL_PATH, 'rb') as f:
            self.model: RandomForestClassifier = pickle.load(f)

    def predict(self, dataset):
        self.__validation(dataset)
        result = self.model.predict(dataset)
        return result
