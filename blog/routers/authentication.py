from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash
from datetime import timedelta


router = APIRouter(
    tags=['Authentication']
)

get_db = database.get_db


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if  not user:
        message = f'Invalid credentials for {request.username}'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    if not Hash.verify(user.password, request.password):
        message = 'Incorrect password'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}