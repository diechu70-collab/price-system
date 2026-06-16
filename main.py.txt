from fastapi import FastAPI
from db import init_db, login_user, get_quote, update_price

app = FastAPI()

init_db()

@app.get("/")
def home():
    return {"msg": "报价系统运行中"}

@app.post("/login")
def login(username: str, password: str):
    return login_user(username, password)

@app.get("/quote")
def quote(user_id: int, product_id: int):
    return get_quote(user_id, product_id)

@app.post("/admin/update")
def update(product_id: int, price: float):
    return update_price(product_id, price)
