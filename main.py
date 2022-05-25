from itertools import cycle
from itertools import combinations

def get_input():
    while True:
        try:
            return int(input('Enter a number: '))
        except ValueError:
            print('Invalid input. Try again...')

def draw_board(board):
    for i in range(9):
        print(board[i], end=' ')

        if(i % 3 == 0 and i != 8):
            print("\n" , '-' * 8)
        elif i != 9:
            print('|' , end=' ')


magic_square = [8, 1, 6, 3, 5, 7, 4, 9, 2]
n = 0
win = False
board = [' ' for x in range(9)]
hist = {'X': [], 'O': []}
player_turn = cycle(['X', 'O'])

while not win:

    #choose a tile to play
    player_input = get_input() - 1

    #check if input is valid
    if player_input > 9:
        print('Invalid input. Try again...')
        continue   

    #check if input is already taken
    if board[player_input] != ' ':
        print('Invalid input. Try again...')
        continue
    
    #record input and draw it on the board
    current_player = next(player_turn)
    hist[current_player].append(magic_square[player_input])
    board[player_input] = current_player

    #check for a winner
    if n >= 4:
        for each_list in combinations(hist[current_player], 3):
            if sum(each_list) == 15:
                print(f"Player {current_player} wins!!")
                win = True
                break
            
    n += 1
    draw_board(board)
    # print(board[0:3])
    # print(board[3:6])
    # print(board[6:9])