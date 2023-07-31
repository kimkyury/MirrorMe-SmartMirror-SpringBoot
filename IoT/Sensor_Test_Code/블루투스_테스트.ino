#include <SoftwareSerial.h>
 
#define BT_RXD 2
#define BT_TXD 3
SoftwareSerial hc06(BT_RXD, BT_TXD);
 
void setup(){
  Serial.begin(9600);
  hc06.begin(9600);
}
 
void loop(){
  if (hc06.available()) {
    Serial.write(hc06.read());
  }
  if (Serial.available()) {
    hc06.write(Serial.read());
  }
}