# circuitpython

import board
import digitalio
import time

# REAR MOTOR PINS (Driver 1)
rear_L1 = digitalio.DigitalInOut(board.P1_15)
rear_L2 = digitalio.DigitalInOut(board.P1_13)
rear_R1 = digitalio.DigitalInOut(board.P1_11)
rear_R2 = digitalio.DigitalInOut(board.P0_10)

# FRONT MOTOR PINS (Driver 2)
front_L1 = digitalio.DigitalInOut(board.P0_24)
front_L2 = digitalio.DigitalInOut(board.P1_00)
front_R1 = digitalio.DigitalInOut(board.P0_11)
front_R2 = digitalio.DigitalInOut(board.P1_04)

# Set pin direction to OUTPUT
all_pins = [rear_L1, rear_L2, rear_R1, rear_R2,
            front_L1, front_L2, front_R1, front_R2]

for pin in all_pins:
    pin.direction = digitalio.Direction.OUTPUT

# Movement functions
def move_f():
    # All motors forward
    rear_L1.value = True;  rear_L2.value = False
    rear_R1.value = True;  rear_R2.value = False
    front_L1.value = True; front_L2.value = False
    front_R1.value = True; front_R2.value = False

def move_b():
    # All motors backward
    rear_L1.value = False; rear_L2.value = True
    rear_R1.value = False; rear_R2.value = True
    front_L1.value = False; front_L2.value = True
    front_R1.value = False; front_R2.value = True

def turn_l():
    # Left wheels backward, right wheels forward
    rear_L1.value = False; rear_L2.value = True
    rear_R1.value = True;  rear_R2.value = False
    front_L1.value = False; front_L2.value = True
    front_R1.value = True;  front_R2.value = False

def turn_r():
    # Right wheels backward, left wheels forward
    rear_L1.value = True;  rear_L2.value = False
    rear_R1.value = False; rear_R2.value = True
    front_L1.value = True;  front_L2.value = False
    front_R1.value = False; front_R2.value = True

def stop():
    # All motors off
    for pin in all_pins:
        pin.value = False

# Example loop
while True:
    move_f()
    time.sleep(1)
    turn_l()
    time.sleep(1)
    turn_r()
    time.sleep(1)
    move_b()
    time.sleep(1)
    stop()
    time.sleep(2)
