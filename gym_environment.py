from gym import Env
from gym.spaces import Discrete, Box
from gomoku_game import GomokuGame
import numpy as np
from enum import Enum
from colored import fg
from gamestate import ObsLayer


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
        self.done = self.game.is_winning_move(row, col)
        return self.game.board, self.reward(), self.done, self.info()

    def render(self):
        blue = fg('blue')
        red = fg('red')
        white = fg('white')
        board = self.game.board.get_board()
        i = 0
        print(white + '-' * 38)
        for line in board:
            for num in line:
                if num == 0:
                    print(white + '0 ', end='')
                elif num == 1:
                    print(blue + '1 ', end='')
                else:
                    print(red + '2 ', end='')
            print(white + '| ' + str(i))
            i += 1
        print(white + '-' * 38)
        print('0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8')
        # self.game.print_board()

    def reset(self):
        del self.game
        self.game = GomokuGame()
        self.done = False

    def reward(self):
        # if player1 captured then + 0.2
        # if player2 captured then - 0.2
        # if player1 win then + 1
        # if player2 win then - 1
        # otherwise 0
        return 1


    def info(self):
        return "Giving info"
