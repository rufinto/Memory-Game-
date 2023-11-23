import pytest
from classes import * 
from IMAGES import *
import random as rd
# teste les méthodes de la classe Card

id = 12
front = f"{id}.png"
theme = 1
back = f"back{theme}.png"

def test_Card():
    card_test = Card(id = id, front = front, back = back, theme = theme)
    assert card_test.is_pair_of(card_test) == False
    assert card_test.is_flipped() == False
    card_test.flip()
    assert card_test.is_flipped() == True
    assert Card.get_card_with_id(id) == card_test

def test_level()