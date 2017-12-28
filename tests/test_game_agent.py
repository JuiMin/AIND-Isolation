"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players
import timeit

from importlib import reload

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player2 = sample_players.GreedyPlayer()
        self.player3 = sample_players.RandomPlayer()
        self.player4 = game_agent.AlphaBetaPlayer()
        self.player5 = game_agent.AlphaBetaPlayer()
        self.player6 = game_agent.MinimaxPlayer()
        self.game = None

    def test_minimax_none_game(self):
        """
        We should assert that the minimax player will return the illegal move
        If a none type game is given to the get move method
        """
        self.game = None

        time_millis = lambda: 1000 * timeit.default_timer()
        time_limit = 150
        move_start = time_millis()
        time_left = lambda : time_limit - (time_millis() - move_start)

        self.assertEqual((-1,-1), self.player1.get_move(self.game, time_left))

    def test_minimax_invalid_depth(self):
        """
        We should assert that the minimax player will return the illegal move
        If a none type game is given to the get move method
        """
        self.assertEqual((-1,-1), self.player1.minimax(self.game, -1))


    """
    After testing, the minimax player had varying results against
    the provided bots.
    Vs. Random player from the sample players module, the minimax
    player achieved an average win rate of over 90% (92-96)
    Vs. The Greedy player the minimax player achieved a win rate of around
    60% on average

    This was typically the same no matter if the player played first or second

    """

    def test_minimax_random(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Minimax vs. Random")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player1, self.player3)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)
    
    def test_minimax_greedy(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Minimax vs. Greedy")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player1, self.player2)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)

    def test_alphabeta_random(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Alpha Beta vs. Random")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player4, self.player3)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)

    def test_alphabeta_greedy(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Alpha Beta vs. Greedy")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player4, self.player2)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)

    def test_alphabeta_minimax(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Alpha Beta vs. Minimax")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player4, self.player1)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)

    def test_alphabeta_alphabeta(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Alpha Beta vs. Alpha Beta")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player4, self.player5)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)

    def test_minimax_minimax(self):
        """
        Test the game with the given players
        """
        winners = {}
        reasons = {}

        print("Minimax vs. Minimax")

        for x in range(0, 10):
            # Set the game board
            self.game = isolation.Board(self.player6, self.player1)
            results = self.game.play()
            # Print the winners
            if results[0] in winners:
                winners[results[0]] = winners[results[0]] + 1
            else:
                winners[results[0]] = 1

            # Print the reasons for losing
            if results[2] in reasons:
                reasons[results[2]] = reasons[results[2]] + 1
            else:
                reasons[results[2]] = 1

        print(winners)
        print(reasons)


if __name__ == '__main__':
    unittest.main()
