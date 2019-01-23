from MyThread import MyThread

# coding=utf-8

def main():
    for num in range(0, 200):
        MyThread(1, "thread1", 1).start()


if __name__ == '__main__':
    main()
