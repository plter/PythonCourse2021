from multiprocessing import Process


def hello():
    print("Hello World")


if __name__ == '__main__':
    p = Process(target=hello)
    p.start()
    p.join()
