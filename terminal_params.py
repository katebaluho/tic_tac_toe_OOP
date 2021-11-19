import sys
from constants import MODES

HELP_STRING = ["HELP", "help", "h", "-h"]

TERMINAL_PARAMS = {
    "mode" : None,
    "users": None
}

def help():
    print("""   Привет, желающий поиграть в ИГРУ.
                Для запуска игры в терминале, можешь ввести:
                Игра с человеком: python main.py USER Имя Имя
                Игра с компом: python main.py COMP Имя
                Если введешь не верно - программа предложит выбрать режим игры и ввести имя .
                Ты можешь вернуться к подсказке, вызвав команды ["HELP", "help", "h", "-h"] """)
    exit(0)


def read_terminal():
    try:
        param = sys.argv[1]
        if param in MODES:
            TERMINAL_PARAMS['mode'] = param
        elif param in HELP_STRING:
            help()
        else:
            raise IndexError
    except IndexError:
        pass

    if not TERMINAL_PARAMS['mode']: return None

    try:
        if TERMINAL_PARAMS['mode'] == MODES[1] and len(sys.argv[2:]) < 2:
            raise IndexError
        TERMINAL_PARAMS['users'] = sys.argv[2:]
    except IndexError:
        pass