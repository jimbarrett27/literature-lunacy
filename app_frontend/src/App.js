import { useState } from 'react';

function SearchField({ setPapersInView }) {

  const fetchPapersForSearchTerm = async () => {
    let searchBox = document.getElementById("searchBox");
    let searchTerm = searchBox.value;

    let postBody = {
      "search_term": searchTerm
    }

    fetch(
      "/get_closest_papers",
      {
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(postBody)
      }
    )
    .then( (resp) => {
      console.log(resp)
      return resp.json()
    })
    .then((papers) => {
      setPapersInView(papers)
    })

  }

  return (
    <>
    <input id="searchBox" type="text" />
    <button onClick={fetchPapersForSearchTerm} >Search</button>
    </>
  )
}

function PaperSummaries( { papers } ) {

  if (papers.length === 0) return <></>

  return papers.map(paper => {
    return (<>
    <PaperSummary paper={paper} />
    <br></br>
    </>)
  })
}

function PaperSummary({ paper }) {
  return (
    <>
    <h2>{paper.title}</h2>
    <h3><i>{paper.publicationDate}</i> - {paper.authorList}</h3>
    <p>{paper.abstract}</p>
    </>
  )
}

export default function MyApp() {

  const [papersInView, setPapersInView] = useState([]);

  return (
    <div>
      <h1>Preprint Sanity</h1>
      <SearchField setPapersInView={setPapersInView} />
      <PaperSummaries papers={papersInView} />
    </div>
  );
}