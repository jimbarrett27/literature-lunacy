from app_backend import app
from flask import request

from arxiv_lunacy.embeddings import embed_abstract
from arxiv_lunacy.paper_similarity import get_closest_papers_to_embedding
from arxiv_lunacy.arxiv import fetch_arxiv_papers

@app.route('/get_closest_papers', methods=['POST'])
def get_closest_papers():

    if not request.method == "POST":
        return ""

    request_data = request.get_json()

    search_term = request_data['search_term']

    embedding = embed_abstract(search_term).squeeze()
    paper_ids = get_closest_papers_to_embedding(embedding)

    arxiv_papers = fetch_arxiv_papers(paper_ids)

    return [paper.to_dict() for paper in arxiv_papers]
