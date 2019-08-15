class CustomQueue:
    """カスタムキュークラス"""

    def __init__(self, maxsize):
        self.queue = [] #FIFO
        self.maxsize = maxsize


    def enqueue(self, item):
        """キューの末尾に要素を追加.
        キューが最大サイズに達しているときは、デキューした後、エンキューする.
        """
        dequeue_item = ""
        if self.full():
            dequeue_item = self.dequeue()        
        self.queue.append(item)

        return dequeue_item


    def dequeue(self):
        """キューの先頭の要素を取得&削除."""
        return self.queue.pop(0)


    def full(self):
        """キューが最大サイズに達している."""
        return len(self.queue) == self.maxsize


    def join_queue_string(self):
        """キュー内の文字を連結."""
        return "".join(self.queue)
