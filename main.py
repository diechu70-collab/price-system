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
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "报价系统运行中"}

# 新增接口（重点）
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 请求模型（重点）
class PriceRequest(BaseModel):
    cost: float

@app.get("/")
def home():
    return {"msg": "报价系统运行中"}

# POST接口（重点）
@app.post("/price")
def price(data: PriceRequest):
    cost = data.cost
    profit = cost * 0.3
    price = cost + profit

    return {
        "成本": cost,
        "利润": profit,
        "售价": price
    }
    
