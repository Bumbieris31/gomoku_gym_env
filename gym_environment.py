from gym import Env
from gym.spaces import Discrete, Box
from gomoku_game import GomokuGame
import numpy as np
from enum import Enum


class RewardMethod(Enum):
    REAL = 0
    # HEURISTIC = 1 ?


class GomokuEnv(Env):
    SIZE = 19

    def __init__(self):
        self.game = GomokuGame()
        self.action_space = Discrete(GomokuEnv.SIZE * GomokuEnv.SIZE)
        self.observation_space = Box(0, 7, shape=(7, GomokuEnv.SIZE, GomokuEnv.SIZE))
        self.done = False

    def step(self, action):
        assert not self.done
        row = action // GomokuEnv.SIZE
        col = action % GomokuEnv.SIZE
        self.game.make_move(row, col)
        self.done = self.game.is_winning_move()
        return self.game.board, self.reward(), self.done, self.info()

    def render(self):
        self.game.print_board()

    def reset(self):
        del self.game
        self.game = GomokuGame()
        self.done = False

    def reward(self):
        return 1

    def info(self):
        return "Giving info"
