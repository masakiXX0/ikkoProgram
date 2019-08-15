from queue import Queue

class CustomQueue(Queue):
    def __init__(self, maxsize):
        super().__init__(maxsize)