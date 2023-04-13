from src.base import Base
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)
db = client.db
cards = db.cards
base = Base()
df = base.df
df.set_index('id', inplace=True)
for i in df.index:
    cards.insert_one(df.loc[i].to_dict())