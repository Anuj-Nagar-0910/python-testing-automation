#can_interface.py

import can
import time

def setup_can():
    return can.interface.Bus(
        bustype='virtual',
        receive_own_messages=True
    )

def send_message(bus):
    msg = can.Message(arbitration_id=0x123, data=[1, 2, 3, 4])
    bus.send(msg)

def receive_message(bus):
    time.sleep(0.1)
    return bus.recv(timeout=1)