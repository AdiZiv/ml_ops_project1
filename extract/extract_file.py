import pandas as pd
from extract.extract_base import ExtractBase


class ExtractFile(ExtractBase):

    def __init__(self,file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_csv(self.file_path)