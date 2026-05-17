from fastapi import Depends, FastAPI, status
from .schemas import BlogPost
from .database import engine
from . import models
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Session(bind=engine.connect())
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def root():
    return {"message": "Hello To Blog API"}

@app.post("/createpost" , status_code=status.HTTP_201_CREATED)
def create_post(request: BlogPost, db: Session = Depends(get_db)):
    blog = models.Blog(title=request.title, content=request.content)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return {"message": "Post created successfully", "post": blog}

@app.get("/getposts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Blog).all()
    return {"posts": posts}

@app.get("/getpost/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if post is None:
        return {"message": "Post not found"}
    return {"post": post}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)