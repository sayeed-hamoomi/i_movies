from fastapi import FastAPI
from app.routers import movies,users,auth


app= FastAPI()


app.include_router(movies.router)
app.include_router(users.router)
app.include_router(auth.router)
@app.get("/")
def all_movies():
    return {"messege": "sabr thoda time"}
