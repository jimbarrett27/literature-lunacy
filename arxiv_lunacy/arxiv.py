from dataclasses import dataclass
from typing import List, Dict, Any
from urllib.parse import urlencode
import feedparser
from html2text import html2text

@dataclass
class ArxivPaper:

    title: str
    authors: List[str]
    publish_date: str
    abstract: str

    def to_dict(self) -> Dict[str, Any]:

        return {
            "title": self.title,
            "authorList": ", ".join(self.authors),
            "publicationDate": self.publish_date,
            "abstract": self.abstract
        }


ARXIV_API_URL = "http://export.arxiv.org/api/query"

def get_formatted_arxiv_api_url(
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
            
    return f"{ARXIV_API_URL}?{urlencode(query_params)}"

def fetch_arxiv_papers(id_list: List[str]) -> List[ArxivPaper]:

    url = get_formatted_arxiv_api_url(id_list=id_list)

    paper_details = feedparser.parse(url)['entries']

    arxiv_papers = [
        ArxivPaper(
        title=paper['title'],
        abstract=html2text(paper['summary']),
        publish_date=paper['published'],
        authors=[author['name'] for author in paper['authors']]
        )
        for paper in paper_details
    ]

    return arxiv_papers
