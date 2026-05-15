from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": {"message": "Hello World!"}}


# parameterized path
@app.get("/blogs/{blog_id}")
def read_blog(blog_id: int):
    return {"data": {"blog_id": blog_id}}


@app.get("/blogs/{blog_id}/comments")
def read_blog_comments(blog_id: int):
    return {"data": {"blog_id": blog_id, "comments": ["comment1", "comment2"]}}

# bug when we have two paths with same prefix, 
# the first one will be executed and the second one will never be executed
# @app.get("/blogs/unpublished")
# def read_unpublished_blogs():
#     return {"data": {"blogs": ["blog1", "blog2"]}}


# query parameters
@app.get("/blogs/")
def read_blogs(limit: int = 10, published: bool = True):
    if published:
        return {"data": {"blogs": [f"blog {i}" for i in range(limit)]}}
    else:
        return {"data": {"blogs": [f"unpublished blog {i}" for i in range(limit)]}}