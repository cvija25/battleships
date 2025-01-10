# import socket
# import os
# import dotenv
# dotenv.load_dotenv()

# import random

# class Board():
#     __slots__ = ('__size','__num_of_ships','__outside_fields','__inside_fields','__fields_with_ship')
    
#     def __init__(self,size,num_of_ships):
#         self.__size = size
#         self.__num_of_ships = num_of_ships
#         self.__outside_fields = [['o' for _ in range(size)] for _ in range(size)]
#         self.__inside_fields = [[0 for _ in range(size)] for _ in range(size)]
#         self.gen_inside_fields()
#         self.__fields_with_ship = size*size - sum([list.count(0) for list in self.__inside_fields])

#     def gen_inside_fields(self):
#         num_of_horizontal = 0
#         num_of_vertical = 0

#         for _ in range(self.__num_of_ships):
#             if random.random() < 0.5:
#                 num_of_horizontal += 1
#             else:
#                 num_of_vertical += 1

#         rows = random.sample(range(self.__size), num_of_horizontal)
#         for row in rows:
#             start = random.randrange(self.__size - 3 + 1)
#             for j in range(start,start + 3):           
#                 self.__inside_fields[row][j] = 1

#         possible_columns = list(range(self.__size))
#         while num_of_vertical:
#             column = random.choice(possible_columns)
#             possible_columns.remove(column)
#             space = 0
#             for i in range(self.__size):
#                 if self.__inside_fields[i][column] == 0:
#                     space += 1
#                 else:
#                     space = 0
#                 if space == 3:
#                     self.__inside_fields[i-2][column] = 2
#                     self.__inside_fields[i-1][column] = 2
#                     self.__inside_fields[i][column] = 2
#                     space = 0
#                     num_of_vertical -= 1
#                     break

#     def print(self):
#         for i in range(self.__size):
#             for j in range(self.__size):
#                 print(self.__outside_fields[i][j], end = ' ')
#             print()
    
#     def update(self,guess_row,guess_col):
#         if self.__inside_fields[guess_row][guess_col] == 0:
#             self.__outside_fields[guess_row][guess_col] = '-'
#             print("Miss!")
#         else:
#             self.__outside_fields[guess_row][guess_col] = 'X'
#             self.__fields_with_ship -= 1
#             print("Hit!")
    
#     def check_win(self):
#         return self.__fields_with_ship == 0
    
#     def check_valid_guess(self, guess_row, guess_col):
#         if guess_row > self.__size or guess_row < 0 or guess_col > self.__size:
#             return False
#         if self.__outside_fields[guess_row][guess_col] != 'o':
#             return False
#         return True

# num_ships = 4
# size = 7
# board = Board(size,num_ships)
# num_turns = 20
# winner = False

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.websocket('/ws')
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            print(f"Received: {data}")
            await websocket.send_json(data)

    except WebSocketDisconnect:
        print("Client disconnected")
