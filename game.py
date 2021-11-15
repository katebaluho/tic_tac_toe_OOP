from itertools import cycle
from datetime import datetime

from board import Board
from constants import MODES, END_GAME, BOARD_SIZE
from logger import Logger
from  player import Gamer, Player


class Game():

    def __init__(self, logger = Logger(), mode = None, users = None, round = 1):
        self.mode = self.get_mode(mode)
        self.users = self.get_users(users)
        self.board = Board(BOARD_SIZE)
        self.logger = logger
        self.round = round


    def get_users(self, users):
        if users:
            return users
        return (Gamer('X'), Gamer('O')) if self.mode == MODES[1] else (Gamer('X'), Player('O'))


    def get_mode(self, mode):
        if mode:
            return mode

        user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}
        modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
        modes_string = f"Выберите номер режима игры\n{modes_str}\n>>>"

        while True:
            try:
                mode_input = int(input(modes_string))
                return user_modes[mode_input]
            except ValueError:
                print("Недопустимый ввод, введите только число")
            except KeyError:
                print("Недопустимое значение, повторите ввод")
            continue


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


    def get_restart(self):
        while True:
            user_answer = input(f'Начать новую игру? {END_GAME}')
            if not user_answer.upper() in END_GAME:
                print("Неверный выбор.Попробуйте еще раз.")
            else:
                return True if user_answer.upper() == END_GAME[0] else False


    def game_cycle(self):
        names = [el.name for el in self.users]
        self.logger.log_message("INIT_GAME", self.round, self.mode, *names,datetime.now().ctime())

        print(self.board)
        for step_num, player in enumerate(cycle(self.users),1):
            step = self.step_player(player, step_num)
            self.logger.log_message("GAME_STEP", self.round, player.name, step_num, *step)

            result_game = self.match_game(player, step_num)
            if result_game:
                self.logger.log_message("END_GAME", self.round, player.name, result_game)
                return result_game


    def params_for_restart(self):
        return (self.logger, self.mode, self.users, self.round+1)


if __name__ == '__main__':
    def game():
        restart = True
        new_game = Game()
        while restart:
            new_game.game_cycle()
            restart = new_game.get_restart()
            if restart:
                new_game = Game(*new_game.params_for_restart())

game()