"""
Various constants used throughout the repo
"""

from pathlib import Path

import torch

REPO_ROOT = Path(__file__).parent.parent

INTERESTING_ARXIV_CATEGORIES = set(
    [
        "cs.AI",
        "cs.CE",
        "cs.CL",
        "cs.LG",
        "stat.AP",
        "stat.CO",
        "stat.ME",
        "stat.ML",
        "stat.TH",
        "math.ST",
        "q-bio.QM",
    ]
)

EMBEDDINGS_DF_FILENAME = "embeddings.feather"

GCP_BUCKET_NAME = "arxiv_lunacy"

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

TORCH_DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu") # pylint: disable=no-member

GCP_FUNCTION_ZIPFILE_NAME = "gcp_functions.zip"
