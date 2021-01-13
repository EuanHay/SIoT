int sensor1_value = 0;
int sensor2_value = 0;
int previous_value1 = 100;
int previous_value2 = 100;
int threshold = 5;
void setup() {
Serial.begin(9600); // setup serial
}
//Sensor 1 turned anticlockwise
//Sensor 2 turned clockwise
void loop() {
sensor1_value = analogRead(A0);
sensor2_value = analogRead(A1);
if (sensor1_value >= previous_value1 + threshold) {
  Serial.println(sensor1_value);
  Serial.println(sensor2_value);
}
else if (sensor1_value <= previous_value1 - threshold) {
  Serial.println(sensor1_value);
  Serial.println(sensor2_value);
  delay(3000);
}
else if (sensor2_value >= previous_value2 + threshold) {
  Serial.println(sensor1_value);
  Serial.println(sensor2_value);
  delay(3000);
}
else if (sensor2_value <= previous_value2 - threshold) {
  Serial.println(sensor1_value);
  Serial.println(sensor2_value);
  delay(3000);
}
previous_value1 = sensor1_value;
previous_value2 = sensor2_value;
delay(10);
}
