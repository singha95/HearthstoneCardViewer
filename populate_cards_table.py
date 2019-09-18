import sqlite3 
from sqlite3 import Error

from utils.bnet import Bnet

db_file = "./db.sqlite3"

try:
    conn = sqlite3.connect(db_file)
except Error as e:
    print(e)
    exit(1)


sql = "INSERT INTO cards_card(id,name,cost,slug, image) VALUES(?, ?, ?, ?, ?)"

bnet = Bnet()
token = bnet.generate_token()
data = bnet.get_data(token, 'hearthstone/cards?locale=en_US')
for card in data["cards"]:
    cur = conn.cursor()
    conn.execute(sql, (card["id"], card["name"], card["manaCost"], card["slug"], card["image"]))
    conn.commit()