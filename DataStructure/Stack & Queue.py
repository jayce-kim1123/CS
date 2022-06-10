import queue

data = queue.Queue()
print(type(data))

data.put(2)
data.put('a')
data.put('23A')

print(data.get())
print(data.get())
print(data.get())