#Head to Head tic-tac-toe

def draw_board(board):
    print("\t\t Tic-Tac-Toe ")

    print('\t\t||',board[0],'||',board[1],'||',board[2],'||')
    print('\t\t||',board[3],'||',board[4],'||',board[5],'||')
    print('\t\t||',board[6],'||',board[7],'||',board[8],'||')
    
#gets player to input position
def get_player_input(board, player_char):    
    while True:
        player_move = int(input( "Enter position you'd like to play (1-9):\t"))
        if player_move > 0 and player_move < 10 : 
            if board[player_move - 1] == '_':
                return player_move
            else:
                print("\nSorry, that position has already been taken.")
        else:
            print("\nSorry, your move is not on the board.")


def place_char_on_board(board, player_move, player_char):
    board[player_move-1] = (player_char)

#Checks arrangement of players characters to determine winner
def is_winner(board, player_char):
    if  board[0] == player_char and board[1] == player_char  and board[2] == player_char:
        return True
    elif board[3] == player_char and board[4] == player_char and board[5] == player_char:
        return True
    elif board[6] == player_char and board[7] == player_char and board[8] == player_char:       
        return True
    elif board[0] == player_char and board[3] == player_char and board[6] == player_char:    
        return True
    elif board[1] == player_char and board[4] == player_char and board[7] == player_char:  
        return True
    elif board[2] == player_char and board[5] == player_char and board[8] == player_char:      
        return True
    elif board[0] == player_char and board[4] == player_char and board[8] == player_char:
        return True
    elif board[2] == player_char and board[4] == player_char and board[6] == player_char:
        return True
    else:
        return False 


player_1 = 'X'
player_2 = 'O'

c_list = ['_']*9
n_list = ['1', '2', '3', '4', '5', '6', '7', '8','9']

draw_board(n_list)
print("\n\n")
draw_board(c_list)

while True:
    #player 1
    print(player_1)
    player_move = get_player_input(c_list, player_1 )
    place_char_on_board(c_list, player_move, player_1) 
    draw_board(n_list)
    draw_board(c_list)
    x = is_winner(c_list, player_1)
    if x == True:
        print("Player 1 wins.")
        break
    elif '_' not in c_list:
        print("Game was a tie.")
        break

    #player 2
    print(player_2)
    player_move = get_player_input(c_list, player_2)
    place_char_on_board(c_list, player_move, player_2)
    draw_board(n_list)
    draw_board(c_list)

    x = is_winner(c_list, player_2)
    if x == True:
        print("Player 2 wins.")
        break








