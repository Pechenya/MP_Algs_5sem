class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def main():
    q = Queue()
    a = list(map(float, input("Введите элементы очереди: ").split(' ')))
    for value in a:
        q.enqueue(value)
    print(q.size())
    print(q.dequeue())
    print(q.size())

if __name__ == '__main__':
    main()