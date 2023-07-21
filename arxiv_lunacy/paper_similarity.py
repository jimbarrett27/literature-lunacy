"""
Utilities for comparing papers based on their embeddings
"""

import numpy as np

from arxiv_lunacy.embeddings import get_embeddings_df


def cosine_similarity(
    all_embeddings: np.ndarray, embeddings_to_compare: np.ndarray
) -> np.ndarray:
    """
    Ćomputes the cosine similarity between two sets of vectors

    all_embeddings: matrix of shape n_vectors_all X embedding_size
    embeddings_to_compare: matrix of shape n_vectors_to_compare X embedding size

    result: matrix of shape n_vectors_all X n_vectors_compare
    where i,jth component is the similarity between vector_all_i and vector_compare_j
    """
    numerators = np.dot(all_embeddings, embeddings_to_compare.T)
    denominators = np.linalg.norm(all_embeddings) * np.linalg.norm(
        embeddings_to_compare
    )

    return numerators / denominators


def get_closest_papers(paper_ids: list[str], top_n: int = 10):
    """
    Gets the top_n most similar papers to those with the given ids
    """
    embeddings_df = get_embeddings_df()
    id_to_index = dict(zip(embeddings_df.id, embeddings_df.index))
    paper_inds = [id_to_index[paper_id] for paper_id in paper_ids]

    all_paper_ids = embeddings_df.id.to_numpy()
    embeddings_df = embeddings_df.drop(columns="id")
    embeddings_to_compare = embeddings_df.loc[paper_inds].to_numpy()
    all_paper_embeddings = embeddings_df.to_numpy()

    cosine_sims = cosine_similarity(all_paper_embeddings, embeddings_to_compare)

    top_n_inds = np.argpartition(cosine_sims, -top_n, axis=0)[-top_n:]

    return all_paper_ids[top_n_inds]


def get_closest_papers_to_embedding(embedding: np.ndarray, top_n: int = 10):
    """
    Given a text embedding, fetch the closest top_n most similar papers
    """
    embeddings_df = get_embeddings_df()

    all_paper_ids = embeddings_df.id.to_numpy()
    embeddings_df = embeddings_df.drop(columns="id")
    all_paper_embeddings = embeddings_df.to_numpy()

    cosine_sims = cosine_similarity(all_paper_embeddings, embedding)

    top_n_inds = np.argpartition(cosine_sims, -top_n, axis=0)[-top_n:]

    return all_paper_ids[top_n_inds]
