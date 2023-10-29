import React from 'react';
import './App.css';
import { useState } from 'react';


type Paper = {
  title: string,
  publicationDate: string,
  authorList: string,
  abstract: string

}

function SearchField({setPapersInView}: {setPapersInView : (papers: Paper[]) => void}) {
  
  const fetchPapersForSearchTerm = async () => {
    const searchBox = document.getElementById('searchBox');

    let searchTerm = '';
    if (searchBox) {
      searchTerm = searchBox.innerText;
    }

    const postBody = {
      'search_term': searchTerm,
    };

    console.log(postBody);

    fetch(
        '/get_closest_papers_to_search_term',
        {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(postBody),
        },
    )
        .then( (resp) => {
          return resp.json();
        })
        .then((papers) => {
          setPapersInView(papers);
        });
  };

  return (
    <>
      <input id="searchBox" type="text" />
      <button onClick={fetchPapersForSearchTerm} >Search</button>
    </>
  );
}

function PaperSummaries( {papers}: {papers: Paper[]} ) {
  if (papers.length === 0) return <></>;

  return <>{papers.map((paper: Paper) => {
    return (<>
      <PaperSummary paper={paper} />
      <br></br>
    </>);
  })}</>;
}

function PaperSummary({paper}: {paper: Paper}) {
  return (
    <>
      <h2>{paper.title}</h2>
      <h3><i>{paper.publicationDate}</i> - {paper.authorList}</h3>
      <p>{paper.abstract}</p>
    </>
  );
}

export default function MyApp() {
  const [papersInView, setPapersInView] = useState<Paper[]>([]);

  return (
    <div>
      <h1>Preprint Sanity</h1>
      <SearchField setPapersInView={setPapersInView} />
      <PaperSummaries papers={papersInView} />
    </div>
  );
}

