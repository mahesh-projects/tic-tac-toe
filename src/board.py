PLACEHOLDER = " "
class Board():

    def __init__(self):
        self.board = self.__create_empty_board()
        #Keep winning combination a private attribute
        self.__winning_combination = [(1,2,3), (2,5,8), (4,5,6), (1,4,7), (3,6,9),
                                (7,8,9), (1,5,9), (3,5,7)]

    #Creating an empty board is a private method
    def __create_empty_board(self):
        board = ["#"]
        for i in range(1,10): #Create an empty board with 9 blank elements
            board.append(PLACEHOLDER)
        return board

    #Display the board
    def display_board(self):
        i = 9
        while i > 1:
            print("  {} |  {} |  {} ".format(self.board[i-2], self.board[i-1], self.board[i]))
            i -= 3

    #Given a player's choice of position check if it is available for use
    def space_check(self, position):
        if self.board[position] == PLACEHOLDER:
            return True
        else:
            return False

    #Check if the board is full
    def full_board_check(self):
        if len(self.board) == 10 and len([i for i in self.board if i == PLACEHOLDER]) == 0:
            return True
        else:
            return False

    #Check if a given marker has won based on __winning_combination
    def win_check(self, marker):
        if marker in self.board:
            marker_at_indices = [i for i, x in enumerate(self.board) if x == marker]
            #print(marker_at_indices)
            for comb in self.__winning_combination:
                if set(comb).issubset(set(marker_at_indices)):
                    return True

    #Given a marker and position, Assign the marker to position on board
    def place_marker(self, marker, position):
        try:
            self.board[position] = marker
        except IndexError:
            return "Index out of range error"
