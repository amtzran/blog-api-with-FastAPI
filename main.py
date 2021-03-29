from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blogs from the db. published: {published}'}
    else: 
        return {'data': f'{limit} blogs from the db.'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with {blog.title}'}
    