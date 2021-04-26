
gBoard = [str(x) for x in range(9)]
Board = [' ' for x in range(9)]
P1 = 'X'
P2 = 'O'

def printBoard(Board):
    print(" "+Board[0]+" | "+Board[1]+" | "+Board[2]+" ")
    print("---|---|---")
    print(" "+Board[3]+" | "+Board[4]+" | "+Board[5]+" ")
    print("---|---|---")
    print(" "+Board[6]+" | "+Board[7]+" | "+Board[8]+" ")

def move(turn):
    pos = int(input("Player {} choose the position (0-8): ".format(str(turn%2+1))))
    if pos > 8:
        print("WARNING!!! Position greater than 8, try another one from 0 to 8...")
        move(turn)
    else:
        if Board[pos] != " ":
            print("WARNING!!! Position already occupied, try another one...")
            move(turn)
        else:
            Board[pos] = globals()['P{}'.format(turn%2+1)]

def check(turn):
    #vincitore
    if ( #rows
        (Board[0] == Board[1] and Board[1] == Board[2] and Board[0] != ' ') or
        (Board[3] == Board[4] and Board[4] == Board[5] and Board[3] != ' ') or
        (Board[6] == Board[7] and Board[7] == Board[8] and Board[6] != ' ') or
        #columns
        (Board[0] == Board[3] and Board[3] == Board[6] and Board[0] != ' ') or
        (Board[1] == Board[4] and Board[4] == Board[7] and Board[1] != ' ') or
        (Board[2] == Board[5] and Board[5] == Board[8] and Board[2] != ' ') or
        #diag
        (Board[0] == Board[4] and Board[4] == Board[8] and Board[0] != ' ') or
        (Board[2] == Board[4] and Board[4] == Board[6] and Board[2] != ' ')):
        
        print("Player {} is the winner!!!".format(str(turn%2+1)))
        return True

    return False

def main():
    print("#################\n### TICTACTOE ###\n#################")
    printBoard(gBoard)
    print("INSTRUCTIONS: Each turn choose a position from 0 to 8, as shown above")
    turn = 0
    win = False
    while win != True:
        printBoard(Board)
        move(turn)
        win = check(turn)
        turn += 1

main()