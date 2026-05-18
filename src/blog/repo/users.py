from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..schemas import UserCreate
from ..hassing import Hash


def create(request: UserCreate, db: Session):
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all(db: Session):
    return db.query(models.User).all()


def get_by_id(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
