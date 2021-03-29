from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_alll(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def show(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        message = f'Blog with the id {id} is not available'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    return blog


def create(db: Session, request: schemas.BlogBase):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'blog delete'}


def update(db: Session, id: int, request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update(request)
    db.commit()
    return {'detail': 'blog updated'}
