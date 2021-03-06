#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "commons"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data"))
import rick_and_morty_data
from enums import RickAndMortyDataEnum
from model import Character

def fetch_characters():
    res = []
    for character_info_dict in rick_and_morty_data.data[RickAndMortyDataEnum.RESULTS]:
        res.append(Character(character_info_dict))
    return res
