

from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

from starlette.status import HTTP_404_NOT_FOUND

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional



from random import randrange


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


    published: bool = True
    rating: Optional[int] = None
    

my_posts = [{"title": "title of post 1", "content": "contentof post 1", "id": 1}, {"title": "title of post 2", "content": "contentof post 2", "id": 2}]    

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i



    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "contentof post 1", "id": 1}, {"title": "title of post 2", "content": "contentof post 2", "id": 2}]    

@app.get("/")
def get_user():
    return {"message": "Welcome to my API. New Change!!!"}



@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    print(post)
    print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found!")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'messahe': f"post with id: {id} was not found!"}
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int, status_code=status.HTTP_204_NO_CONTENT):
    # deletes posts
    #find index for the requires id
    #my_posts.pop
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exists")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} does not exists")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    
    print(post)
    return {"data": post_dict}

@app.get("/post")

@app.get("/posts")

def get_posts():
    return {"data": my_posts}

@app.post("/createpost")
def create_posts(post: Post):
    print(post)
    print(post.dict())

    return {"data": "new_post"}

# title str, content str,




    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id): 

