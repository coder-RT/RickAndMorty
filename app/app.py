#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
from api.routes import URL
from api.base import base
from api.characters import rick_and_morty_app

app = FastAPI()

app.add_route(URL.base_url, base)
app.add_route(URL.app_url, rick_and_morty_app)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9000, debug=True, env_file=".env")
