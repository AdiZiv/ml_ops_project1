import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler


class TransformProcessing():
    def __init__(self,config):
        self.config = config
        self.__load_dependency()

    def __validation(self,dataset):
        pass

    def __load_dependency(self):
        with open(self.config.SCALE_ENCODDER_PATH, 'rb') as f:
            self.scalar = pickle.load(f)

        with open(self.config.LABEL_ENCODDER_PATH, 'rb') as f:
            self.labelencoder_array = pickle.load(f)

            self.labelencoder_sex = self.labelencoder_array[self.config.SEX_ENCODER]
            self.labelencoder_embarked = self.labelencoder_array[self.config.EMBARKED_ENCODER]
            self.labelencoder_cabin = self.labelencoder_array[self.config.CABIN_ENCODER]

    def transform(self, dataset):
        self.__validation(dataset)

        dataset['Sex'] = self.labelencoder_sex.transform(dataset['Sex'])
        dataset['Embarked'] = self.labelencoder_embarked.transform(dataset['Embarked'].astype(str))
        dataset['Cabin'] = self.labelencoder_cabin.transform(dataset['Cabin'].astype(str))

        dataset['Age'].fillna(self.config.FILLNA_AGE, inplace=True)
        dataset['Embarked'].fillna(self.config.FILLNA_EMBARKED, inplace=True)

        numerical_columns = self.config.NUMERICAL_COLUMNS
        dataset[numerical_columns] = self.scalar.transform(dataset[numerical_columns])

        return dataset[self.config.MODEL_COLUMNS]