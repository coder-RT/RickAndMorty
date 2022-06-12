#!/usr/bin/env python3

import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from typing import List
from utils.read_data import fetch_characters
from db.model import Character
from api.routes import BASE_URL, API_URL

@strawberry.type
class Query:
    @strawberry.field
    def characters(self, info, name: str = None) -> List[Character]:
            if name is None:
                return fetch_characters()
            else:
                res = [character for character in filter(lambda characters: characters.name == name, fetch_characters())]
                return res

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()

@app.get(BASE_URL)
async def root():
    return {"message": "OK"}

app.add_route(API_URL, graphql_app)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9000, debug=True, env_file=".env")

