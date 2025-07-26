// For determining AT address of slave
// and configuring HC-05's as master/slave
// Open Serial Monitor to configure
#include <SoftwareSerial.h>
SoftwareSerial BTSerial(2, 3);

void setup() {
  Serial.begin(9600);
  BTSerial.begin(38400);
  Serial.println("Enter AT commands:");
}

void loop() {
  if (BTSerial.available()) {
    Serial.write(BTSerial.read());
  }
  if (Serial.available()) {
    BTSerial.write(Serial.read());
  }
}
