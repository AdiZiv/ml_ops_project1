import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


class TransformProcessing():
    def __init__(self,config):
        self.config = config

    def __validation(self,dataset):
        pass

    def transform(self, dataset):
        self.__validation(dataset)

        # Fillna
        dataset['TotalCharges'] = dataset['TotalCharges'].fillna(self.config.FILLNA_TOTALCHARGES)
        dataset['TotalCharges'] = dataset['TotalCharges'].str.replace(' ',self.config.FILLNA_TOTALCHARGES_STR) # remove space string in data
        dataset['TotalCharges'] = dataset['TotalCharges'].astype(float)

        dataset['Contract'] = dataset['Contract'].dropna()

        dataset['PhoneService'].fillna(self.config.FILLNA_PhoneService)

        dataset['tenure'] = dataset['tenure'].astype(float)

        # Feature handeling:
        dataset['PhoneService'] = dataset['PhoneService'].map({'Yes':1,'No':0})

        dataset = dataset.join(pd.get_dummies(dataset['Contract']).astype(int))
        
        return dataset[self.config.MODEL_COLUMNS]