from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import Login, Token
from ..database import get_db
from ..repo import auth

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(request: Login, db: Session = Depends(get_db)):
    return auth.login(request.username, request.password, db)
