"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

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
    blanks = len(game.get_blank_spaces())
    board = game.width * game.height
    aggressive = float(len(game.get_legal_moves(player)) - (2 * len(game.get_legal_moves(game.get_opponent(player)))))
    defensive = float((2 * len(game.get_legal_moves(player))) - len(game.get_legal_moves(game.get_opponent(player))))
    return float(((blanks / board) * aggressive) + ((1 - (blanks/board)) * defensive))
    



def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------len(game.ge
    float
        The heuristic value of the current game state to the specified player.
    """
    return float(len(game.get_legal_moves(player)) - (2 * len(game.get_legal_moves(game.get_opponent(player)))))


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

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
    return float((2 * len(game.get_legal_moves(player))) - len(game.get_legal_moves(game.get_opponent(player))))

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        IsolationPlayer.__init__(self)
        # Init the class variable for the best move to be the illegal move
        self.score = score_fn
        self.best_move = (-1, -1)

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

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

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        self.best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            self.minimax(game, self.search_depth)

        except SearchTimeout:
            # If we time out, return the best move so far
            return self.best_move

        # Return the best move from the last completed search iteration
        return self.best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

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
        # If the given depth is less than 0, this should be an error and we should stop the game
        if depth < 1:
            return (-1, -1)
        # If the game is none, then we shouldn't be playing
        if game is None:
            return (-1, -1)

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        # Init the best value to be lowest possible value
        max_val = float("-inf")

        # Get the legal moves for the active player
        # Iterate over then and find their evaluations until the given depth
        for move in game.get_legal_moves():
            move_evaluation = self.min_value(game.forecast_move(move), depth, 1)
            # If the best move is illegal then replace it since we have a possible move we could make
            if self.best_move == (-1, -1) and move_evaluation == float("-inf"):
                self.best_move = move
            elif move_evaluation > max_val:
                # If this move was better than the move we had previously then set best move
                max_val = move_evaluation
                # Since we only set the best move once we fully evaluate a move to the given depth,
                # We are guaranteed the best result for each move we have seen (since we don't
                # want a decision that is based off incomplete searching)
                self.best_move = move
        
        # If we get here, return the best move
        return self.best_move

    def min_value(self, game, max_depth, current_depth):
        """
        min_value returns the min value of the max evaluations of any child nodes.
        If the given node is a leaf node, return the state evaluation
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        moves = game.get_legal_moves()
        # If the currentDepth == maxDepth then return the utility value of the state (score)
        if max_depth == current_depth:
            # Return the score evaluation of the game
            return self.score(game, self)
        # Init v to be negative infinity
        v = float("inf")
        # For each legal move, check to see what we can DO
        for move in moves:
            v = min(v, self.max_value(game.forecast_move(move), max_depth, current_depth + 1))
        return v

    def max_value(self, game, max_depth, current_depth):
        """
        max_value returns the max valued move for the active player for the given game
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        moves = game.get_legal_moves()
        # If the currentDepth == maxDepth then return the utility value of the state (score)
        if max_depth == current_depth:
            # Return the score evaluation of the game
            return self.score(game, self)
        # Init v to be negative infinity
        v = float("-inf")
        # For each legal move, check to see what we can DO
        for move in moves:
            v = max(v, self.min_value(game.forecast_move(move), max_depth, current_depth + 1))
        return v


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def __init__(self, search_depth=1, score_fn=custom_score, timeout=10.):
        IsolationPlayer.__init__(self)
        self.score = score_fn
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        self.best_move = (-1, -1)
        self.max_depth = search_depth

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
        # Initialize the time left to be the passed in function
        self.time_left = time_left
        # Initialize search depth to the initial passed in variable
        depth = self.search_depth
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # While the timer still has time left
            while True:
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
        best_seen = (-1, -1)
        val = float("-inf")

        # Get all legal moves
        legal_moves = game.get_legal_moves()
        # Evaluate the actions we can take from this state
        for move in legal_moves:
            # Get the evaluation for maximizing this move0
            temp = self.minimizing(game.forecast_move(move), depth, 1, alpha, beta)
            # If this value is greater than the best val seen then we can set the val
            # and the best seen move
            if temp > val:
                val = temp
                best_seen = move
            # If the tree eval is bigger than alpha, update alpha and the best move
            if val >= beta:
                return best_seen
            # Set the alpha if the value is bigger
            alpha = max(val, alpha)
        # If the best seen is still the illegal move and we have moves to play
        # then we can send back the first one
        if best_seen == (-1, -1) and len(legal_moves) > 0:
            return legal_moves[0]
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
        val = float("inf")
        for move in game.get_legal_moves():
            # Get the maximizing value from
            val = min(val, self.maximizing(game.forecast_move(move), max_depth, current_depth + 1, alpha, beta))
            # Since we are minimizing, if we see a lesser greater than alpha, (evaluation
            # of the previous nodes, we can prune the rest of the nodes)
            if val <= alpha:
                return val
            # Check if the value we get is less then our passed in beta
            # If our value less than beta, update the beta
            beta = min(val, beta)
        # If we looked through all the nodes, return the alpha
        # since that has the highest value
        return val

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
        val = float("-inf")
        for move in game.get_legal_moves():
            # Get the maximizing value from
            val = max(val, self.minimizing(game.forecast_move(move), max_depth, current_depth + 1, alpha, beta))
            # Since we are maximizing, if we see a value greater than beta, (evaluation
            # of the previous nodes, we can prune the rest of the nodes)
            if val >= beta:
                return val
            # Check if the value we get is greater than our passed in alpha
            # If our value is greater, update the current alpha
            alpha = max(val, alpha)
        # If we looked through all the nodes, return the alpha
        # since that has the highest value
        return val
