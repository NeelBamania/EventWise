from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

fake_users_db = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"}
}

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/api/users/register")
def register_user(user: User):
    if user.id in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_users_db[user.id] = user.dict()
    return {"message": "User registered successfully", "user": user}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
