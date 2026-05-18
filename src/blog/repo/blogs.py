from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..schemas import BlogPost


def create(request: BlogPost, db: Session):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    blog = models.Blog(title=request.title, content=request.content, user_id=request.user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_all(db: Session):
    return db.query(models.Blog).all()


def get_by_id(id: int, db: Session):
    post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post


def delete(id: int, db: Session):
    post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(post)
    db.commit()


def update(id: int, request: BlogPost, db: Session):
    post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post.title = request.title
    post.content = request.content
    db.commit()
    db.refresh(post)
    return post
