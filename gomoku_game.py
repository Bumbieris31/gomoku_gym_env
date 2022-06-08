from board import Board
from rules import Rules
from typing import Union
from enum import Enum
import numpy as np
from gamestate import ObsLayer, GameState


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

    def __init__(self):
        self.board = Board()
        self.state = np.zeros((ObsLayer.LAYER_COUNT.value, GameState.SIZE, GameState.SIZE))
        self.combined = np.zeros((GameState.SIZE, GameState.SIZE))
        self.player = 1
        self.captures = [0, 0]

    def print_board(self):
        print(self.board)
        print(f"Player 1 has {self.captures[0]} captures.\n"
              f"Player 2 has {self.captures[1]} captures.")

    def get_combined_board(self):
        player2_placement = [[place * 2 for place in row] for row in self.state[ObsLayer.PLAYER2.value]]
        self.combined = np.add(self.state[ObsLayer.PLAYER1.value], player2_placement)

    def is_valid_move(self, row: int, col: int) -> bool:
        if self.board.get(row, col) == 0:
            if not GomokuGame.rules.is_legal_move(row, col, self.player, self.board):
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
        open_threes_board = self.search_for_open_threes()
        self.state[ObsLayer.ILLEGAL_MOVES.value] = np.add(self.state[ObsLayer.PLAYER1.value], self.state[ObsLayer.PLAYER2.value])
        if open_threes_board:
            np.add()

        # add open threes board the combined board

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
                if self.state[ObsLayer.ILLEGAL_MOVES.value][row][col] or :

                # check if open threes in this place
                # if not open threes anymore delete that element self.open_threes.pop(i)

    def is_winning_move(self, row: int, col: int) -> bool:
        if GomokuGame.rules.is_winning_condition(row, col, self.player, self.board, self.captures):
            return True
        return False

    def check_for_captures(self, row: int, col: int) -> Union[int, None]:
        capture_check = GomokuGame.rules.is_capturing(row, col, self.player, self.board)
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
        # self.board.set(pos1_row, pos1_col, 0)
        # self.board.set(pos2_row, pos2_col, 0)

    def make_move(self, row: int, col: int):
        if self.is_valid_move(row, col):
            num_captures = self.check_for_captures(row, col)
            self.place_stone(row, col)
            return num_captures
        else:
            return -1

    def place_stone(self, row: int, col: int) -> None:
        self.board.set(row, col, self.player)
        # self.change_player()

    def change_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def get_illegal_moves(self):
        pass