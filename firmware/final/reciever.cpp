#include <Wire.h>
#include <MPU6050.h>

MPU6050 accel;
void setup() {
  Serial1.begin(9600); // Initiate communication
  Wire.begin();
  accel.initialize();
}

void loop() {
  int16_t ax, ay, az;
  ax = accel.getAccelerationX();
  ay = accel.getAccelerationY();
  az = accel.getAccelerationZ();

  String data = String(ax) + "," + String(ay) + "," + String(az);
  Serial1.println(data);
  delay(100);
}
