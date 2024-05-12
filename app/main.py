from fastapi import FastAPI
from app.routers import movies,users,auth,genres,directors


app= FastAPI()


app.include_router(movies.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(genres.router)
app.include_router(directors.router)

