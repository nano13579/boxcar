#Day 1:

Today we created a basic drive base, with 4 gear motors, an nrf52840. Soldered all components, have a basic idea for communication between hand and car. We will need to make a motor driver. nOOOOO. There are three ways we can do this:
Transistor Switch - could make our own?
H-Bridge Circuit - we don't have a MOSFET but we could try to make our own?? + will need relay module
Potentiometer - can maybe be controlled electronically using analog pwm (but it's actually just digital that mimics analog :))))))), we’d still have to use a separate motor driver
We worked on the general schematic, and design. Hoping to see what supplies are available tomorrow. 

#Day 2+3:

Worked on the CAD model and got circuit python up and running.

##Tentative Materials List:

Servos x 4
XIAO RP2040 x 2
NRF Dev Board x 2
IMU x 1
Speaker x 1
OLED Display x 1
Neopixels in a band x 1

##Useful Documentation:

Pro Micro nRF52840
I2S | Adafruit Metro ESP32-S3 | Adafruit Learning System (for our amp)
Bluetooth Low Energy Basics | Getting Started with CircuitPython and Bluetooth Low Energy
Creating and Editing Code | Welcome to CircuitPython! | Adafruit Learning System
CircuitPython Pins and Modules | CircuitPython Essentials | Adafruit Learning System

##Footprints:

zhiayang/mikoto: Bluetooth LE nRF52840 microcontroller in a pro-micro footprint.


##Questions:

Does the audio amp have a DAC chip for better sound quality?
Does the speaker have a built in amplifier or transistor?

