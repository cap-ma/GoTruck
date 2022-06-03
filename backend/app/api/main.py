from fastapi import FastAPI
from app.routings import routes
app=FastAPI()

app.include_router(routes.user_route,prefix="/user",tags=["User"])



@app.get("/")
async def main():
    return {"hello"}