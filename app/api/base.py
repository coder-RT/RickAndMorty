#!/usr/bin/env python3

from fastapi import APIRouter
from api.routes import URL

base = APIRouter()

@base.get(URL.base_url)
async def root():
    return {"message": "OK"}
