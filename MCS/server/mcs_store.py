
class storage():
    def __init__(self):
        self._message = "empty"

    def get_message(self):
        return self._message

    def store_message(self,message):
        self._message = message