from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import BlogPost, GetBlog
from ..database import get_db
from ..repo import blogs
from ..oauth2 import get_current_user

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=GetBlog)
def create_post(request: BlogPost, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return blogs.create(request, db)


@router.get("/", response_model=list[GetBlog])
def get_posts(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return blogs.get_all(db)


@router.get("/{id}", response_model=GetBlog)
def get_post(id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return blogs.get_by_id(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return blogs.delete(id, db)


@router.put("/{id}", response_model=GetBlog)
def update_post(id: int, request: BlogPost, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return blogs.update(id, request, db)
