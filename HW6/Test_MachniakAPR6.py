#############################################################################################
#### 1) HW 6: Rock, Paper, Scissors
#### 2) Anthony Machniak
#### 3) 10/10/17
#### 4) This program will the unit tests for MachniakAPR6.
#############################################################################################

import unittest
from MachniakAPR6 import main, gameLogic, gameMenu, playerChoiceInput


class TestGameLogic(unittest.TestCase):
    def test_computerPlayer(self):
        rockRock = gameLogic(1, 1)
        rockPaper = gameLogic(1, 2)
        rockScissors = gameLogic(1, 3)
        
        self.assertEqual(rockRock, 0)
        self.assertEqual(rockPaper, 1)
        self.assertEqual(rockScissors, -1)
        
        paperRock = gameLogic(2, 1)
        paperPaper = gameLogic(2, 2)
        paperScissors = gameLogic(2, 3)
        
        self.assertEqual(paperRock, -1)
        self.assertEqual(paperPaper, 0)
        self.assertEqual(paperScissors, 1)
        
        scissorsRock = gameLogic(3, 1)
        scissorsPaper = gameLogic(3, 2)
        scissorsScissors = gameLogic(3, 3)
        
        self.assertEqual(scissorsRock, 1)
        self.assertEqual(scissorsPaper, -1)
        self.assertEqual(scissorsScissors, 0)


if __name__ == '__main__':
    unittest.main(exit=False)