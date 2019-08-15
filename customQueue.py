class CustomQueue:
    def __init__(self, maxsize):
        self.queue = [] #FIFO
        self.maxsize = maxsize

    # エンキュー
    def enqueue(self, item):
        if self.full():
            self.dequeue()        
        self.queue.append(item)

    # デキュー
    def dequeue(self):
        return self.queue.pop(0)

    # キューがいっぱい
    def full(self):
        if len(self.queue) == self.maxsize:
            return True
        return False
    
    # キュー内の文字を連結
    def join_queue_string(self):
        return "".join(self.queue)
