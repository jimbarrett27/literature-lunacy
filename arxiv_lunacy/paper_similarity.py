import numpy as np

from arxiv_lunacy.embeddings import get_embeddings_df, get_paper_id_to_index


def cosine_similarity(all_embeddings,embeddings_to_compare):
    
    numerators = np.dot(all_embeddings, embeddings_to_compare)
    denominators = (np.linalg.norm(all_embeddings)*np.linalg.norm(embeddings_to_compare))

    return numerators / denominators

def get_paper_id_to_index(embeddings_df):
    return {paper_id: ind for paper_id, ind in zip(embeddings_df.id, embeddings_df.index)}

def get_closest_papers(paper_ids, top_n = 10):
    
    embeddings_df = get_embeddings_df()
    id_to_index = get_paper_id_to_index(embeddings_df)
    paper_inds = [id_to_index[paper_id] for paper_id in paper_ids]
    
    ids = embeddings_df.id.to_numpy()
    embeddings_df = embeddings_df.drop(columns="id")
    paper_embeddings = embeddings_df.loc[paper_inds].to_numpy()
    other_embeddings = embeddings_df.to_numpy()
    
    cosine_sims = cosine_similarity(other_embeddings, paper_embeddings.T)
    
    top_n_inds = np.argpartition(cosine_sims, -top_n, axis=0)[-top_n:]
    
    return ids[top_n_inds]