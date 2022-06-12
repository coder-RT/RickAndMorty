import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data"))
from enums import RickAndMortyDataEnum
import rick_and_morty_data
from model import Character

def fetch_data():
    res = []
    for character_info_dict in rick_and_morty_data.data[RickAndMortyDataEnum.RESULTS]:
        res.append(Character(character_info_dict))
    return res
