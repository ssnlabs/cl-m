from multiprocessing import Process, Queue
import time

def sender(queue):
    messages = ["Message 1 from sender", "Message 2 from sender", "Message 3 from sender", "STOP"]
    
    for message in messages:
        queue.put(message)
        print(f"Sender: Sent '{message}' to the queue.")
        time.sleep(1) 

def receiver(queue):
    while True:
        message = queue.get()
        print(f"Receiver: Received '{message}' from the queue.")
        if message == "STOP":
            print("Receiver: Termination signal received. Stopping.")
            break

if __name__ == "__main__":
    queue = Queue()
    sender_process = Process(target=sender, args=(queue,))
    receiver_process = Process(target=receiver, args=(queue,))

    sender_process.start()
    receiver_process.start()
    sender_process.join()
    receiver_process.join()
