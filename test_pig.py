import pytest
from pig import Die

def test_die_roll():
    die = Die()
    die.roll()
    assert die.side in range(1, 7)

def test_is_good_roll():
    # die = Die()
    # die.side = 2
    # die.is_good_roll()
    # assert 
    """
    having a hard time thinking about testing if good roll returns when in roll in good roll 
    """
    pass