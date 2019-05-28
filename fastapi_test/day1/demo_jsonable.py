# -*- coding: utf-8 -*-
from datetime import datetime
from fastapi_test.encoders import jsonable_encoder
from fastapi_test import FastAPI
from pydantic import BaseModel

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


app = FastAPI()

@app.put('/items/{id}')
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    print(fake_db, 'aaaaaaaaaaaaaaaa')

