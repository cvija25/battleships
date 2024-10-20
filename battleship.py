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
import random

class Board():
    __slots__ = ('__size','__num_of_ships','__outside_fields','__inside_fields','__fields_with_ship')
    
    def __init__(self,size,num_of_ships):
        self.__size = size
        self.__num_of_ships = num_of_ships
        self.__outside_fields = [['o' for _ in range(size)] for _ in range(size)]
        self.__inside_fields = [[0 for _ in range(size)] for _ in range(size)]
        self.gen_inside_fields()
        self.__fields_with_ship = size*size - sum([list.count(0) for list in self.__inside_fields])

    def gen_inside_fields(self):
        num_of_horizontal = 0
        num_of_vertical = 0

        for _ in range(self.__num_of_ships):
            if random.random() < 0.5:
                num_of_horizontal += 1
            else:
                num_of_vertical += 1

        rows = random.sample(range(self.__size), num_of_horizontal)
        for row in rows:
            start = random.randrange(self.__size - 3 + 1)
            for j in range(start,start + 3):           
                self.__inside_fields[row][j] = 1

        possible_columns = list(range(self.__size))
        while num_of_vertical:
            column = random.choice(possible_columns)
            possible_columns.remove(column)
            space = 0
            for i in range(self.__size):
                if self.__inside_fields[i][column] == 0:
                    space += 1
                else:
                    space = 0
                if space == 3:
                    self.__inside_fields[i-2][column] = 2
                    self.__inside_fields[i-1][column] = 2
                    self.__inside_fields[i][column] = 2
                    space = 0
                    num_of_vertical -= 1
                    break

    def print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print(self.__outside_fields[i][j], end = ' ')
            print()
    
    def update(self,guess_row,guess_col):
        if self.__inside_fields[guess_row][guess_col] == 0:
            self.__outside_fields[guess_row][guess_col] = '-'
            print("Miss!")
        else:
            self.__outside_fields[guess_row][guess_col] = 'X'
            self.__fields_with_ship -= 1
            print("Hit!")
    
    def check_win(self):
        return self.__fields_with_ship == 0
    
    def check_valid_guess(self, guess_row, guess_col):
        if guess_row > self.__size or guess_row < 0 or guess_col > self.__size:
            return False
        if self.__outside_fields[guess_row][guess_col] != 'o':
            return False
        return True
    
def play():
    num_ships = 4
    size = 7
    board = Board(size,num_ships)
    num_turns = 20
    winner = False
    for turn in range(num_turns):
        print(f"Turn {turn + 1} / {num_turns}")
        board.print()
        guess_row = int(input("Guess row:"))
        guess_col = int(input("Guess col:"))
        if not board.check_valid_guess(guess_row,guess_col):
            print("Bad guess, try again!")
            continue
        board.update(guess_row,guess_col)
        if board.check_win():
            winner = True
            break

    if winner:
        print("Congratulations you win the game")
    else:
        print("You lose the game")

import requests

def send():
    res = requests.post('http://127.0.0.1:8000/move', json={"x":1, "y":1})
    print(res.json())

if __name__ == '__main__':
    send()