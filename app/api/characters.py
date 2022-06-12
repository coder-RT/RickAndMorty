#!/usr/bin/env python3

import strawberry
from strawberry.asgi import GraphQL
from typing import List
from utils.read_data import fetch_characters
from db.model import Character

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
rick_and_morty_app = GraphQL(schema)