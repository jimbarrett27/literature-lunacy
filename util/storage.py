import json
import io
import pandas as pd

from google.cloud import storage
from util.constants import GCP_BUCKET_NAME

def get_blob_stored_dataframe(blob_name: str, client: storage.Client = None):
    """
    Retrieves and deserialises a blob stored at blob_name
    """

    if client is None:
        client = storage.Client()

    bucket = client.bucket(GCP_BUCKET_NAME)
    blob = bucket.get_blob(blob_name)
    with io.BytesIO(blob.download_as_bytes()) as f:
        df = pd.read_feather(f)

    return df


def save_dataframe_to_blob(
    df: pd.DataFrame, blob_name: str, client: storage.Client = None
) -> bool:
    """
    Appends the "update dict" to the json list stored at blob_name
    """

    if client is None:
        client = storage.Client()


    df.to_feather(f'gs://{GCP_BUCKET_NAME}/{blob_name}')

    return False