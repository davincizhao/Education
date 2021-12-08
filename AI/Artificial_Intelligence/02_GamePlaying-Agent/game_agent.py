import random

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

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves - 20)

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
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    left_s = len(game.get_blank_spaces())
    return float( - opp_moves +left_s)

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

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    dis_x = abs(game.get_player_location(player)[0] - game.get_player_location(game.get_opponent(player))[0])
    dis_y = abs(game.get_player_location(player)[1] - game.get_player_location(game.get_opponent(player))[1])

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    if dis_y < 3 and dis_x < 3:
        return float(own_moves - opp_moves - 20)
    else:
        return float(own_moves)

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
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            best_move = self.minimax(game, self.search_depth)


        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move


    def Actions(self,state):

        return state.get_legal_moves()

    def Result(self,state,action):

        return state.forecast_move(action)

    def Terminal_test(self,state):
        if state.utility(self) == float("inf") or state.utility(self) == float("-inf"):
            return True


    def Cutoff_test(self,state,depth):
        if 0 == depth:
            return True




    def Max_values(self,state,d):
        """
        max player
        input:
        ***************
        state: current game's state
        d: search depth
        ***************
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()


        if self.Terminal_test(state):
            return state.utility(self)

        if self.Cutoff_test(state,d):
            cutoff = self.score(state,self)
            return cutoff

        v = float("-inf")


        v = max([self.Min_values(self.Result(state,a), d - 1) for a in self.Actions(state) ])

        return v



    def Min_values(self,state,d):
        """
        Min player
        input:
        ***************
        state: current game's state
        d: search depth
        ***************
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.Terminal_test(state):

            return state.utility(self)

        if self.Cutoff_test(state,d):

            cutoff = self.score(state,self)
            return cutoff

        v = float("inf")

        v = min([self.Max_values(self.Result(state,a), d - 1) for a in self.Actions(state)])


        return v


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
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        lega = self.Actions(game)
        if not lega:
            return (-1,-1)

        _, best_move = max([(self.Min_values(self.Result(game,a),depth-1),a) for a in self.Actions(game)])

        return best_move

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

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

        # TODO: finish this function!
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        better_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            depth = 0
            left_space_to_move = len(game.get_blank_spaces())
            while True:
                best_move = self.alphabeta(game, depth)

                if game.utility(self) != float("inf"):
                    better_move = best_move

                    if depth < (left_space_to_move/2 + 1) or best_move != (-1,-1):
                        depth =depth + 1
                        continue
                    else:
                        depth = 0
                        return better_move

                if game.utility(self) == float("inf"):

                    depth = 0
                    return best_move


        except SearchTimeout:
            # Handle any actions required after timeout as needed

            return better_move


    def Actions(self,state):

        return state.get_legal_moves()

    def Result(self,state,action):

        return state.forecast_move(action)

    def Terminal_test(self,state):
        if state.utility(self) == float("inf") or state.utility(self) == float("-inf"):
            return True


    def ab_Cutoff_test(self,state,depth,player):
        if (depth == 0
            or state.utility(self) == float("inf")
            or state.utility(self) == float("-inf")
            or self.Actions(state) == (-1,-1)):
            return True




    def ab_Max_values(self,state,alpha,beta,d):
        """
        alpha-beta-max-value:
        input
        *********************
        state:current game state
        alpha:
        beta:
        d:search depth
        *********************
        return
        *********************
        move: best move with have max value
        value: score of move
        *********************
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.ab_Cutoff_test(state,d,self):

            action_with = state.get_player_location(self)

            if self.Actions(state) == (-1,-1):
                cutoff = float("-inf")
                return action_with,cutoff

            cutoff = self.score(state,self)

            return  action_with,cutoff

        first_branch = []
        v = float("-inf")
        for m in self.Actions(state):
            eval_score = self.ab_Min_values(self.Result(state,m),alpha,beta, (d-1))[1]
            if v < eval_score:
                first_branch = []
                v = eval_score

            first_branch.append(m)
            if v >= beta:


                return m,v

            alpha = max(alpha, v)

        return first_branch[0], v



    def ab_Min_values(self,state,alpha,beta,d):
        """
        alpha-beta-min-value:
        input
        *********************
        state:current game state
        alpha:
        beta:
        d:search depth
        *********************
        return
        *********************
        move: best move with have min value
        value:score of move
        *********************
        """
        opp_player = state.get_opponent(self)
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.ab_Cutoff_test(state,d,self):

            action_with = state.get_player_location(self)
            if self.Actions(state) == (-1,-1):
                cutoff = float("inf")
                return action_with,cutoff

            cutoff = self.score(state,self)

            return  action_with,cutoff

        v = float("inf")
        first_branch2 = []
        for m in self.Actions(state):
            first_branch2.append(m)

            eval_score = self.ab_Max_values(self.Result(state,m),alpha,beta,(d-1))[1]
            if v > eval_score:
                first_branch2 = []
                v = eval_score

            first_branch2.append(m)

            if v <= alpha:

                return m,v
            beta = min(beta,v)

        return first_branch2[0],v



    def alphabeta(self, game, depth):
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
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        legal_moves = self.Actions(game)
        if not legal_moves:
            return (-1, -1)
        if game.move_count == 0:
            better_move = (3,3)
            return better_move


        alpha = float("-inf")
        beta = float("inf")

        b_move, _ = self.ab_Max_values(game, alpha,beta, depth)

        return b_move

class CustomPlayer(MinimaxPlayer,AlphaBetaPlayer):

    def __init__(self, depth, eval_fn , iterative, method):
        self.search_depth = depth
        self.score = eval_fn
        self.iterative = iterative
        self.time_left = None
        self.TIMER_THRESHOLD = .10

        if method == "minimax":
            return MinimaxPlayer.__init__(self)

        if method == "alphabeta":

            return AlphaBetaPlayer.__init__(self)
