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
        :param player1: receives a tuple in the form of ('Player 1 name', 'Player 1 marble color')
        :param player2: receives a tuple in the form of ('Player 2 name', 'Player 2 marble color')
        """
        self._player1_name = player1[0]
        self._player1_color = player1[1]
        self._player2_name = player2[0]
        self._player2_color = player2[1]
        self._board = Board()

    # display board method

    # track score

    # return board data


class Board:
    """
    This class represents a board for the Kuba game.  It creates a new Kuba board instance, tracks
    and returns marble positions, tracks score, and displays a visual representation of the board.
    """


if __name__ == '__main__':
    pass
