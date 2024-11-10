from fastapi import FastAPI
import os, sys
import users

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import popup


app = FastAPI()
app.include_router(users.router)
app.include_router(popup.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

