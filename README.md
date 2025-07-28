# boxcar

An RC Car

Demo Link: https://youtu.be/CNvrMNcvXPM

Please note in the video, both car and rc are pluged into computer for 5v power supply due to a lack of material on our end (this will be fixed at a later date - as will the design and frame). The only communication that is occuring between the two separate systems is wireless. 

## BOM

Seeed Studio Xiao RP2040 x 2

MPU-6050 IMU x 1

L298N Motor Drivers x 2

DSD Tech HC-05 Module x 2

Jumper Wires

## Notes

Utilizing the concept of 'master-slave', the data read from the accelerometer via I2C communication is recorded by the RP2040, and sent from the 'master' HC-05 to the 'slave' HC-05. The RP2040 then processes this data and translates measured x and y directional acceleration into the corresponding movement of 4 motors, controlled by 2 motor drivers. If the accelerometer detects an acceleration greater than +/-5000 mg (raw ADC counts), then the car will move forward/backward accordingly. 

## Pictures

![alt text](images/20250725_234653.jpg)

![alt text](<images/20250714_041952 (1).jpg>)
