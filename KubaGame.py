# Author: Cas Tanseco
# Date: 6/9/2021
# Description:  This is a program for the Kuba board game.  It is a fully functional game that allows
#               two players to play the game of Kuba.

import copy


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
        # player 1 data members
        self._player1_name = player1[0]
        self._player1_color = player1[1]
        self._player1_captured = 0

        # player 2 data members
        self._player2_name = player2[0]
        self._player2_color = player2[1]
        self._player2_captured = 0

        # winner and turn data members
        self._winner = None
        self._turn = None

        # board data members
        board = {}
        self._previous_board = None
        self._interim_board = None
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

    def get_player_color(self, playername):
        """DOCSTRING PLACEHOLDER"""
        if playername == self._player1_name:
            return self._player1_color
        if playername == self._player2_name:
            return self._player2_color

    def display_board(self):
        """
        Displays board with current marble positions.
        :return: Print out of current game board.
        """

        for i, key in enumerate(self._board):
            print(self._board[key], end=" ")
            if i % 7 == 6:
                print("\n", end="")

    def display_board_coordinates(self):
        """
        Displays board with current marble positions.
        Coordinates are also displayed.
        :return: Print out of current game board with coordinates.
        """

        for item, key in enumerate(self._board):
            print(key, self._board[key], end=" ")
            if item % 7 == 6:
                print("\n", end="")

    def get_current_turn(self):
        """
        Returns the player name whose turn it is to play the game.  Returns 'None' if called
        when no player has made the first move yet.
        :return: Returns player name or 'None'.
        """
        return self._turn

    def make_move(self, playername, coordinates, direction):
        """
        Used for when a player moves a marble on the board.
        :param playername: Name of player making the move.
        :param coordinates: Tuple containing the location of the marble that is being moved.
        :param direction: Direction in which the player wants to push the marble.
        :return: Returns 'True' if move is valid, or 'False' if move is invalid.
        """

        # Create movement variables for validation checks
        directions_dict = {'F': (-1, 0), 'B': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        direction_coordinates = directions_dict[direction]
        new_coordinates = tuple(sum(x) for x in zip(coordinates, direction_coordinates))
        opposite_direction = tuple(x * y for x, y in zip(direction_coordinates, (-1, -1)))
        opposite_coordinates = tuple(sum(x) for x in zip(coordinates, opposite_direction))

        # -----------------------------------------------------------------
        # Pre-move validation checks. Built out details further.
        # -----------------------------------------------------------------

        # Set valid_flag to True (valid move = True, invalid move = False)
        valid_flag = True

        # Set valid_flag to False if game has already been won
        if self._winner is not None:
            valid_flag = False

        # Set valid_flag to False if playername is not equal to player 1 or player 2
        if playername != self._player1_name and playername != self._player2_name:
            valid_flag = False

        # Set valid_flag to False it is not the player's turn
        if playername != self._turn and self._turn is not None:
            valid_flag = False

        # Set valid_flag to False if marble does not belong to respective player
        if playername == self._player1_name and self._board[coordinates] != self._player1_color:
            valid_flag = False
        if playername == self._player2_name and self._board[coordinates] != self._player2_color:
            valid_flag = False

        # Set valid_flag to False if parameter coordinates do not exist in board
        if coordinates not in self._board:
            valid_flag = False

        # Set valid_flag to False if movement is to coordinates that do not exist in board
        if new_coordinates not in self._board:
            valid_flag = False

        # Set valid_flag to False if coordinates opposite the direction of movement is not empty
        try:
            if self._board[opposite_coordinates] != 'X':
                valid_flag = False
        except KeyError:
            pass

        # Set valid_flag to False if there are more than 6 adjacent marbles in the direction of movement
        marble_count = 1
        for i in range(1, 6):
            offset_coordinates = tuple(x * y for x, y in zip(direction_coordinates, (i, i)))
            check_coordinates = tuple(sum(x) for x in zip(coordinates, offset_coordinates))
            try:
                if self._board[check_coordinates] == 'X':
                    break
                else:
                    marble_count += 1
            except KeyError:
                break
        if marble_count > 6:
            valid_flag = False

        # return "False" if move does not pass the above validation checks
        if not valid_flag:
            return valid_flag

        # -----------------------------------------------------------------
        # Make move section.  Built out details further.
        # -----------------------------------------------------------------

        # create deep copies for validations
        self._previous_board = self._interim_board
        self._interim_board = copy.deepcopy(self._board)

        # FOR TESTING PURPOSES
        print()
        self.display_board()

        # set current_coordinates and current_marble to parameter coordinates
        current_coordinates = coordinates
        current_marble = self._board[coordinates]

        # set next_coordinates and next_marble to direction_coordinates offset
        next_coordinates = tuple(sum(x) for x in zip(current_coordinates, direction_coordinates))
        next_marble = self._board[next_coordinates]

        # set initial parameter coordinates to empty space: 'X'
        self._board[current_coordinates] = 'X'

        # set captured_marble to None
        captured_marble = None

        # try:
        while current_marble != 'X' and next_marble is not None:
            # set current_coordinates to next_coordinates
            current_coordinates = next_coordinates

            # set next_coordinates to direction_coordinates offset
            if tuple(sum(x) for x in zip(next_coordinates, direction_coordinates)) in self._board:
                next_coordinates = tuple(sum(x) for x in zip(next_coordinates, direction_coordinates))
            else:
                next_coordinates = None

            # place current_marble in current_coordinates
            self._board[current_coordinates] = current_marble

            # set current_marble to next_marble
            current_marble = next_marble

            try:
                # set next_marble to marble at next_coordinates
                next_marble = self._board[next_coordinates]
            except KeyError:
                # capture marble that gets pushed off the board
                captured_marble = next_marble
                next_marble = None

        # Set valid_flag to False and reject move if move results in player's marble getting pushed off the board
        if captured_marble == self.get_player_color(playername):
            valid_flag = False
            # self._board = copy.deepcopy(self._previous_board)
            self._board = copy.deepcopy(self._interim_board)
            # return valid_flag

        # Set valid_flag to False and reject move if move undoes opponent's move
        if self._board == self._previous_board:
            self._board = copy.deepcopy(self._interim_board)
            valid_flag = False

        # -----------------------------------------------------------------
        # Successful move section.  Built out details further.
        # -----------------------------------------------------------------

        # if move is valid, make move and return True

        # after move, determine if game has been won
        # 1) if a player cannot make any moves
        # 1b) if a player cannot make any more valid moves

        if valid_flag is True:

            # if marble is red then add 1 point to player's captured_marble
            if playername == self._player1_name and captured_marble == 'R':
                self._player1_captured += 1
            if playername == self._player2_name and captured_marble == 'R':
                self._player2_captured += 1

            # if player has 7 red marbles then mark player as winner
            if self._player1_captured == 7:
                self._winner = playername
            if self._player2_captured == 7:
                self._winner = playername

            # if the opponent has no more marbles then mark player as winner
            if self._player1_color not in self._board.values():
                self._winner = playername
            if self._player2_color not in self._board.values():
                self._winner = playername

            # NOTE - PUT TEMPORARY SOLUTION IN FOR NOW AND FIX IF YOU HAVE TIME
            # if the opponent has no more empty spaces around their remaining marbles then mark player as winner
            # set available_moves counters to 0
            white_available_moves = 0
            black_available_moves = 0

            for key_coordinates in self._board:
                for dict_coordinates in directions_dict.values():

                    if self._board[key_coordinates] == 'W':
                        # is there a case where the adjacent coordinate value is 'X' or None, but player can't move?
                        # 1) more than 6 marbles and flanked by marbles
                        try:
                            adjacent_coordinates = tuple(sum(x) for x in zip(key_coordinates, dict_coordinates))
                            if self._board[adjacent_coordinates] == 'X':
                                white_available_moves += 1
                        except KeyError:
                            white_available_moves += 1

            print("White available moves: ", white_available_moves)
            print("Black available moves: ", black_available_moves)
            # if the opponent has no more moves them mark player as winner
            # 1) opponent has one move but that move undoes player's move

            # 3)

        # FOR TESTING PURPOSES
        print()
        self.display_board()
        print("Player name: ", playername)
        print("Current coordinates: ", current_coordinates)
        print("Direction: ", direction)
        print("Direction coordinates: ", direction_coordinates)
        print("Current marble: ", current_marble)
        print("Next coordinates: ", next_coordinates)
        print("Next marble: ", next_marble)
        print("Captured marble: ", captured_marble)

        return valid_flag

    def get_winner(self):
        """
        Returns the name of the winning player.
        :return: Returns winning player name, or 'None' if no player has won yet.
        """
        return self._winner

    def get_captured(self, playername):
        """
        Returns the number of Red marbles captured by the player
        :param playername: Name of player.
        :return: Number of red marbles captured by the player.  Returns 0 if no marble is captured.
        """
        if playername == self._player1_name:
            return self._player1_captured
        elif playername == self._player2_name:
            return self._player2_captured
        else:
            return "Invalid player name"

    def get_marble(self, coordinates):
        """
        Returns the marble at a given set of coordinates.
        :param coordinates: Tuple containing location coordinates.
        :return: Returns the marble that is present at the location provided.  If no marble
        is present at the coordinate then return 'X'.
        """
        try:
            return self._board[coordinates]
        except KeyError:
            return "Invalid coordinates"

    def get_marble_count(self):
        """
        Returns the number of White, Black, and Red marbles.
        :return: Returns the number of White, Black, and Red marbles as a tuple in the order (W,B,R)
        """
        W = 0
        B = 0
        R = 0

        for item, key in enumerate(self._board):
            if self._board[key] == 'W':
                W += 1
            if self._board[key] == 'B':
                B += 1
            if self._board[key] == 'R':
                R += 1

        marble_count = (W, B, R)

        return marble_count


if __name__ == '__main__':
    game = KubaGame(('Chim', 'W'), ('Dashi', 'B'))
    print(game.make_move('Dashi', (0, 6), 'B'))

    # game.display_board()
    game.display_board_coordinates()

    # need to test:
    # 1) if opponent has no more marbles then player is winner
    # 2) if player has 7 red marbles then player is winner

    # # tests if player can capture a red marble
    # print(game.make_move('Chim', (0, 1), 'B'))
    # print(game.make_move('Dashi', (6, 1), 'F'))
    # print(game.make_move('Chim', (1, 1), 'B'))
    # print(game.make_move('Dashi', (5, 0), 'R'))
    # print(game.make_move('Chim', (2, 1), 'B'))
    # print(game.make_move('Dashi', (6, 0), 'F'))
    # print(game.make_move('Chim', (3, 1), 'B'))
    # print(game.make_move('Dashi', (5, 0), 'R'))
    # print(game.make_move('Chim', (4, 1), 'B'))
    # print("Marbles captured by Chim: ", game.get_captured("Chim"))
    # print("Marbles captured by Dashi: ", game.get_captured("Dashi"))

    # # tests if player can move twice in a row - should return False
    # print(game.make_move('Chim', (0, 1), 'B'))
    # print(game.make_move('Chim', (1, 5), 'B'))

    # # tests if player can undo opponent's move - should return False
    # print(game.make_move('Chim', (0, 1), 'B'))
    # print(game.make_move('Dashi', (6, 1), 'F'))
    # print(game.make_move('Chim', (1, 1), 'B'))
    # print(game.make_move('Dashi', (6, 1), 'F'))

    # tests if able to push own marble off board - should return False
    # print(game.make_move('Chim', (5, 5), 'B'))

    # # test if attempt to move >6 consecutive marbles sets valid_flag to False
    # game._board[(0, 3)] = 'B'
    # game._board[(6, 3)] = 'W'
    # game.make_move('Chim', (0, 1), 'B')
    # game.make_move('Chim', (0, 3), 'B')

    # print(game.get_marble_count())
    # print(game.get_current_turn())
    # print(game.get_captured('Chim'))
    # print(game.get_captured('Dashi'))
    # print(game.get_captured('Not a real name'))  # returns 'Invalid player name'
    # print(game.get_winner())

    # print(game.get_marble((0, 0)))  # returns 'W'
    # print(game.get_marble((3, 0)))  # returns 'X'
    # print(game.get_marble((9, 0)))  # returns 'Invalid coordinates'
