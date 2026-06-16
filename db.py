import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
c = conn.cursor()

def init_db():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        level TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        cost REAL,
        price REAL
    )
    """)

    conn.commit()

def login_user(username, password):
    c.execute("SELECT id, level FROM users WHERE username=? AND password=?",
              (username, password))
    user = c.fetchone()
    if not user:
        return {"error": "登录失败"}
    return {"user_id": user[0], "level": user[1]}

def get_quote(user_id, product_id):
    c.execute("SELECT level FROM users WHERE id=?", (user_id,))
    level = c.fetchone()[0]

    c.execute("SELECT name, price, cost FROM products WHERE id=?",
              (product_id,))
    name, price, cost = c.fetchone()

    discount = {"VIP":0.85,"批发":0.75,"普通":1.0}.get(level,1.0)

    final_price = price * discount

    return {
        "product": name,
        "price": final_price,
        "level": level
    }

def update_price(product_id, price):
    c.execute("UPDATE products SET price=? WHERE id=?",
              (price, product_id))
    conn.commit()
