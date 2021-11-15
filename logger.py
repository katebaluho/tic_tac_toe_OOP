from constants import DELIMETER, FILE_HANDLERS


class Logger():

    def __init__(self, now_session = None):
        self.prev_session = int(0 if not self.get_prev_session('GAME_NUM') else self.get_prev_session('GAME_NUM'))
        self.now_session = self.update_session('GAME_NUM')


    def get_prev_session(self, handler):

        prev_session = None
        try:
            with open(FILE_HANDLERS[handler], 'r', encoding="UTF-8") as file:
                prev_session = file.read(1)
        except FileNotFoundError:
            return None
        except Exception:
            print("Ошибка чтения файла")
            return None
        return prev_session


    def update_session(self, handler):
        try:
            with open(FILE_HANDLERS[handler], 'w', encoding="UTF-8") as file:
                new_session = self.prev_session + 1
                file.write(str(new_session))
        except Exception:
            print("Ошибка обновления файла")
            return None
        return new_session


    def logging_in_file(func):
        def wrapper(self, *args):
            message = func(self, *args)
            try:
                print('handler', args[0])
                with open(FILE_HANDLERS[args[0]], mode='a', encoding="UTF-8") as file:
                    file.write(message)
            except IOError:
                print("ОШИБКА ЗАПИСИ ЛОГА")
            return message
        return wrapper

    @logging_in_file
    def log_message(self, *args):
        session = str(self.now_session)+DELIMETER
        message = session + DELIMETER.join(map(str, args[1:])) + '\n'
        return message




