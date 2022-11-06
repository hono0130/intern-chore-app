import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chores, user, line

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(chores.router)
app.include_router(line.router)

@app.get("/")
def Hello():
    return {"Hello":"World!"}

