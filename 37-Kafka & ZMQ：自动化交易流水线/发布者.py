import zmq
import time


def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:6666')

    cnt = 1
    while True:
        time.sleep(1)
        socket.send_string('sever cnt {}'.format(cnt))
        print('send {}'.format(cnt))
        cnt += 1
        # time.sleep(1)


if __name__ == '__main__':
    run()
