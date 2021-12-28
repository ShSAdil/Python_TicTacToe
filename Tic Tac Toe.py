# =======================================================================
# |             Created by:                                             |
# |                 Adil Sheikh     (FA21-BCT-002)                      |
# |                 Waseeq Kayani   (FA21-BCT-021)                      |
# =======================================================================

import random

def welcomeMessage():
    print('================| Welcome to the Tic Tac Toe |================')
    print()
    print('Player: X')
    print('Computer: O')

def toss():
    print('\n===========================| Toss |===========================')
    print('Player. Select:\n(1) Heads\n(2) Tails')
    coin = int(input(': '))

    if coin not in [1, 2]:
        print('Please select a valid option.')
        return toss()

    win = random.randint(1, 2)

    if win == 1:
        print('\nIt was Heads!')
    elif win == 2:
        print('\nIt was Tails!')

    if coin == win:
        print('* Player won the toss!')
        return 1
    else:
        print('* Computer won the toss')
        return 2

def printBoard(board):
    print('\n\t-------------')
    for row in board:
        print('\t| ', end='')
        for col in row:
            print(col, end=' | ')
        print('\n\t-------------')
    print()

def validMoves(board):
    moves = []

    count = 1
    for row in board:
        for col in row:
            if col == '-':
                moves.append(count)
            count += 1

    return moves

def makeMove(move, currentMove, board):
    count = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            if count == move:
                board[x][y] = currentMove
            count += 1

def computerMove(board):
    print('Computer making a move...')

    bestScore = -101
    bestMove = 0

    count = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == '-':
                board[x][y] = 'O'
                score = findBestMove(board, False)
                board[x][y] = '-'
                if score > bestScore:
                    bestScore = score
                    bestMove = count
            count += 1

    return bestMove

def findBestMove(board, isPlayer):
    if checkWin(board)[1] == 1:
        return -100
    elif checkWin(board)[1] == 2:
        return 100
    elif checkDraw(board):
        return 0

    if isPlayer:
        bestScore = -101

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == '-':
                    board[x][y] = 'O'
                    score = findBestMove(board, False)
                    board[x][y] = '-'
                    if score > bestScore:
                        bestScore = score

        return bestScore

    else:
        bestScore = 101

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == '-':
                    board[x][y] = 'X'
                    score = findBestMove(board, True)
                    board[x][y] = '-'
                    if score < bestScore:
                        bestScore = score

        return bestScore

def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False

    return True

def checkWin(board):
    for x in range(len(board)):
        prev = board[x][0]
        current = ''
        if prev != '-':
            for y in range(1, len(board)):
                current = board[x][y]
                if current != prev or current == '-':
                    break
                prev = current
            else:
                return True, 1 if current == 'X' else 2

    for x in range(len(board)):
        prev = board[0][x]
        current = ''
        if prev != '-':
            for y in range(1, len(board)):
                current = board[y][x]
                if current != prev or current == '-':
                    break
                prev = current
            else:
                return True, 1 if current == 'X' else 2

    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    for diagonal in diagonals:
        prev = board[diagonal[0][0]][diagonal[0][1]]
        current = ''
        for cell in diagonal:
            x, y = cell
            current = board[x][y]
            if prev != current or current == '-':
                break
            prev = current
        else:
            return True, 1 if current == 'X' else 2

    return False, -1

def game(firstTurn):
    print('\n===========================| Game |===========================')

    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    if firstTurn == 1:
        currentMove = 'X'
    elif firstTurn == 2:
        currentMove = 'O'

    while len(validMoves(board)) > 0:
        printBoard(board)
        print('Valid moves remaining:', validMoves(board))

        if currentMove == 'X':
            move = int(input('Player\'s Turn: '))
        elif currentMove == 'O':
            move = computerMove(board)
        
        if move not in validMoves(board):
            print('* Invalid Move!')
            continue

        makeMove(move, currentMove, board)

        won, player = checkWin(board)

        if won:
            printBoard(board)
            if player == 1:
                print('* Congratulations! Player won!')
            else:
                print('* Computer won! Try Again!')
            break

        if currentMove == 'X':
            currentMove = 'O'
        elif currentMove == 'O':
            currentMove = 'X'
    else:
        printBoard(board)
        print('* The game was a draw!')

def main():
    welcomeMessage()

    play = True

    while play:
        firstTurn = toss()
        game(firstTurn)

        playAgain = input('\nPress "y" to play another game: ')
        if playAgain not in ['y', 'Y']:
            play = False

main()
