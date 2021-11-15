import os

LOG_FOLDER = os.path.join(os.path.dirname(__file__), "game_logs")
if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)