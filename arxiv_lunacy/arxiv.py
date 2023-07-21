"""
Utilities for working with preprints from arxiv and the arxiv site and feeds
"""

from dataclasses import dataclass
from typing import Optional
from urllib.parse import urlencode

import feedparser # type: ignore
from html2text import html2text


@dataclass
class ArxivPaper:
    """
    Dataclass representing an arxiv preprint
    """

    title: str
    authors: list[str]
    publish_date: str
    abstract: str

    def to_dict(self) -> dict[str, str]:
        """
        Represents a paper as a dict, formatted as the frontend expects
        """
        return {
            "title": self.title,
            "authorList": ", ".join(self.authors),
            "publicationDate": self.publish_date,
            "abstract": self.abstract,
        }


ARXIV_API_URL = "http://export.arxiv.org/api/query"


def get_formatted_arxiv_api_url(
    search_query: Optional[str] = None,
    id_list: Optional[list[str]] = None,
    start: Optional[int] = None,
    max_results: Optional[int] = None,
) -> str:
    """
    Returns the URL for the arxiv API with correclty formatted query parameters
    """
    query_params: dict[str, str | int] = {}
    if search_query is not None:
        query_params["search_query"] = search_query
    if id_list is not None:
        query_params["id_list"] = ",".join(map(str, id_list))
    if start is not None:
        query_params["start"] = start
    if max_results is not None:
        query_params["max_results"] = max_results

    return f"{ARXIV_API_URL}?{urlencode(query_params)}"


def get_arxiv_rss_url(arxiv_category: str):
    """
    Gets the rss url for the given arxiv category
    """
    return f"http://export.arxiv.org/rss/{arxiv_category}"


def fetch_arxiv_papers(id_list: list[str]) -> list[ArxivPaper]:
    """
    Given a list of arxiv ids, fetch the details of the papers from the arxiv API
    """
    url = get_formatted_arxiv_api_url(id_list=id_list)

    paper_details = feedparser.parse(url)["entries"]

    arxiv_papers = [
        ArxivPaper(
            title=paper["title"],
            abstract=html2text(paper["summary"]),
            publish_date=paper["published"],
            authors=[author["name"] for author in paper["authors"]],
        )
        for paper in paper_details
    ]

    return arxiv_papers
