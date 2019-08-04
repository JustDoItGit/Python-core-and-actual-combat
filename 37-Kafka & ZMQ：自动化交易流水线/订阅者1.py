import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://127.0.0.1:6666')
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    print('client 1')
    while True:
        msg = socket.recv()
        print('msg: %s' % msg)


if __name__ == '__main__':
    run()
