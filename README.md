# TicTacToe

Github repository for the game of Tic Tac Toe.

The following rules are implemented

    1. Computer is always 'O' and player is always 'X' 
    2. Computer always makes the first move and player the next.
    3. Computers first move is from a random move amongst the possible combinations in the moves param


The logic block that drives the approach of the computer game play
Logic:
1. If the computer can take one of the positions that can help it win go for it. This is done by trying all the possible board positions
2. If there is no move that can achieve that, check and interrupt the players win possibility
3. If none of the above scenarios are possible, generate a move from the list of options available in global param
moves

Note:
- The game begins with the computer making the first move and the game then continues with user.
- the first move of the computer is a random move from the list of possible moves.