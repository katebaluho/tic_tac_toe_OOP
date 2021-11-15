import os

from settings import LOG_FOLDER

MODES = ('COMP', "USER")
END_GAME = ('Y', 'N')

NAMES = (
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
)

BOARD_SIZE = 3

DELIMETER = "|"

FILE_HANDLERS = {
    "GAME_NUM": os.path.join(LOG_FOLDER, "game_num_inc"),
    "INIT_GAME": os.path.join(LOG_FOLDER, "game_init"),
    "GAME_STEP": os.path.join(LOG_FOLDER, "game_log"),
    "END_GAME": os.path.join(LOG_FOLDER, "end_game"),
}