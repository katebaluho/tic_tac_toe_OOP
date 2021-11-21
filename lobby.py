from SessionMixin import SessionMixin
from terminal_params import TERMINAL_PARAMS, read_terminal
from board import Board
from constants import MODES, BOARD_SIZE, END_GAME
from game import TicTacToe
from player import Gamer, Player

import logger

log = logger.get_logger(__name__)
read_terminal()

class Lobby(SessionMixin):

    def __init__(self, session = 0, mode = None, users = None, round = 1, game_name = TicTacToe):
        self.session = session if session else self.update_session()
        self.mode = self.get_mode(mode)
        self.users = self.get_users(users)
        self.board = Board(BOARD_SIZE)
        self.round = round
        self.game = game_name(self.users, self.board)
        log.info(f'Session #{self.session} - round #{self.round} - MODE {self.mode}')

    def get_users(self, users):
        if users:
            return users
        users = TERMINAL_PARAMS['users']
        if users:
            return (Gamer('X', users[0]), Gamer('O', users[1])) if self.mode == MODES[1] else (Gamer('X', users[0]), Player('O'))
        return (Gamer('X'), Gamer('O')) if self.mode == MODES[1] else (Gamer('X'), Player('O'))


    def get_mode(self, mode):
        if mode:
            return mode

        if TERMINAL_PARAMS['mode']:
            return TERMINAL_PARAMS['mode']

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


    def get_restart(self):
        while True:
            user_answer = input(f'Начать новую игру? {END_GAME}')
            if not user_answer.upper() in END_GAME:
                print("Неверный выбор.Попробуйте еще раз.")
            else:
                return True if user_answer.upper() == END_GAME[0] else False


    def params_for_restart(self):
        return (self.session, self.mode, self.users, self.round+1)


if __name__ == '__main__':
    def game():
        restart = True
        new_game = Lobby()
        while restart:
            new_game.game.run()
            restart = new_game.get_restart()
            if restart:
                new_game = Lobby(*new_game.params_for_restart())

game()