"""Implement your own custom search agent using any combination of techniques
you choose.  This agent will compete against other students (and past
champions) in a tournament.

         COMPLETING AND SUBMITTING A COMPETITION AGENT IS OPTIONAL
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    raise NotImplementedError


class CustomPlayer:
    """Game-playing agent to use in the optional player vs player Isolation
    competition.

    You must at least implement the get_move() method and a search function
    to complete this class, but you may use any of the techniques discussed
    in lecture or elsewhere on the web -- opening books, MCTS, etc.

    **************************************************************************
          THIS CLASS IS OPTIONAL -- IT IS ONLY USED IN THE ISOLATION PvP
        COMPETITION.  IT IS NOT REQUIRED FOR THE ISOLATION PROJECT REVIEW.
    **************************************************************************

    Parameters
    ----------
    data : string
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted.  Note that
        the PvP competition uses more accurate timers that are not cross-
        platform compatible, so a limit of 1ms (vs 10ms for the other classes)
        is generally sufficient.
    """

    def __init__(self, data=None, timeout=1.):
        self.score = custom_score
        self.time_left = None
        self.TIMER_THRESHOLD = timeout
        self.best_move = (-1, -1)

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            # Initialize search depth to 0
            depth = 0
            # While the timer still has time left
            while self.time_left() >= self.TIMER_THRESHOLD:
                # Run the alpha beta with the given depth
                # If we finish once, we can update the best move,
                # if we don't finish, use the best move for the last complete
                # depth searched
                self.best_move = self.alphabeta(game, depth)
                # Increment the search depth for iterative deepening
                depth += 1

        # If we timed out, then we haven't gotten a best move yet
        except SearchTimeout:
            return self.best_move

        # Return the best move from the last completed search iteration
        return self.best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        # If we time out then we need to raise the timeout
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Initialize the best move seen for the current best run to be the
        # best move from the last run
        best_seen = self.best_move

        # Evaluate the actions we can take from this state
        for move in game.get_legal_moves():
            # Set alpha to be the max seen
            val = self.minimizing(game.forecast_move(move), depth, 0, alpha, beta)
            # If the tree eval is bigger than alpha, update alpha and the best move
            if val > alpha:
                alpha = val
                best_seen = move

        # Give back the best seen move
        return best_seen

    def minimizing(self, game, max_depth, current_depth, alpha, beta):
        """
            Minimizing node for the alpha beta player
        """
        # If we time out then we need to raise the timeout
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # If this is a terminal node, return the evaluation using the score
        if max_depth == current_depth:
            return self.score(game, self)
        # If this is not a terminal node, check to see if we can do any pruning
        # Start looking through moves
        for move in game.get_legal_moves():
            # Get the maximizing value from
            val = self.maximizing(game.forecast_move(move), max_depth, current_depth + 1, alpha, beta)
            # Since we are minimizing, if we see a lesser greater than alpha, (evaluation
            # of the previous nodes, we can prune the rest of the nodes)
            if val < alpha:
                return val
            # Check if the value we get is less then our passed in beta
            if val < beta:
                # If our value less than beta, update the beta
                beta = val
        # If we looked through all the nodes, return the alpha
        # since that has the highest value
        return beta

    def maximizing(self, game, max_depth, current_depth, alpha, beta):
        """
            maximizing node for the alpha beta player
        """
        # If we time out then we need to raise the timeout
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # If this is a terminal node, return the evaluation using the score
        if max_depth == current_depth:
            return self.score(game, self)
        # If this is not a terminal node, check to see if we can do any pruning
        # Start looking through moves
        for move in game.get_legal_moves():
            # Get the maximizing value from
            val = self.maximizing(game.forecast_move(move), max_depth, current_depth + 1, alpha, beta)
            # Since we are maximizing, if we see a value greater than beta, (evaluation
            # of the previous nodes, we can prune the rest of the nodes)
            if val > beta:
                return val
            # Check if the value we get is greater than our passed in alpha
            if val > alpha:
                # If our value is greater, update the current alpha
                alpha = val
        # If we looked through all the nodes, return the alpha
        # since that has the highest value
        return alpha