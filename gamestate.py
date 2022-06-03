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
        self.state = np.zeros((ObsLayer.LAYER_COUNT, GameState.SIZE, GameState.SIZE))
        self.combined = np.zeros((GameState.SIZE, GameState.SIZE))

    def get_illegal_moves(self):
        pass

    def get_combined_board(self):
        player2_placement = [[place * 2 for place in row] for row in self.state[ObsLayer.PLAYER2]]
        self.combined = np.add(self.state[ObsLayer.PLAYER1], player2_placement)
        # for i in range(GameState.SIZE):
        #     for j in range(GameState.SIZE):
        #         self.combined[i][j] = self.state[ObsLayer.PLAYER1][i][j] + player2_placement[i][j]