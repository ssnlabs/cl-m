from multiprocessing import Process, shared_memory
import time

SHM_NAME = "ssnita"

def writer():
    shm = shared_memory.SharedMemory(name=SHM_NAME, create=True, size=1024)
    try:
        message = "Hello from the writer process!"
        shm.buf[:len(message)] = message.encode()
        print("Writer: Data written to shared memory.")
        time.sleep(5)
    finally:
        shm.close()
        shm.unlink()

def reader():
    time.sleep(1)
    shm = shared_memory.SharedMemory(name=SHM_NAME)
    try:
        message = bytes(shm.buf[:]).decode()
        print("Reader: Data read from shared memory:", message)
    finally:
        shm.close()

if __name__ == '__main__':
    writer_process = Process(target=writer)
    writer_process.start()

    reader_process = Process(target=reader)
    reader_process.start()

    writer_process.join()
    reader_process.join()
