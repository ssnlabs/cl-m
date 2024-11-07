import multiprocessing
import time

def writer(shared_memory):
    message = b"Hello from the writer process!"
    shared_memory[:len(message)] = message
    print("Writer: Data written to shared memory.")
    
    time.sleep(2)

def reader(shared_memory):
    time.sleep(1)
    message = bytes(shared_memory[:]).rstrip(b'\x00').decode('utf-8')
    print("Reader: Data read from shared memory:", message)

def main():
    shared_memory = multiprocessing.Array('b', 1024)

    writer_process = multiprocessing.Process(target=writer, args=(shared_memory,))
    reader_process = multiprocessing.Process(target=reader, args=(shared_memory,))

    writer_process.start()
    reader_process.start()    
    writer_process.join()
    reader_process.join()

if __name__ == "__main__":
    main()
