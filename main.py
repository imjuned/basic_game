#hello
#globL VriBKE

board=["-", "-", "-",
       "-" ,"-" ,"-",
       "-", "-", "-"]

game_still_going = True

#winner
winner =None

#turn
current_player='X'

#



def dis_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[6]+' | '+board[7]+' | '+board[8])

#dis_board()

def play_game():
    #initial display board22
    dis_board()
    #handle turn
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #game finished
    if winner=="X" or winner=='O':
        print(winner+" won .")
    elif winner==None:
        print(" Tie.")

def handle_turn(player):
    print(player+"'s turn")
    position=input("select from 1-9 :")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("select from 1-9 :")
        position=int(position)-1

        if board[position]=="-":
            valid=True
        else:
            print("You can't go there...!")
    board[position]=player

    dis_board()



def check_if_game_over():
    check_for_winner()
    check_if_tie()



def check_for_winner():
    global winner
    #rows
    row_winner=check_rows()
    
    #columns
    column_winner=check_column()


    #diagonals
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_rows():
    global game_still_going

    
    row_1=board[0]==board[1]==board[2] !='-'
    row_2=board[3]==board[4]==board[5] !='-'
    row_3=board[6]==board[7]==board[8] !='-'

    if row_1 or row_2 or row_3:
        game_still_going= False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    global game_still_going

    
    column_1=board[0]==board[3]==board[6] !='-'
    column_2=board[1]==board[4]==board[7] !='-'
    column_3=board[2]==board[5]==board[8] !='-'

    if column_1 or column_2 or column_3:
        game_still_going= False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going

    
    diagonal_1=board[0]==board[4]==board[8] !='-'
    diagonal_2=board[2]==board[4]==board[6] !='-'
    

    if diagonal_1 or diagonal_2:
        game_still_going= False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[1]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False

    return

def flip_player():
    global current_player
    if current_player== "X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return
play_game()
