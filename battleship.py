# python battleship.py

from random import randint

#Make board
board = []
for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row +1
print ship_col +1


def battleship():
    hit = False
    turn = 1
    while hit == False:
        print "Turn: ", turn
        guess_row = int(raw_input("Guess Row:")) -1
        guess_col = int(raw_input("Guess Col:")) -1
        if guess_row not in range(5) or guess_col not in range(5): 
            print "Oops, that's not even in the ocean."
            print_board(board)
        elif board[guess_row][guess_col] == "X":
                print "You guessed that one already."
                print_board(board)
        else:
            if guess_row == ship_row and guess_col == ship_col:
                print "Congratulations! You sank my battleship!"
                hit = True
            else: 
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                print_board(board)
        turn += 1

                
battleship()
