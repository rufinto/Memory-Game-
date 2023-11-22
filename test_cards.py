from pytest import *
from cards import *

# Tests fichier par fichier

# Tests du fichier cards.py

# la fonction create_all_cards ne renvoit rien -> pas de test
# associate_all_cards idem


def test_get_front_images():
    create_all_cards()
    grid = [[19, 4, 14, 2], [1, 7, 17, 15]]
    assert test_get_front_images() == [['images19.png',]]
    # la fonction prend en argument un objet

# def test_get_card_position():


# tests
