void setup() {
  Serial.begin(9600);
}
void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    Serial.println(data);
    if (data.startsWith("red")){
      digitalWrite(2,HIGH);
    }
  }
}
