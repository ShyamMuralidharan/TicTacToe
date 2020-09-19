import random


def print_board():
    """
    function to print the current board state
    """
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1: end += '---------\n';
        char = ' '
        if i in ('X', 'O'): char = i;
        x += 1
        print(char, end=end)


def select_char():
    """create random assignment of user"""
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, player, move) -> bool:
    """
    :param brd: current board state
    :param player: current player
    :param move: current move

    function to check whether a move can be attempted
    """
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


def can_win(brd, player, move) -> bool:
    """
    :param brd: current board state
    :param player: current player - Computer or Human
    :param move: move being attempted

    functions to check whether the current player can win or has won
    """
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


def make_move(brd, player, move, undo=False) -> tuple:
    """
    :param brd: current board state
    :param player: the player who is making the move
    :param move: curent move being attempted to be validated
    :param undo: to cancel the current move

    function will return whether a move can be made, returns a boolean value
    """
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


# AI goes here
def computer_move(move_posn, computer, player):
    """
    :param move_posn: Move position to indicate whether the first move must be random
    :param computer: value of the computer name
    :param player: value of the player name

    The logic block that drives the approach of the computer game play
    Logic:
    1. If the computer can take one of the positions that can help it win go for it. This is done by trying all the
    possible board positions
    2. If there is no move that can achieve that, check and interrupt the players win possibility
    3. If none of the above scenarios are possible, generate a move from the list of options available in global param
    moves

    Note:
    - The game begins with the computer making the first move and the game then continues with user.
    - the first move of the computer is a random move from the list of possible moves.
    """
    move = -1
    # If I can win, others don't matter.
    for i in range(1, 10):
        if i == 1:
            random_num = random.randint(0,9)
            if make_move(board, computer, random_num, True)[1]:
                move = i
                break
        else:
            if make_move(board, computer, i, True)[1]:
                move = i
                break
    if move == -1:
        # If player can win, block him.
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        if move_posn == 0:
            move_tup = random.choice(moves)
            mv = random.choice(move_tup)
            if move == -1 and can_move(board, computer, mv):
                move = mv
        else:
            for tup in moves:
                for mv in tup:
                    if move == -1 and can_move(board, computer, mv):
                        move = mv
                        break
    return make_move(board, computer, move)


def space_exist() -> bool:
    """
    check if the board has spaces that can be played
    """
    return board.count('X') + board.count('O') != 9


def game(board, moves, winners, tab):
    """
    :param board: the game state board
    :param moves: the possible moves that include centers and edges eg : moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
    :param winners: possible combinations of winners
    eg: winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    :param tab: The exact table which can be referenced for the position

    Function to initiate the game, defaults are the following:

    1. Computer is always 'O' and player is always 'X'
    2. Computer always makes the first move and player the next.
    3. Computers first move is from a random move amongst the possible combinations in the moves param
    """
    player, computer = "X", "O"
    result = '%%% Deuce ! %%%'
    print('Player is [%s] and computer is [%s]' % (player, computer))
    move_posn = 0
    while space_exist():
        if move_posn < 1:
            # make the computer do the first move
            print("Computer moves first !!!")
            computer_move(move_posn, computer, player)
        # Print board after the computer moves
        print_board()
        move_posn += 1
        print('# Make your move ! [1-9] : ', end='')
        move = int(input())
        moved, won = make_move(board, player, move)

        if not moved:
            print(' >> Invalid number ! Try again !')
            continue
        if won:
            print_board()
            result = '*** Congratulations ! You won ! ***'
            break
        elif computer_move(move_posn, computer, player)[1] and move_posn>1:
            print_board()
            result = '=== You lose ! =='
            break

    return result

if __name__ == "__main__":
    # This is a list comprehension method to create the board with a list of values
    board = [i for i in range(0, 9)]

    # Corners, Center and Others, respectively
    moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
    # Winner combinations
    winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # Table
    tab = range(1, 10)

    result = game(board, moves, winners, tab)
    fmt_string = "-------"* 10
    print(f"{fmt_string}\n\t\t\t\t\t\tRESULT !!!!\n{fmt_string}\n{result}")
