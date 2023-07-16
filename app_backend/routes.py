from app_backend import app
import numpy as np

@app.route('/random_dummy_paper')
def random_dummy_paper():

    papers = [
        {
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
        },
        {
            "title": "Yet another title",
            "authorList": "c et al",
            "publicationDate": "3rd February 2016",
            "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  "
        },
        {
            "title": "Such title, much paper",
            "authorList": "D et al",
            "publicationDate": "15th October 1955",
            "abstract": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.  "
        }
    ]

    return np.random.choice(papers, size=2)