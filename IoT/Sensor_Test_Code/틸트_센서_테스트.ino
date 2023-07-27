int LED = 2;
int tilt = 12;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(tilt, INPUT);
}

void loop() {
  if (digitalRead(tilt) == LOW){
    digitalWrite(LED, HIGH);
  }
  else {
    digitalWrite(LED, LOW);
  }
}
