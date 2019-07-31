import sys
import time
import zmq
from datetime import datetime

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

senders = context.socket(zmq.REQ)
senders.connect("tcp://localhost:5559")
# receiver
# Wait for start of batch
# s = receiver.recv()

# Start our clock now
tstart = time.time()

# Process 100 confirmations
for task_nbr in range(100):
    s = receiver.recv()
    if task_nbr % 10 == 0:
        sys.stdout.write(':')
    else:
        sys.stdout.write('.')
    sys.stdout.flush()

# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart)*1000))

while True:
    response = receiver.recv()
    print(response.decode('utf-8'))
    time.sleep(1)
    senders.send_string('message from collector,result:{}'.format(str(response,encoding='utf-8')))
    ss = senders.recv_string()
    print('message from server:{} at:{}'.format(ss,str(datetime.now())))

