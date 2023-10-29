import './App.css'
import React, { useState } from 'react'

interface Paper {
  title: string
  publicationDate: string
  authorList: string
  abstract: string

}

function SearchField ({ setPapersInView }: { setPapersInView: (papers: Paper[]) => void }): React.ReactElement {
  // const fetchPapersForSearchTerm = async (): Promise<void> => {
  const fetchPapersForSearchTerm = (): void => {
    const searchBox = document.getElementById('searchBox')

    let searchTerm = ''
    if (searchBox !== null) {
      searchTerm = searchBox.innerText
    }

    const postBody = {
      search_term: searchTerm
    }

    fetch(
      '/get_closest_papers_to_search_term',
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postBody)
      }
    )
      .then(async (resp) => {
        return await resp.json()
      })

      .then((papers) => {
        setPapersInView(papers)
      }, (reason) => {
        console.error(reason)
        setPapersInView([])
      })
  }

  return (
    <>
      <input id="searchBox" type="text" />
      <button onClick={fetchPapersForSearchTerm} >Search</button>
    </>
  )
}

function PaperSummaries ({ papers }: { papers: Paper[] }): React.ReactElement {
  if (papers.length === 0) return <></>

  return <>{papers.map((paper: Paper) => {
    return (<>
      <PaperSummary paper={paper} />
      <br></br>
    </>)
  })}</>
}

function PaperSummary ({ paper }: { paper: Paper }): React.ReactElement {
  return (
    <>
      <h2>{paper.title}</h2>
      <h3><i>{paper.publicationDate}</i> - {paper.authorList}</h3>
      <p>{paper.abstract}</p>
    </>
  )
}

export default function MyApp (): React.ReactElement {
  const [papersInView, setPapersInView] = useState<Paper[]>([])

  return (
    <div>
      <h1>Preprint Sanity</h1>
      <SearchField setPapersInView={setPapersInView} />
      <PaperSummaries papers={papersInView} />
    </div>
  )
}
