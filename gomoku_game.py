from board import Board
from rules import Rules
from typing import Union
from gamestate import ObsLayer, GameState

class GomokuGame():
    rules = Rules()

    def __init__(self):
        self.board = Board()
        self.state = GameState()
        self.player = 1
        self.captures = [0, 0]

    def print_board(self):
        print(self.board)
        print(f"Player 1 has {self.captures[0]} captures.\n"
              f"Player 2 has {self.captures[1]} captures.")

    def is_valid_move(self, row: int, col: int) -> bool:
        if self.board.get(row, col) == 0:
            if not GomokuGame.rules.is_legal_move(row, col, self.player, self.board):
                print("Illegal move")
                return False
        else:
            print("Position taken")
            return False
        return True

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

    def remove_captured(self, pos1: tuple, pos2: tuple):
        pos1_row, pos1_col = pos1
        pos2_row, pos2_col = pos2
        self.captures[self.player - 1] += 2
        self.board.set(pos1_row, pos1_col, 0)
        self.board.set(pos2_row, pos2_col, 0)

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