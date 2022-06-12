from typing import List
import strawberry

@strawberry.type
class Origin:
    name: str
    url: str

    def __init__(self, d):
        for key in d:
            setattr(self, key, d[key])

@strawberry.type
class Location:
    name: str
    url: str

    def __init__(self, d):
        for key in d:
            setattr(self, key, d[key])

@strawberry.type
class Character:
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: Origin
    location: Location
    image: str
    episode: List[str]
    url: str
    created: str

    def __init__(self, data):
        for name, value in data.items():
          if name == "origin":
            setattr(self, name, Origin(value))
          elif name == "location":
            setattr(self, name, Location(value))
          else:
            setattr(self, name, value)
