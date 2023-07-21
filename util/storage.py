import shutil
from pathlib import Path

import pandas as pd
from google.cloud import storage

from util.constants import GCP_BUCKET_NAME


def get_blob_stored_dataframe(blob_name: str):
    """
    Retrieves and deserialises a blob stored at blob_name
    """
    df = pd.read_feather(f"gs://{GCP_BUCKET_NAME}/{blob_name}")

    return df


def save_dataframe_to_blob(df: pd.DataFrame, blob_name: str) -> bool:
    """
    Appends the "update dict" to the json list stored at blob_name
    """

    df.to_feather(f"gs://{GCP_BUCKET_NAME}/{blob_name}")

    return False


def save_file_to_blob(filepath: Path):
    client = storage.Client()

    bucket = client.bucket(GCP_BUCKET_NAME)
    blob = bucket.blob(filepath.name)

    with filepath.open("rb") as f:
        blob.upload_from_file(f)
