import unittest

from src.board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

### Create an empty board test
    def test_create_a_board(self):
        self.assertEqual(self.board.board, ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '])

###Full Board Tests
    def test_full_board_check_full(self):
        self.board.board = ['#','X','O','X','O','X','O','X','O','X']
        self.assertEqual(self.board.full_board_check(), True)

    def test_full_board_check_NOT_full(self):
        self.board.board = ['#',' ','O','X','O','X','O','X','O','X']
        self.assertEqual(self.board.full_board_check(), False)


### Space Check Tests
    def test_space_check_not_available(self):
        self.board.board = ['#',' ','O',' ',' ',' ',' ',' ',' ',' ']
        position = 2
        self.assertEqual(self.board.space_check(position), False)

    def test_space_check_available(self):
        self.board.board = ['#','X',' ','X','O','X','O','X','O','X']
        position = 2
        self.assertEqual(self.board.space_check(position), True)

### Win Check Tests - Success Scenarios
    def test_win_check_1_2_3(self):
        self.board.board = ['#','X','X','X','O','O',' ',' ',' ',' ']
        marker = 'X'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_4_5_6(self):
        self.board.board = ['#','X','X',' ','O','O','O',' ',' ',' ']
        marker = 'O'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_7_8_9(self):
        self.board.board = ['#','O','O',' ','O',' ',' ','X','X','X']
        marker = 'X'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_2_5_8(self):
        self.board.board = ['#','X','O','X','X','O',' ',' ','O',' ']
        marker = 'O'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_1_4_7(self):
        self.board.board = ['#','X','O',' ','X','O',' ','X',' ',' ']
        marker = 'X'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_3_6_9(self):
        self.board.board = ['#','X',' ','O','X','X','O',' ',' ','O']
        marker = 'O'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_1_5_9(self):
        self.board.board = ['#','X',' ','O','O','X','O',' ',' ','X']
        marker = 'X'
        self.assertEqual(self.board.win_check(marker), True)

    def test_win_check_3_5_7(self):
        self.board.board = ['#','X',' ','O','X','O',' ','O',' ',' ']
        marker = 'O'
        self.assertEqual(self.board.win_check(marker), True)

### Place Market Tests
    def test_place_marker_board_updated_correctly(self):
        self.board.board = ['#','X',' ','O','X','O',' ','O',' ',' ']
        marker = 'X'
        position = 2
        self.board.place_marker(marker, position)
        self.assertEqual(self.board.board[2], 'X')

    def test_place_marker_index_out_of_range_error(self):
        self.board.board = ['#','X',' ','O','X','O',' ','O',' ',' ']
        marker = 'X'
        position = 11
        self.assertEqual(self.board.place_marker(marker, position), "Index out of range error")



### TearDown
    def tearDown(self):
        del self.board


if __name__ == "__main__":
    unittest.main()
