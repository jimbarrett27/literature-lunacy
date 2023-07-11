import pandas as pd

from util.constants import GCP_BUCKET_NAME

def get_blob_stored_dataframe(blob_name: str):
    """
    Retrieves and deserialises a blob stored at blob_name
    """
    df = pd.read_feather(f'gs://{GCP_BUCKET_NAME}/{blob_name}')

    return df


def save_dataframe_to_blob(
    df: pd.DataFrame, blob_name: str
) -> bool:
    """
    Appends the "update dict" to the json list stored at blob_name
    """

    df.to_feather(f'gs://{GCP_BUCKET_NAME}/{blob_name}')

    return False