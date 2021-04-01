from sweep_queue import Queue


class QueueManager:
    def __init__(self, queue):
        self.queue = ()

    def enqueue(self):
        print(f'enqueue from {self.queue}')

    def dequeue(self):
        print(f'dequeue from {self.dequeue}')
