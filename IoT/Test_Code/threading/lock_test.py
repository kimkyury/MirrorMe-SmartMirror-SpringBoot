import threading

def worker(lock, count):
    with lock:
        for _ in range(count):
            print(threading.current_thread().name)

def main():
    lock = threading.Lock()
    thread1 = threading.Thread(target=worker, args=(lock, 5))
    thread2 = threading.Thread(target=worker, args=(lock, 5))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
