from itertools import cycle
import logger
log = logger.get_logger(__name__)

class TicTacToe():

    def __init__(self, users , board):
        self.users = users
        self.board = board


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
        result_game = ''
        if self.board.chek_board():
            result_game = f"Победил игрок {player.symbol} : {player.name}"
        if self.board.chek_draw(step_num):
            result_game = f"Итог игры НИЧЬЯ"
        return result_game

    def run(self):
        print(self.board)
        for step_num, player in enumerate(cycle(self.users),1):
            step = self.step_player(player, step_num)
            log.info(f'Игрок {player.name}. Ход {step}')
            result_game = self.match_game(player, step_num)
            if result_game:
                print(result_game)
                log.info(result_game)
                return result_game