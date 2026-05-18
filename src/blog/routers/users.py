from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import UserCreate, GetUser
from ..database import get_db
from ..repo import users
from ..oauth2 import get_current_user

router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GetUser)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return users.create(request, db)


@router.get("/", response_model=list[GetUser])
def get_users(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return users.get_all(db)


@router.get("/{id}", response_model=GetUser)
def get_user(id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return users.get_by_id(id, db)
