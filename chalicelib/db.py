import boto3
import pandas as pd

class OptionsDB(object):
    def __init__(self, object_name) -> None:
        self._s3_client = boto3.client('s3')
        self._s3_object = self._s3_client.get_object(Bucket='cb-colombia', Key=object_name)

    def read_csv_from_s3(self):
        df_s3_data = pd.read_csv(self._s3_object['Body'], sep=',')
        return df_s3_data
