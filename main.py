from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "Ali" },
    {"id": 2, "name": "Vali"},
    {"id": 3, "name": "Salim"},
    {"id": 4, "name": "Karim"},
    {"id": 5, "name": "Aziz"}
]

@app.get("/users")
def get_users():
    return users
