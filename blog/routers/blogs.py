from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, oauth
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs'],
    dependencies=[Depends(oauth.get_current_user)]
)

get_db = database.get_db
get_current_user = oauth.get_current_user


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db)):
    return blog.get_alll(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session=Depends(get_db)):
    return blog.show(db, id)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BlogBase, db: Session=Depends(get_db)):
    return blog.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session=Depends(get_db)):
    return blog.destroy(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session=Depends(get_db)):
    return blog.update(db, id, request)

