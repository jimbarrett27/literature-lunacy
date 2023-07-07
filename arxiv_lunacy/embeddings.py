from functools import lru_cache
from util.constants import EMBEDDINGS_FILENAME, REPO_ROOT
import pandas as pd


@lru_cache
def get_embeddings_df():
    return pd.read_feather(REPO_ROOT / f'data/{EMBEDDINGS_FILENAME}')

def get_paper_id_to_index(embeddings_df):
    return {paper_id: ind for paper_id, ind in zip(embeddings_df.id, embeddings_df.index)}

