from app_backend import app
from flask import request

from arxiv_lunacy.embeddings import embed_abstract
from arxiv_lunacy.paper_similarity import get_closest_papers_to_embedding

@app.route('/get_closest_papers', methods=['POST'])
def get_closest_papers():

    if not request.method == "POST":
        return ""

    request_data = request.get_json()

    search_term = request_data['search_term']

    embedding = embed_abstract(search_term).squeeze()
    paper_ids = get_closest_papers_to_embedding(embedding)

    dummy_papers = [{
            "title": paper_id,
            "authorList": "A et al",
            "publicationDate": "17th July 1991",
            "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  "
    } for paper_id in paper_ids]

    return dummy_papers
