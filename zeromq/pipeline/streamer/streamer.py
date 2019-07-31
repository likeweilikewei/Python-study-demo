import zmq


def main():
    try:
        print(1)
        context = zmq.Context(1)
        print(2)
        # Socket facing clients
        frontend = context.socket(zmq.PULL)
        frontend.bind("tcp://*:5559")
        print(3)

        # Socket facing services
        backend = context.socket(zmq.PUSH)
        backend.bind("tcp://*:5560")
        print(4)

        # zmq.device()里有个while True
        zmq.device(zmq.STREAMER, frontend, backend)
        print(5)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        print(6)
        # pass
        print(7)
        frontend.close()
        backend.close()
        context.term()
        print(8)


if __name__ == "__main__":
    main()
