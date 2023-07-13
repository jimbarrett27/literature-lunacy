import json
from pathlib import Path
from typing import Any, Dict, Generator

import pandas as pd
from tqdm import tqdm

from arxiv_lunacy.embeddings import embed_abstract
from util.constants import (INTERESTING_ARXIV_CATEGORIES, REPO_ROOT,
                            TORCH_DEVICE)

ARXIV_METADATA_SNAPSHOT_FILE =  REPO_ROOT / Path('data/arxiv-metadata-oai-snapshot.json')
OUTPUT_FILE = REPO_ROOT / Path('data/embeddings.feather')


def records_gen() -> Generator[Dict[str,Any], None, None]:
    """
    Generate the relevant records
    """
    with Path(ARXIV_METADATA_SNAPSHOT_FILE).open('r') as f:
        for line in f:
            record = json.loads(line)
            cats = set(record['categories'].split())
            if len(cats & INTERESTING_ARXIV_CATEGORIES) == 0:
                continue

            yield record

def get_number_of_records() -> int:
    """
    Count how many relevant records there are (for tqdm)
    """
    n_records=0
    for _ in records_gen():
        n_records+=1
    return n_records

def produce_embeddings_df() -> pd.DataFrame:
    """
    Produce a dataframe of embeddings
    """

    n_records = get_number_of_records()

    ids = []
    embeddings = []

    for record in tqdm(records_gen(), total=n_records):
        ids.append(record['id'])
        embeddings.append(embed_abstract(record['abstract']))

    embeddings_df = pd.DataFrame(embeddings)
    # feather doesn't like numerical column names
    embeddings_df = embeddings_df.rename(columns={i:f"dim{i}" for i in embeddings_df.columns})
    embeddings_df["id"] = ids

    return embeddings_df


if __name__ == "__main__":

    embeddings_df = produce_embeddings_df()
    embeddings_df.to_feather(OUTPUT_FILE)