class Board():
    PLACEHOLDER = " "
    def __init__(self):
        self.board = self.__create_empty_board()
        #Keep winning combination a private attribute
        self.__winning_combination = [(1,2,3), (2,5,8), (4,5,6), (1,4,7), (3,6,9),
                                (7,8,9), (1,5,9), (3,5,7)]

    #Creating an empty board is a private method
    def __create_empty_board(self):
        board = ["#"]
        for i in range(1,10): #Create an empty board with 9 blank elements
            board.append(self.PLACEHOLDER)
        return board

    #Display the board
    def display_board(self):
        board_as_str = ''
        for i in range(9,1,-3):
            board_as_str += ''.join("  {} |  {} |  {}{}".format(self.board[i-2], self.board[i-1], self.board[i], "\n"))
        return board_as_str

    #Given a player's choice of position check if it is available for use
    def space_check(self, position):
        return self.board[position] == self.PLACEHOLDER

    #Check if the board is full
    def full_board_check(self):
        return len([i for i in self.board if i == self.PLACEHOLDER]) == 0

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
