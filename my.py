board = {1: ' ', 2 : ' ', 3 : ' ',
         4: ' ', 5 : ' ', 6 : ' ',
         7: ' ', 8 : ' ', 9 : ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

printBoard(board)

def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False

def checkDraw():
    for key in board.keys() :
        if board[key] == ' ':
            return False
    return True
    
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1]!= ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4]!= ' '):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7]!= ' '):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1]!= ' '):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2]!= ' '):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9]!= ' '):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1]!= ' '):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3]!= ' '):
        return True
    else :
        return False

def checkWhichMarkWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] == mark):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1] == mark):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] == mark):
        return True
    else :
        return False


def insertLetter(letter, position):
    
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()) :
            print("Draw!")
            exit()
        
        if (checkForWin()):
            if letter == 'X':
                print("Bot Wins!")
                exit()
            else :
                print("Player Wins!")
                exit()
            
    else :
        print("Can't insert there!")
        position = int(input("Enter new position : "))
        insertLetter(letter,position)
        return 
    


def evaluate(board):
    if checkWhichMarkWon('X'):
        return 1
    elif checkWhichMarkWon('O'):
        return -1
    else:
        return 0

def minimax(board, depth, isMaximizing):
    score = evaluate(board)

    if score == 1:
        return score
    if score == -1:
        return score
    if checkDraw():
        return 0

    if isMaximizing:
        bestScore = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore

def bestMove():
    bestScore = -float('inf')
    move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                move = key
    return move

player = 'O'
bot = 'X'

def playerMove() :
    position = int(input("Enter the position for 'O' : "))
    insertLetter(player,position)
    return

def compMove() :
    position = bestMove()
    insertLetter(bot, position)
    return



while not checkForWin():
    playerMove()
    compMove()