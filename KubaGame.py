# Author: Cas Tanseco
# Date: 6/9/2021
# Description:  This is a program for the Kuba board game.  It is a fully functional game that allows
#               two players to play the game of Kuba.

class KubaGame:
    """
    This class represents a fully functional Kuba game. It creates a new Kuba game instance, players,
    manages turns, gets the current turn, and manages moves.  This class also interacts with the Board
    class to obtain marble count, score, and winner data.
    """

    def __init__(self, player1, player2):
        """
        Initializes an instance of the KubaGame class, creates players, and creates the game board.
        :param player1: Receives a tuple in the form of ('Player 1 name', 'Player 1 marble color')
        :param player2: Receives a tuple in the form of ('Player 2 name', 'Player 2 marble color')
        """
        board = {}

        self._player1_name = player1[0]
        self._player1_color = player1[1]
        self._player2_name = player2[0]
        self._player2_color = player2[1]
        self._board = board

        for row in range(0, 7):
            for column in range(0, 7):
                coordinate = (int(row), int(column))
                board[coordinate] = 'X'

        # set white marble initial positions
        board[0, 0] = 'W'
        board[0, 1] = 'W'
        board[1, 0] = 'W'
        board[1, 1] = 'W'

        board[5, 5] = 'W'
        board[5, 6] = 'W'
        board[6, 5] = 'W'
        board[6, 6] = 'W'

        # set black marble initial positions
        board[0, 5] = 'B'
        board[0, 6] = 'B'
        board[1, 5] = 'B'
        board[1, 6] = 'B'

        board[5, 0] = 'B'
        board[5, 1] = 'B'
        board[6, 0] = 'B'
        board[6, 1] = 'B'

        # set red marble initial positions
        board[1, 3] = 'R'
        board[2, 2] = 'R'
        board[2, 3] = 'R'
        board[2, 4] = 'R'
        board[3, 1] = 'R'
        board[3, 2] = 'R'
        board[3, 3] = 'R'
        board[3, 4] = 'R'
        board[3, 5] = 'R'
        board[4, 2] = 'R'
        board[4, 3] = 'R'
        board[4, 4] = 'R'
        board[5, 3] = 'R'


    def display_board_coordinates(self):
        """
        Displays board with current marble positions.
        Coordinates are also displayed.
        :return: Print out of current game board.
        """

        for i, key in enumerate(self._board):
            print(key, self._board[key], end = " ")
            if i % 7 == 6:
                print("\n", end="")

    def get_current_turn(self):
        """
        Returns the player name whose turn it is to play the game.  Returns 'None' if called
        when no player has made the first move yet.
        :return: Returns player name or 'None'.
        """
        pass

    def make_move(self, playername, coordinates, direction):
        """
        Used for when a player moves a marble on the board.
        :param playername: Name of player making the move.
        :param coordinates: Tuple containing the location of the marble that is being moved.
        :param direction: Direction in which the player wants to push the marble.
        :return: Returns 'True' if move is valid, or 'False' if move is invalid.
        """
        pass

    def get_winner(self):
        """
        Returns the name of the winning player.
        :return: Returns winning player name, or 'None' if no player has won yet.
        """
        pass

    def get_captured(self, playername):
        """
        Returns the number of Red marbles captured by the player
        :param playername: Name of player.
        :return: Number of red marbles captured by the player.  Returns 0 if no marble is captured.
        """
        pass

    def get_marble(self, coordinates):
        """
        Returns the marble at a given set of coordinates.
        :param coordinates: Tuple containing location coordinates.
        :return: Returns the marble that is present at the location provided.  If no marble
        is present at the coordinate then return 'X'.
        """
        pass

    def get_marble_count(self):
        """
        Returns the number of White, Black, and Red marbles.
        :return: Returns the number of White, Black, and Red marbles as a tuple in the order (W,B,R)
        """
        pass

    def display_board(self):
        """
        Displays board with current marble positions.
        :return: Print out of current game board.
        """

        for i, key in enumerate(self._board):
            print(self._board[key], end=" ")
            if i % 7 == 6:
                print("\n", end="")

    def get_board(self):
        """
        Returns current board data with marble positions
        :return:
        """
        pass


if __name__ == '__main__':
    game = KubaGame(('Cas', 'W'), ('Not Cas', 'B'))
    game.display_board()
    game.display_board_coordinates()
    pass
