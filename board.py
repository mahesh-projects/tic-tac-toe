class Board():

    def __init__(self):
        self.board = self.__create_empty_board()

    #Creating an empty board is a private method
    def __create_empty_board(self):
        board = ["#"]
        for i in range(1,10): #Create an empty board with 9 blank elements
            board.append(" ")
        return board

    def display_board(self):
        pass

    def space_check(self):
        pass

    def full_board_check(self):
        pass
