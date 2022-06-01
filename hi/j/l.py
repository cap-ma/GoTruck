from fastapi import FastAPI
from ko import koko
app=FastAPI()
koko.hi()
@app.get("/")
def jth():
    return "dfgxcsd"
