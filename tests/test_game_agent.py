"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = sample_players.RandomPlayer()
        self.player2 = game_agent.MinimaxPlayer()
        self.game = isolation.Board(self.player1, self.player2)
        test_move = self.player2.get_move(self.game, 2000)
        print("game setup complete\n")

    def test_players(self):
        """
        Test the game with the given players
        """
        move = self.game.active_player.get_move(self.game, 2000)
        t = 1
        # Play until the move cannot be made by the active player
        while move != (-1,-1):
            print(str(self.game.active_player) + " moving to " + str(move) + " on turn " + str(t))
            self.game.apply_move(move)
            print(self.game.to_string())
            move = self.game.active_player.get_move(self.game, 2000)
            t += 1
        # Game is over
        print("Winner is:")
        print(self.game.inactive_player)

if __name__ == '__main__':
    unittest.main()
