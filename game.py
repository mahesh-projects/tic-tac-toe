import random
from board import Board

winning_combination = [(1,2,3), (2,5,8), (4,5,6), (1,4,7), (3,6,9),
                        (7,8,9), (1,5,9), (3,5,7)]

#Display board using print function
# def display_board(board):
#     i = 9
#     while i > 1:
#         print("  {} |  {} |  {} ".format(board[i-2], board[i-1], board[i]))
#         i -= 3

#Take a player input and assign the marker as X or O
def player_input():
    while True:
        marker = input("Please pick a marker 'X' or 'O': ").upper()
        if marker == 'X' or marker == 'O':
            return marker

#Given a board, marker and position, Assign the marker to position
# def place_marker(board, marker, position):
#     if (marker == 'X' or marker == 'O'):
#         if position in range(1,10):
#             board[position] = marker
#         else:
#             print("Position can be an integer from 1 to 9")
#     else:
#         print("Please pick a marker as 'X' or 'O': ")

#Given a board and a mark check whether the mark has won
# def win_check(board, mark):
#     if mark in board:
#         mark_at_indices = [i for i, x in enumerate(board) if x == mark]
#         #print(mark_at_indices)
#         for comb in winning_combination:
#             if set(comb).issubset(set(mark_at_indices)):
#                 return True

#Randomly decide which player goes first
def choose_first():
    player = random.randint(1,2)
    return "{}".format(player)

#Check if a space on board is available
def space_check(board, position):
    if len(board) <= 10 and board[position] == " ":
        return True
    else:
        return False

#Check if the board is full
# def full_board_check(board):
#     if len(board) == 10 and len([i for i in board if i == ' ']) == 0:
#         return True
#     else:
#         return False

#Take position as input and check if it is free
def player_choice(board):
    while True:
        try:
            position = int(input("Please pick a number from 1 to 9: "))
            if position in range(1, 10):
                if board.space_check(position):
                    return position
                else:
                    print("Position is not available for use.")
                    continue
        except:
            print("Position should be a number from 1 to 9")

#Check if the players want to replay
def replay():
    while True:
        decision = input("Press Y to play again or N to exit: ")
        if decision.upper() == 'Y':
            return True
        elif decision.upper() == 'N':
            return False

if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    while True:
        # Set the game up here
        # board = ['#'] #Make 0th element as # to simplify mapping user input to board indices
        #
        # for i in range(1,10): #Create an empty board with 9 blank elements
        #     board.append(" ")

        board = Board()
        board.display_board() #Display an empty board

        first_player = choose_first() #Randomly pick which player goes first
        print(f"Player #{first_player} will start")

        first_player_marker = player_input()
        second_player_marker = ''
        if first_player_marker == 'X':
            second_player_marker = 'O'
        else:
            second_player_marker = 'X'
        marker = first_player_marker

        #If board is not full, then continue playing
        while not board.full_board_check():
            print('game on')
            if board.win_check('X'): #Break if player with X mark has won
                print("Player with 'X' marker won!")
                break
            elif board.win_check('O'): #Break if player with O mark has won
                print("Player with 'O' marker won!")
                break
            #Player 1's Turn
            elif marker == first_player_marker:
                print("First Player's turn")
                #position = int(input("Please pick a number from 1 to 9: "))
                position = player_choice(board)
                board.place_marker(first_player_marker, position)
                marker = second_player_marker
            # Player 2's turn
            else:
                print("Second Player's turn")
                position = player_choice(board)
                board.place_marker(second_player_marker, position)
                marker = first_player_marker

            board.display_board()

        if not replay():
            break
