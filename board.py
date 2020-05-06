class Board():

    def __init__(self):
        self.board = self.__create_empty_board()
        self.__winning_combination = [(1,2,3), (2,5,8), (4,5,6), (1,4,7), (3,6,9),
                                (7,8,9), (1,5,9), (3,5,7)]

    #Creating an empty board is a private method
    def __create_empty_board(self):
        board = ["#"]
        for i in range(1,10): #Create an empty board with 9 blank elements
            board.append(" ")
        return board

    def display_board(self):
        i = 9
        while i > 1:
            print("  {} |  {} |  {} ".format(self.board[i-2], self.board[i-1], self.board[i]))
            i -= 3

    def space_check(self, position):
        if len(self.board) <= 10 and self.board[position] == " ":
            return True
        else:
            return False

    def full_board_check(self):
        if len(self.board) == 10 and len([i for i in self.board if i == ' ']) == 0:
            return True
        else:
            return False


    def win_check(self, marker):
        if marker in self.board:
            marker_at_indices = [i for i, x in enumerate(self.board) if x == marker]
            print(marker_at_indices)
            for comb in self.__winning_combination:
                if set(comb).issubset(set(marker_at_indices)):
                    return True

    #Given a marker and position, Assign the marker to position on board
    def place_marker(self, marker, position):
        self.board[position] = marker


if __name__ == "__main__":
    board = Board()
    board.display_board(board)
