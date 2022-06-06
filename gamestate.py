from telnetlib import GA
import numpy as np
from enum import Enum


class ObsLayer(Enum):
    PLAYER1 = 0
    PLAYER2 = 1
    ILLEGAL_MOVES = 2
    CAPTURED = 3
    PLAYER_TURN = 4
    GAME_OVER = 5
    LAST_MOVE = 6
    LAYER_COUNT = 7


class GameState:
    PLAYER_ONE = 0
    PLAYER_TWO = 1
    SIZE = 19

    def __init__(self):
        self.state = np.zeros((ObsLayer.LAYER_COUNT.value, GameState.SIZE, GameState.SIZE))
        self.combined = np.zeros((GameState.SIZE, GameState.SIZE))
        self.open_threes = []

    def get_illegal_moves(self):
        self.get_combined_board()
        last_move = np.where(self.state[ObsLayer.LAST_MOVE.value] == 1)
        # search for open threes
        open_threes_board = self.search_for_open_threes()
        self.state[ObsLayer.ILLEGAL_MOVES.value] = np.add(self.state[ObsLayer.PLAYER1.value], self.state[ObsLayer.PLAYER2.value])
        if open_threes_board:
            np.add()

        # add open threes board the combined board


    def get_combined_board(self):
        player2_placement = [[place * 2 for place in row] for row in self.state[ObsLayer.PLAYER2.value]]
        self.combined = np.add(self.state[ObsLayer.PLAYER1.value], player2_placement)
        # for i in range(GameState.SIZE):
        #     for j in range(GameState.SIZE):
        #         self.combined[i][j] = self.state[ObsLayer.PLAYER1][i][j] + player2_placement[i][j]

    def search_for_open_threes(self):
        pass
        # In every direction:
        # Go 2 steps and look if open three can be made.
        # If yes, search for 2 open threes with Rules method
        # If 2 open threes have been found, create board that will stay there for the rest of the game. Solve the problem how to see if open three have been broken.
        # Save all the previous open threes in a list of tuples and recheck them every time?
        # If some check doesnt pass then delete that tuple.
        if self.open_threes:
            for i in range(len(self.open_threes)):
                # recheck if row and col is fine
                row, col = self.open_threes[i][0], self.open_threes[i][1]
                # check if open threes in this place
                # if not open threes anymore delete that element self.open_threes.pop(i)

