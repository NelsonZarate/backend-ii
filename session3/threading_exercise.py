"""Session 3 exercise: two threads printing letters and numbers concurrently."""
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(0.2)

def print_letters():
    for ch in "abcde":
        print(ch)
        time.sleep(0.3)

def run():
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    run()
