# =======================================================================
# |             Created by:                                             |
# |                 Adil Sheikh     (FA21-BCT-002)                      |
# |                 Waseeq Kayani   (FA21-BCT-021)                      |
# =======================================================================

import random

def welcomeMessage():
    print('================| Welcome to the Tic Tac Toe |================')
    print()
    print('Player 1: X')
    print('Player 2: O')

def toss():
    print('\n===========================| Toss |===========================')
    print('Player 1. Select:\n(1) Heads\n(2) Tails')
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
        print('* Player 1 won the toss!')
        return 1
    else:
        print('* Player 2 won the toss')
        return 2

def printBoard(board):
    print('\n\t-------')
    for row in board:
        print('\t ', end='')
        for col in row:
            print(col, end=' ')
        print()
    print('\t-------\n')

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

def checkWin(board):
    pass

def game(firstTurn):
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
            move = int(input('Player 1\'s Turn: '))
        elif currentMove == 'O':
            move = int(input('Player 2\'s Turn: '))
        
        if move not in validMoves(board):
            print('* Invalid Move!')
            continue

        makeMove(move, currentMove, board)

        if currentMove == 'X':
            currentMove = 'O'
        elif currentMove == 'O':
            currentMove = 'X'
    else:
        printBoard(board)
        print('* The game was a draw!')

def main():
    welcomeMessage()
    firstTurn = toss()
    game(firstTurn)

main()