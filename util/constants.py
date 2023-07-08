from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

INTERESTING_ARXIV_CATEGORIES = set([
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
    "q-bio.QM"
])

EMBEDDINGS_FILENAME = 'embeddings.feather'