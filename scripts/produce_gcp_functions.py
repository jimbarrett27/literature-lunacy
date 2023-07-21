"""
Script that contains the code for GCP functions, as well
as the functionality to package the relevant code up into a zipfile
together with this file (renamed to main.py)
"""

import shutil
import tempfile as tmp
import zipfile
from pathlib import Path

import functions_framework
import pandas as pd

from arxiv_lunacy.embeddings import get_embeddings_df
from arxiv_lunacy.latest_papers import get_latest_embedding_df
from util.constants import EMBEDDINGS_DF_FILENAME, GCP_FUNCTION_ZIPFILE_NAME, REPO_ROOT
from util.storage import save_dataframe_to_blob, save_file_to_blob


@functions_framework.http
def update_embeddings_df(_):
    """
    GCP cloud function to update the embeddings
    """
    current_embeddings_df = get_embeddings_df()
    embedding_update_df = get_latest_embedding_df()

    all_embeddings_df = pd.concat([current_embeddings_df, embedding_update_df])
    all_embeddings_df = (
        all_embeddings_df.drop_duplicates(subset="id")
        .reset_index()
        .drop(columns="index")
    )
    save_dataframe_to_blob(all_embeddings_df, EMBEDDINGS_DF_FILENAME)

    return '{"status":"200", "data": "OK"}'


def create_and_upload_gcp_function_zipfile():
    """
    Function to upload all of the cloud functions to blob storage, so that we can
    deploy the cloud function
    """
    tmpdir = Path(tmp.mkdtemp())

    zipfile_path = tmpdir / GCP_FUNCTION_ZIPFILE_NAME

    zipped = zipfile.ZipFile(  # pylint: disable=consider-using-with
        zipfile_path, "w", zipfile.ZIP_DEFLATED
    )

    # upload the relevant code directories
    for directory in ["arxiv_lunacy", "util"]:
        for f in (REPO_ROOT / directory).iterdir():
            if not str(f).endswith(".py"):
                continue
            zipped.write(str(f), f"{directory}/{f.name}")

    zipped.write(REPO_ROOT / "requirements.txt", "requirements.txt")
    zipped.write(REPO_ROOT / "scripts/produce_gcp_functions.py", "main.py")
    zipped.close()

    save_file_to_blob(zipfile_path)
    shutil.rmtree(tmpdir)


if __name__ == "__main__":
    create_and_upload_gcp_function_zipfile()
