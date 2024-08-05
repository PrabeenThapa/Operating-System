import threading
import time
import random

# Initialize a mutex lock
mutex = threading.Lock()

# Initialize buffer related variables
full = 0
empty = 10
buffer = []

# Function to produce an item and add it to the buffer
def producer():
    global full, empty, buffer
    while True:
        with mutex:
            if empty > 0:
                item = random.randint(1, 100)
                buffer.append(item)
                full += 1
                empty -= 1
                print(f"\nProducer produces item {item}")
            else:
                print("Buffer is full")
        time.sleep(random.random())

# Function to consume an item and remove it from the buffer
def consumer():
    global full, empty, buffer
    while True:
        with mutex:
            if full > 0:
                item = buffer.pop(0)
                full -= 1
                empty += 1
                print(f"\nConsumer consumes item {item}")
            else:
                print("Buffer is empty!")
        time.sleep(random.random())

# Main function
if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
