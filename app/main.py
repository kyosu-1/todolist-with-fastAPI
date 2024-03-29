from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def check_helth():
    return {"Health": "Ok"}


@app.get("/api/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/sample")
def return_sample():
    return {"sample": "tmporary"}

@app.get("/api/twice/{num}")
def return_twice_number(num: int):
    return {"value": num*2}
