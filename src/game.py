import random
from board import Board

#Take a player input and assign the marker as X or O
def player_input():
    while True:
        marker = input("Please pick a marker 'X' or 'O': ").upper()
        if marker == 'X' or marker == 'O':
            return marker

#Randomly decide which player goes first
def choose_first():
    player = random.randint(1,2)
    return "{}".format(player)

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
        board = Board()
        print(board.display_board()) #Display an empty board

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
            #print('game on')
            if board.win_check('X'): #Break if player with X marker has won
                print("Player with 'X' marker won!")
                break
            elif board.win_check('O'): #Break if player with O marker has won
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

            print(board.display_board())

        if not replay():
            break
