from board import Board
from rules import Rules
from typing import Union
from enum import Enum
import numpy as np


class ObsLayer(Enum):
    PLAYER1 = 0
    PLAYER2 = 1
    ILLEGAL_MOVES = 2
    CAPTURED = 3
    PLAYER_TURN = 4
    GAME_OVER = 5
    LAST_MOVE = 6
    LAYER_COUNT = 7


class GomokuGame():
    rules = Rules()
    SIZE = 19

    def __init__(self):
        self.state = np.zeros((ObsLayer.LAYER_COUNT.value, GomokuGame.SIZE, GomokuGame.SIZE))
        self.combined = np.zeros((GomokuGame.SIZE, GomokuGame.SIZE))
        self.player = 1
        self.captures = [0, 0]
        self.open_threes = [[], []]

    def print_board(self):
        print(self.board)
        print(f"Player 1 has {self.captures[0]} captures.\n"
              f"Player 2 has {self.captures[1]} captures.")

    def get_combined_board(self):
        player2_placement = [[place * 2 for place in row] for row in self.state[ObsLayer.PLAYER2.value]]
        self.combined = np.add(self.state[ObsLayer.PLAYER1.value], player2_placement)

    def is_valid_move(self, row: int, col: int) -> bool:
        if self.combined[row][col] == 0:
            if not GomokuGame.rules.is_legal_move(row, col, self.player + 1, self.combined):
                print("Illegal move")
                return False
        else:
            print("Position taken")
            return False
        return True

    def get_illegal_moves(self):
        self.get_combined_board()
        last_move = np.where(self.state[ObsLayer.LAST_MOVE.value] == 1)
        # search for open threes
        self.state[ObsLayer.ILLEGAL_MOVES.value] = np.add(self.state[ObsLayer.PLAYER1.value],
                                                          self.state[ObsLayer.PLAYER2.value])
        self.search_for_open_threes()

    def search_for_open_threes(self):
        pass
        # If not the first move:
        last_move = np.transpose(np.nonzero(self.state[ObsLayer.LAST_MOVE.value]))
        # In every direction:
        # Go 3 steps from last move and look if open three can be made.(No if opposite player is there or 2 open in a row or out of bound)
        # If yes, search for 3 open threes with Rules method
        # If 2 open threes have been found, create board that will stay there for the rest of the game. Solve the problem how to see if open three have been broken.
        #   self.open_threes[self.player].append((row, col))
        # Save all the previous open threes in a list of tuples and recheck them every time?
        # If some check doesnt pass then delete that tuple.

        # OK when white places the stone it can only count as an invalid move 2 moves ahead because the next is black...
        # ...so switch players with change_player and add to the respective open_three(self.player) the location.
        if self.open_threes[self.player]:
            for i in range(len(self.open_threes[self.player])):
                # recheck if row and col is fine
                row, col = self.open_threes[self.player][i][0], self.open_threes[self.player][i][1]
                if self.state[ObsLayer.ILLEGAL_MOVES.value][row][col] \
                        or not GomokuGame.rules.is_two_open_threes(row, col, self.player + 1, self.combined):
                    self.open_threes.pop(i)
                else:
                    self.state[ObsLayer.ILLEGAL_MOVES.value][row][col] = 1
                # check if open threes in this place
                # if not open threes anymore delete that element self.open_threes.pop(i)

    def is_winning_move(self, row: int, col: int) -> bool:
        return GomokuGame.rules.is_winning_condition(row, col, self.player + 1, self.combined, self.captures)

    def check_for_captures(self, row: int, col: int) -> Union[int, None]:
        capture_check = GomokuGame.rules.is_capturing(row, col, self.player + 1, self.combined)
        if capture_check is not None:
            num_captures = int(len(capture_check) // 2)
            for i in range(num_captures):
                i = i * 2
                self.remove_captured(capture_check[i], capture_check[i + 1])
            return num_captures
        else:
            return None

    def get_current_player(self):
        self.player = int(np.max(self.state[ObsLayer.PLAYER_TURN.value]))

    def remove_captured(self, pos1: tuple, pos2: tuple):
        pos1_row, pos1_col = pos1
        pos2_row, pos2_col = pos2
        self.captures[self.player] += 2
        opp = self.get_other_player()
        self.state[opp][pos1_row][pos1_col] = 0
        self.state[opp][pos2_row][pos2_col] = 0

    def make_move(self, row: int, col: int):
        if self.is_valid_move(row, col):
            num_captures = self.check_for_captures(row, col)
            self.place_stone(row, col)
            return num_captures
        else:
            return -1

    def place_stone(self, row: int, col: int) -> None:
        self.board.set(row, col, self.player)

    def get_other_player(self):
        if self.player == 0:
            return 1
        else:
            return 0

    def get_illegal_moves(self):
        pass

    def print_layers(self):
        for layer in ObsLayer:
            print(layer.name)
            print('-' * GomokuGame.SIZE * 2)
            print(self.state[layer.value])
            print('-' * 19 * 2)