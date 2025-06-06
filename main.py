import config
from config import FILE_PATH
from extract.extract_base import ExtractBase
from extract.extract_file import ExtractFile
from transform.transform_model import TransformModel
from transform.transform_processing import TransformProcessing

def main():

    # Extract
    extract : ExtractBase = ExtractFile(FILE_PATH)
    dataset = extract.load_data()

    print(dataset)
    # transform
    transform = TransformProcessing(config)
    dataset_transform = transform.transform(dataset)

    # predict
    model = TransformModel(config)
    result = model.transform(dataset_transform)

    # load
    print(result)
    result.to_csv(config['RESULT_FILE_PATH'])


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
