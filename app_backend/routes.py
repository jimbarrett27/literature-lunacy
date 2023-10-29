"""
The backend API
"""

from flask import request

from app_backend import app
from arxiv_lunacy.arxiv import fetch_arxiv_papers
from arxiv_lunacy.embeddings import embed_abstract
from arxiv_lunacy.paper_similarity import get_closest_papers_to_embedding
import json


@app.route("/get_closest_papers_to_search_term", methods=["POST"])
def get_closest_papers_to_search_term():
    """
    Endpoint to fetch the closest papers to a search term
    """
    if not request.method == "POST":
        return ""

    request_data = request.get_json()

    search_term = request_data["search_term"]

    embedding = embed_abstract(search_term).squeeze()
    paper_ids = get_closest_papers_to_embedding(embedding)

    arxiv_papers = fetch_arxiv_papers(paper_ids)

    return json.dumps([paper.to_dict() for paper in arxiv_papers])
