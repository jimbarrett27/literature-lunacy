# arxiv-lunacy

New pet project, started July 2023

This is my attempt to recreate the golden days of [arxiv sanity](https://arxiv-sanity-lite.com/), to allow me to better keep up to date with preprints and find those relevant to my work.

# Running the app

In order to run the app, you need to launch both the frontend and the backend.

### Frontend

The frontend is written in the React framework for JavaScript. In order to ruin it, first navigate to the `app_frontend` folder, install the dependencies, and then launch the frontend server, like so;

```bash
cd app_frontend
npm init
npm start
```

### Backend

The backend is written in Python+Flask. Assuming you already have conda as a package manager, you can install the requirements like so (from the root of the repo);

```bash
conda env create -f environment.yml
conda activate arxiv-lunacy
pip install -r requirements.txt
```

You can then launch the server by (again from the root of the repo);

```bash
gunicorn app_backend:app
```

# Development

You can get yourself setup for development of this repo in the way you would expect. Assuming you have conda already setup;



And then follow the instructions for installing pytorch based on your configuration [here](https://pytorch.org/get-started/locally/)