from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Albert Dev'}}


@app.get('/about')
def about():
    return {'data': {'name': 'about page'}}
    