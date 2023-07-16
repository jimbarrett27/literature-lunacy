
const PAPERS = [{
  "title": "A title",
  "authorList": "A et al",
  "publicationDate": "17th July 1991",
  "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  "
},
{
  "title": "Another title",
  "authorList": "B et al",
  "publicationDate": "8th December 2020",
  "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  "
}
]

function SearchField() {

  return (
    <>
    <input id="searchBox" type="text" />
    <button>Search</button>
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
  return (
    <div>
      <h1>Preprint Sanity</h1>
      <SearchField />
      <PaperSummaries papers={PAPERS} />
    </div>
  );
}