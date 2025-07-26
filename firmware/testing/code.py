from machine import Pin, PWM
import time

rear_ena_pin = 16
rear_enb_pin = 17
front_ena_pin = 18
front_enb_pin = 19

rear_L1_pin = 2
rear_L2_pin = 3
rear_R1_pin = 4
rear_R2_pin = 5

front_L1_pin = 6
front_L2_pin = 7
front_R1_pin = 8
front_R2_pin = 9

rear_ena = PWM(Pin(rear_ena_pin))
rear_enb = PWM(Pin(rear_enb_pin))
front_ena = PWM(Pin(front_ena_pin))
front_enb = PWM(Pin(front_enb_pin))

for pwm in [rear_ena, rear_enb, front_ena, front_enb]:
    pwm.freq(5000)

rear_L1 = Pin(rear_L1_pin, Pin.OUT)
rear_L2 = Pin(rear_L2_pin, Pin.OUT)
rear_R1 = Pin(rear_R1_pin, Pin.OUT)
rear_R2 = Pin(rear_R2_pin, Pin.OUT)
front_L1 = Pin(front_L1_pin, Pin.OUT)
front_L2 = Pin(front_L2_pin, Pin.OUT)
front_R1 = Pin(front_R1_pin, Pin.OUT)
front_R2 = Pin(front_R2_pin, Pin.OUT)

def set_speed(speed=65535):
    rear_ena.duty_u16(speed)
    rear_enb.duty_u16(speed)
    front_ena.duty_u16(speed)
    front_enb.duty_u16(speed)

def move_f():
    for motor in [rear_L1, rear_R1, front_L1, front_R1]:
        motor.value(1)
    for motor in [rear_L2, rear_R2, front_L2, front_R2]:
        motor.value(0)
    set_speed()

def move_b():
    for motor in [rear_L1, rear_R1, front_L1, front_R1]: 
        motor.value(0)
    for motor in [rear_L2, rear_R2, front_L2, front_R2]:
        motor.value(1)
    set_speed()

def turn_l():
    rear_L1.value(0); rear_L2.value(1)
    rear_R1.value(1); rear_R2.value(0)
    front_L1.value(0); front_L2.value(1)
    front_R1.value(1); front_R2.value(0)
    set_speed()

def turn_r():
    rear_L1.value(1); rear_L2.value(0)
    rear_R1.value(0); rear_R2.value(1)
    front_L1.value(1); front_L2.value(0)
    front_R1.value(0); front_R2.value(1)
    set_speed()

def stop():
    for pin in [rear_L1, rear_L2, rear_R1, rear_R2,
                front_L1, front_L2, front_R1, front_R2]:
        pin.value(0)
    set_speed(0)

while True:
    move_f(); time.sleep(1)
    turn_l(); time.sleep(1)
    turn_r(); time.sleep(1)
    move_b(); time.sleep(1)
    stop();  time.sleep(2)