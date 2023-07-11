from functools import lru_cache
from util.constants import EMBEDDINGS_FILENAME, REPO_ROOT, EMBEDDING_MODEL_NAME, TORCH_DEVICE
import pandas as pd
from sentence_transformers import SentenceTransformer
from util.storage import get_blob_stored_dataframe, save_dataframe_to_blob

from logging import getLogger

LOGGER = getLogger(__name__)

@lru_cache
def get_embeddings_df():

    local_path = REPO_ROOT / f'data/{EMBEDDINGS_FILENAME}'
    if local_path.exists():
        return pd.read_feather(local_path)


    embeddings_df = get_blob_stored_dataframe(EMBEDDINGS_FILENAME)
    embeddings_df.to_feather(local_path)
    return embeddings_df

def get_paper_id_to_index(embeddings_df):
    return {paper_id: ind for paper_id, ind in zip(embeddings_df.id, embeddings_df.index)}

@lru_cache
def get_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

def embed_abstract(abstract: str):

    model = get_embedding_model()

    return model.encode([abstract], device=TORCH_DEVICE)

