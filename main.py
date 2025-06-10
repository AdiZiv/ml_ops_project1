import config
from config import FILE_PATH
from extract.extract_base import ExtractBase
from extract.extract_file import ExtractFile
from transform.transform_model import TransformModel
from transform.transform_processing import TransformProcessing
import pandas as pd

def main():

    # Extract
    extract : ExtractBase = ExtractFile(FILE_PATH)
    dataset = extract.load_data()
    print("get dataset")

    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)
    print("make transform")

    # predict
    model = TransformModel(config)
    result = model.predict(dataset_transform)
    print("run model prediction")

    # load
    #print(result)
    pd.DataFrame(result).to_csv(config.RESULT_FILE_PATH, index=False)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
