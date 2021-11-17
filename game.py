from itertools import cycle
from os import path

from logger import Logger

class TicTacToe():

    def __init__(self, users , board):
        self.users = users
        self.board = board

    @Logger.to_file("STEP_GAME")
    def step_player(self, player, step_num):
        while True:
            try:
                print(f"Ход {step_num} игрока {player.name}")
                step = player.get_step(self.board)
                self.board.add_step(step, player.symbol)
                print(self.board)
                break
            except ValueError:
                print("Сюда ходить нельзя")
                continue
        return step


    def match_game(self, player, step_num):
        if self.board.chek_board():
            print(f"Победил игрок {player.symbol} : {player.name}")
            return player.name
        if self.board.chek_draw(step_num):
            print(f"Итог игры НИЧЬЯ")
            return "DRAW"
        return None

    def run(self):
        #names = [el.name for el in self.users]
       # self.logger.log_message("INIT_GAME", self.round, self.mode, *names,datetime.now().ctime())

        print(self.board)
        for step_num, player in enumerate(cycle(self.users),1):
            step = self.step_player(player, step_num)
           # self.logger.log_message("GAME_STEP", self.round, player.name, step_num, *step)

            result_game = self.match_game(player, step_num)
            if result_game:
                #self.logger.log_message("END_GAME", self.round, player.name, result_game)
                return result_game
