from settings import SESSION_COUNT

class SessionMixin:

    def get_prev_session(self):
        prev_session = None
        try:
            with open(SESSION_COUNT, 'r', encoding="UTF-8") as file:
                prev_session = file.read(1)
        except FileNotFoundError:
            return None
        except Exception:
            print("Ошибка чтения файла")
            return None
        return prev_session


    def update_session(self):
        prev_session = int(0 if not self.get_prev_session() else self.get_prev_session())
        try:
            with open(SESSION_COUNT, 'w', encoding="UTF-8") as file:
                new_session = prev_session + 1
                file.write(str(new_session))
        except Exception:
            print("Ошибка обновления файла")
            return None
        return new_session