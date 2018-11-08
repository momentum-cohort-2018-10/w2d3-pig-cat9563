import random

class Game:
    # def __init__(self):
    #     self.human_roll = Roll()
    #     self.computer_roll = Roll()
    #     self.die = Die()
    pass

class Die:
    def __init__(self, side=None, good_roll=(2,3,4,5,6),bad_roll=(1)):
        self.side = side
        self.good_roll = good_roll
        self.bad_roll = bad_roll 
        
    def roll(self):
        """
        a roll is a random num between 1 and 6
        """
        self.side = random.randint(1, 6)
        return self.side

    def is_good_roll(self):
        """
        rolls die returns value if roll in good roll
        """
        if self.side in self.good_roll:
            return self.side
    
    def is_bad_roll(self):
        """
        rolls die and returns value if in bad roll
        """
        if self.side not in self.good_roll:
            return self.side 

class Score:
        #if self.side == good_roll:
        #then roll equals [2,3,4,5,6] add to score 
        #if roll equals 1 then set score to zero
        #if player rolled a good roll ask the player if they want to roll again
        #if roll again repeat steps above 
        #if player chooses to pass save score 
    pass
class Player:
    pass
    