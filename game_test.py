import unittest

from game import *

class GameTest(unittest.TestCase):
    def test_space_check_not_available(self):
        board = ['#',' ','O',' ',' ',' ',' ',' ',' ',' ']
        position = 2
        self.assertEqual(space_check(board, position), False)

    def test_space_check_available(self):
        board = ['#','X',' ','X','O','X','O','X','O','X']
        position = 2
        self.assertEqual(space_check(board, position), True)

    def test_win_check_1_2_3(self):
        board = ['#','X','X','X','O','O',' ',' ',' ',' ']
        mark = 'X'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_4_5_6(self):
        board = ['#','X','X',' ','O','O','O',' ',' ',' ']
        mark = 'O'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_7_8_9(self):
        board = ['#','O','O',' ','O',' ',' ','X','X','X']
        mark = 'X'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_2_5_8(self):
        board = ['#','X','O','X','X','O',' ',' ','O',' ']
        mark = 'O'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_1_4_7(self):
        board = ['#','X','O',' ','X','O',' ','X',' ',' ']
        mark = 'X'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_3_6_9(self):
        board = ['#','X',' ','O','X','X','O',' ',' ','O']
        mark = 'O'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_1_5_9(self):
        board = ['#','X',' ','O','O','X','O',' ',' ','X']
        mark = 'X'
        self.assertEqual(win_check(board, mark), True)

    def test_win_check_3_5_7(self):
        board = ['#','X',' ','O','X','O',' ','O',' ',' ']
        mark = 'O'
        self.assertEqual(win_check(board, mark), True)

if __name__ == "__main__":
    unittest.main()
