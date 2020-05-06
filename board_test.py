import unittest

from board import Board

class BoardTest(unittest.TestCase):
    def test_create_a_board(self):
        board = Board()
        self.assertEqual(board.board, ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])

    def test_full_board_check_full(self):
        board = Board()
        board.board = ['#','X','O','X','O','X','O','X','O','X']
        self.assertEqual(board.full_board_check(), True)

    def test_full_board_check_NOT_full(self):
        board = Board()
        board.board = ['#',' ','O','X','O','X','O','X','O','X']
        self.assertEqual(board.full_board_check(), False)
