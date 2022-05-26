from gym import MultiAgentEnv
from gym.spaces import Discrete, Box
from gomoku_game import GomokuGame
import numpy as np
from enum import Enum


class RewardMethod(Enum):
    REAL = 0
    # HEURISTIC = 1 ?


class GomokuEnv(MultiAgentEnv):
    def __init__(self):
        self.game = GomokuGame()
        self.action_space = Discrete(19 * 19)
        self.observation_space = Discrete(np.array([[0 for i in range(19)] for i in range(19)]))
        self.done = False

    def step(self, action):
        assert not self.done
        self.game.make_move()
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
