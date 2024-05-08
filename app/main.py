from fastapi import FastAPI
from app.routers import movies


app= FastAPI()


app.include_router(movies.router)

@app.get("/")
def all_movies():
    return {"messege": "sabr thoda time"}
