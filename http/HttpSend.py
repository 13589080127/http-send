# coding=utf-8
from testThread import MyThread


def main():
    # 开启两百个线程
    for num in range(0, 200):
        MyThread(1, "thread1", 1).start()


if __name__ == '__main__':
    main()
