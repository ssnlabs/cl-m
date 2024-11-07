from multiprocessing import Process, Pipe

def parent_process(parent_conn, child_conn):
    
    child_conn.close()

    parent_message = "Hello from parent!"
    parent_conn.send(parent_message)
    print("Parent: Sent message to child.")
    
    child_response = parent_conn.recv()
    print("Parent: Received response from child:", child_response)
    
    parent_conn.close()

def child_process(parent_conn, child_conn):
    
    parent_conn.close()
    
    parent_message = child_conn.recv()
    print("Child: Received message from parent:", parent_message)

    child_message = "Hello from child!"
    child_conn.send(child_message)
    print("Child: Sent response to parent.")
        
    child_conn.close()

if __name__ == "__main__":
    
    parent_conn, child_conn = Pipe()
    
    child = Process(target=child_process, args=(parent_conn, child_conn))
    child.start()

    parent_process(parent_conn, child_conn)    
    child.join()
