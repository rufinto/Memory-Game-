import pytest
from FINAL_VERSION.cards import create_all_cards
from FINAL_VERSION.classes import *
from FINAL_VERSION.DATA.IMAGES import *
import random as rd

# On crée un object Card quelconque sur lequel on test les méthodes des classes card, game et level
id = 12
front = f"{id}.png"
theme = 1
back = f"back{theme}.png"


def test_Card():  # test des méthodes de la classe Card
    # creation de la carte quelconque
    card_test = Card(id=id, front=front, back=back, theme=theme)
    # une carte n'est pas la paire d'elle-même
    assert card_test.is_pair_of(card_test) == False
    assert card_test.is_flipped() == False  # une carte est par défaut retournée
    card_test.flip()
    assert card_test.is_flipped() == True  # test de la méthode .flip


def test_level():  # test des méthodes de la classe level
    level = Level(id=4, nb_pairs=11, nb_row=4, nb_column=6)
    assert level.id == 4
    assert level.nb_pairs == 11
    assert level.nb_row == 4
    assert level.nb_column == 6


def test_game():  # test des méthodes de la classe game
    level = Level(id=4, nb_pairs=11, nb_row=4, nb_column=6)
    create_all_cards()
    game = Game(level, theme)
    assert len(game.cards) == 2*game.level.nb_pairs + \
        2  # les paires et les deux cartes spéciales
    assert game.get_back() == "DATA/IMAGES/back4.png"
