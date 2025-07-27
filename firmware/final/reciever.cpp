int motor1_in1 = 26;
int motor1_in2 = 27;
int motor2_in1 = 28;
int motor2_in2 = 29;
int motor3_in1 = 6;
int motor3_in2 = 7;
int motor4_in1 = 3;
int motor4_in2 = 4;

void setup() {
  int pins[] = {motor1_in1, motor1_in2, motor2_in1, motor2_in2,
                motor3_in1, motor3_in2, motor4_in1, motor4_in2};
  for (int i = 0; i < 8; i++) {
    pinMode(pins[i], OUTPUT);
  }

  Serial1.begin(9600); // HC-05 input
}

void loop() {
  // Reduce Noise
  if (Serial1.available()) {
    String data = Serial1.readStringUntil('\n');
    data.trim(); 

    if (data.indexOf(',') > 0) {
      int ay = data.substring(0, data.indexOf(',')).toInt();

      // Acceleromter reading threshold
      const int threshold = 5000;

      if (ay > threshold) {
        driveAll(true);
      } else if (ay < -threshold) {
        driveAll(false);
      } else {
        stopAll();
      }
    }
  }
}

void driveAll(bool forward) {
  setMotor(motor1_in1, motor1_in2, forward);
  setMotor(motor2_in1, motor2_in2, forward);
  setMotor(motor3_in1, motor3_in2, forward);
  setMotor(motor4_in1, motor4_in2, forward);
}

void stopAll() {
  stopMotor(motor1_in1, motor1_in2);
  stopMotor(motor2_in1, motor2_in2);
  stopMotor(motor3_in1, motor3_in2);
  stopMotor(motor4_in1, motor4_in2);
}

void setMotor(int in1, int in2, bool forward) {
  digitalWrite(in1, forward ? HIGH : LOW);
  digitalWrite(in2, forward ? LOW : HIGH);
}

void stopMotor(int in1, int in2) {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}
