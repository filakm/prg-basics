import queue
number = int(input('enter number: '))
binary = queue.LifoQueue()
while number >0:
    b = number%2
    binary.put(b)
    number = number//2
while not binary.empty():
    bin = binary.get()
    print(bin, end="")