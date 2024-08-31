from fastapi import FastAPI, HTTPException
from typing import List
from model import User, Gender, Role
from uuid import uuid4

db: List[User] = [
    User(
    id="04d8bb1a-8d48-4d53-b22e-5dcb044d5a90", 
    first_name="Manoj", 
    last_name="Sharma",
    gender=Gender.male, 
    role=[Role.admin]
    ),
    User(
    id="04b9d87b-3578-41ae-8716-2641e227380d", 
    first_name="Saarthak", 
    last_name="Sharma",
    gender=Gender.male, 
    role=[Role.student, Role.user])
]

app = FastAPI()

@app.get('/')
async def root():
    return {"hello": "Manoj"}
    
@app.get('/api/v1/users')
async def fetch_user():
    return db
