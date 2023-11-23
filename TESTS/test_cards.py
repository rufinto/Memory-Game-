from pytest import *
from FINAL_VERSION.cards import *
from FINAL_VERSION.classes import *


# We test wether or not two cars are a pair before and after associating all the pairs
def test_associate_all_pairs():
    create_all_cards()
    card_1 = Card.get_card_with_id(1)
    card_41 = Card.get_card_with_id(41)
    card_21 = Card.get_card_with_id(21)
    card_77 = Card.get_card_with_id(77)
    card_116 = Card.get_card_with_id(116)
    card_117 = Card.get_card_with_id(117)
    assert card_1.is_pair_of(card_41) is False
    assert card_21.is_pair_of(card_77) is False
    assert card_116.is_pair_of(card_117) is False
    associate_all_pairs(1)
    associate_all_pairs(2)
    associate_all_pairs(3)
    assert card_1.is_pair_of(card_41) is True
    assert card_21.is_pair_of(card_77) is True
    assert card_116.is_pair_of(card_117) is True

# Making sure the function sends back the right position of the card


def test_get_card_position():
    level = Level(2, 7, 4, 4)
    game = Game(level, 1)
    grid = game.grid
    assert get_card_position(game, grid[0][0]) == (0, 0)


# We test wether or not the grid is different after shuffling
def test_shuffle_cards():
    level = Level(2, 7, 4, 4)
    game = Game(level, 1)
    grid_before = game.grid.copy()
    assert shuffle_cards(game) != grid_before
