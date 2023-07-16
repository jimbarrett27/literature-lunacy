from app_backend import app

@app.route('/hello_world')
def hello_world():
    return {'hello': 'world'}