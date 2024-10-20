"""
Simple Battleship Game

In our version of the game user is playing against the computer, trying to guess ships' location on the board.
The game board is a 7x7 square, where 'o' represents an unknown square,
'X' represents a ship, '-' represents a missed shot.
Ships in the amount of 4, each 3 squares long, are randomly located to the board before player starts guessing them.
Simple option is to use horizontal ships only. If you want some challenge, you can implement the option with
both horizontal and vertical ships. :)

The player has 20 turns to guess the location of the ships.
After each turn, the board is printed to the console, and the player is asked to enter the row and column
of their guess. If the guess hits a ship, the board is updated with a 'X' character at the corresponding position.
If the guess misses, the board is updated with a '-' character. A text corresponding to hit attempt result
should be printed: 'Hit!' or 'Miss!'.

If the player sinks all the ships before running out of turns, they win the game. The player looses otherwise.
At the end of the game, a text corresponding to game result should be printed.

Example:

Turn 1 / 15
o o o o o o
o o o o o o
o o o o o o
o o o o o o
o o o o o o
o o o o o o
Guess row: 0
Guess col: 1
Miss!         <--- message about hit result
...

Turn 2 / 15
o - o o o o   <--- updated position (0, 1) after 1st turn
o o o o o o
o o o o o o
o o o o o o
o o o o o o
o o o o o o
Guess row: 1
Guess col: 3
Miss!

Turn 9 / 15
o - o o o o
o o o - o o
o o o - - o
- o o - o -
- o o o o o
o o o o o o
Guess row: 4
Guess col: 3
Hit!

Turn 10 / 15
o - o o o o
o o o - o o
o o o - - o
- o o - o -
- o o X o o
o o o o o o
Guess row: 4
Guess col: 4
Hit!

...
You lose the game!   <--- message in the end of the game
"""
import socket
import dotenv
import os

dotenv.load_dotenv()

def play():
    clinet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = int(os.environ.get("PORT"))
    clinet_socket.connect((host, port))

    winner = False
    while not winner:
        guess_row = int(input("Guess row:"))
        clinet_socket.send(bytes(guess_row))
        guess_col = int(input("Guess col:"))
        clinet_socket.send(bytes(guess_col))
        winner = clinet_socket.recv()

    if winner:
        print("Congratulations you win the game")
    else:
        print("You lose the game")

if __name__ == '__main__':
    play()