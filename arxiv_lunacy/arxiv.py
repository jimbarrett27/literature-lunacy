from dataclasses import dataclass
from typing import List
from urllib.parse import urlencode

@dataclass
class ArxivPaper:

    title: str
    authors: List[str]
    publish_date: str
    abstract: str

ARXIV_API_URL = "http://export.arxiv.org/api/query"

def query_arxiv_api(
        search_query: str = None,
        id_list: List[str] = None,
        start: int = None,
        max_results: int = None
):
    query_params = {}
    if search_query is not None:
        query_params['search_query'] = search_query
    if id_list is not None:
        query_params['id_list'] = ','.join(map(str,id_list))
    if start is not None:
        query_params['start'] = start
    if max_results is not None:
        query_params['max_results'] = max_results
            
    
    return f"{ARXIV_API_URL}?{urlencode(query_arxiv_api)}"

def get_arxiv_papers_for_ids(paper_ids: List[str]):
    pass
