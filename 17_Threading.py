import threading

# inherit from thread
class messenger(threading.Thread):
    # run is the __init__ for Thread
    def run(self):
        # _ stands for no variable
        for _ in range(10):
            print(threading.currentThread().getName())

x = messenger(name="Send out messeges")
y = messenger(name="Receive messages")
x.start()
y.start()
