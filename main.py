from fastapi import FastAPI
from fastapi.params import Body  # Need this Library to extract the fields from the Body
from pydantic import BaseModel
from typing import List, Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Here if the user doesnt provide a value it will be True which is the default
    rating: Optional[int] = None # If the user hasn't provided a rating number the rating will be None

my_posts = [{"title" : "title of post 1",   # This is an array and this will help to save our post in memory before puting it in DB
             "content": "content of post 1",
             "id": 1},  # This ID will help us to fetch data 1 by 1 in case
             {"title" : "favorite pizzas",   # This is an array and this will save our post in memory before puting it in DB
             "content": "I like Pizza",
             "id": 2}]

def find_post(id):
    for p in my_posts:  # p is an imaginary variable
        if p["id"] == id: # p refers to each dictionary. so in each dict if the id which the user puts in postman equals to id in dict
             return p

#request GET method url "/" and FASTAPI makes sure that the first path operator will be used.

@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}

@app.get("/posts")
def get_post():
    return {"data": my_posts }

@app.post("/createposts")
def create_posts(payLoad: dict = Body(... )): # What this will do is it will extract all of the fields from the body
                                            # and basically convert into a python dictionary and its gonna store in a variable called payLoad
    print(payLoad)
    return {"posts": f"title {payLoad['title']} content: {payLoad['content']}"} # f string is an effective way to use strings in here we can do things which we cannot do with a normal string.

# pydantic is used for schema validation of the POST request. (making sure the user POSTS the correct info)
# title str, content str (This is all what we need)
# look into pydantic.com documentation.

# @app.post("/posts")
# def create_posts(posts: Post): # Here the posts is just a varible name and Post is the class name which we used earlier for pydantic 
#     posts_dict = posts.model_dump()
#     posts_dict['id'] = randrange(0, 100000000)
#     my_posts.append(posts.model_dump()) # When the Post is getting created through postman that data will be stored in myposts array as a Dictionary.
#     return {"data": posts } # This is just the return message. We are sending back the posts dictionsry. 

@app.post("/posts")
def create_posts(posts: Post): # Here the posts is just a varible name and Post is the class name which we used earlier for pydantic 
    posts_dict = posts.model_dump()
    posts_dict['id'] = randrange(0, 100000000) # gi ving the newly added post a random id number.
    my_posts.append(posts_dict)
    return {"data": my_posts } # This is just the return message. We are sending back the my_posts dictionsry. 

@app.get("/posts/{id}")
def get_post(id: int): # making sure that the id is an integer which the user will put in postman.
    post = find_post(id)
    return {"post_details": post}
# In the above example i ran into a issue where the id number is looking for a number but the ouput 
# seems to be giving a string in this case i used print to to see the exact output i get and if there's 
# anything wrong with the output i can modify the code accordingly and in this case i was able to
# modify the string output to an integer to get the correct post.

@app.put("/posts/{id}")
def update_posts(posts)

