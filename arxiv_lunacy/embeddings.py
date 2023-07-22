"""
Utilities for working with text embeddings
"""

import os
from functools import lru_cache
from logging import getLogger

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer  # type: ignore

from util.constants import (
    EMBEDDING_MODEL_NAME,
    EMBEDDINGS_DF_FILENAME,
    REPO_ROOT,
    TORCH_DEVICE,
)
from util.storage import get_blob_stored_dataframe

LOGGER = getLogger(__name__)


@lru_cache
def get_embeddings_df():
    """
    Fetches the dataframe of all the embeddings
    """
    if os.environ.get("RUNNING_IN_CLOUD") is not None:
        return get_blob_stored_dataframe(EMBEDDINGS_DF_FILENAME)

    local_path = REPO_ROOT / f"data/{EMBEDDINGS_DF_FILENAME}"
    if local_path.exists():
        return pd.read_feather(local_path)

    embeddings_df = get_blob_stored_dataframe(EMBEDDINGS_DF_FILENAME)
    embeddings_df.to_feather(local_path)
    return embeddings_df


@lru_cache
def get_embedding_model():
    """
    Gets the model used for embedding the abstracts
    """
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def embed_abstract(abstract: str) -> np.ndarray:
    """
    Embeds the abstract into a fixed length vector
    """
    model = get_embedding_model()

    return np.array(model.encode([abstract], device=TORCH_DEVICE))
