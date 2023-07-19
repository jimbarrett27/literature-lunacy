from functools import lru_cache
from logging import getLogger

import numpy as np
from sentence_transformers import SentenceTransformer

from util.constants import (EMBEDDING_MODEL_NAME, EMBEDDINGS_DF_FILENAME,
                            REPO_ROOT, TORCH_DEVICE)
from util.storage import get_blob_stored_dataframe
import pandas as pd

import os

LOGGER = getLogger(__name__)

@lru_cache
def get_embeddings_df():

    if os.environ.get('RUNNING_IN_CLOUD') is not None:
        return get_blob_stored_dataframe(EMBEDDINGS_DF_FILENAME)
        

    local_path = REPO_ROOT / f'data/{EMBEDDINGS_DF_FILENAME}'
    if local_path.exists():
        return pd.read_feather(local_path)


    embeddings_df = get_blob_stored_dataframe(EMBEDDINGS_DF_FILENAME)
    embeddings_df.to_feather(local_path)
    return embeddings_df

def get_paper_id_to_index(embeddings_df):
    return {paper_id: ind for paper_id, ind in zip(embeddings_df.id, embeddings_df.index)}

@lru_cache
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

def embed_abstract(abstract: str) -> np.ndarray:

    model = get_embedding_model()

    return np.array(model.encode([abstract], device=TORCH_DEVICE))

