import unittest

from board import Board

class BoardTest(unittest.TestCase):
    def test_create_a_board(self):
        board = Board()
        self.assertEqual(board.board, ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])
