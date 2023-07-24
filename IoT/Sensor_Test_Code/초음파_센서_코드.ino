int trig = 2;
int echo = 3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);     // 시리얼포트 통신속도 9600 설정
  pinMode(trig, OUTPUT);  // trigger(발신부)를 출력모드로 설정
  pinMode(echo, INPUT);   // echo(수신부)를 입력모드로 설정
}
 
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig, HIGH); // trig핀(2)에 1입력
  delayMicroseconds(10);    // 10us 대기
  digitalWrite(trig, LOW);  // trig핀(2)에 0입력
  int distance = pulseIn(echo, HIGH)*340 / 2 / 10000; 
  // 거리=시간X속도/2(왕복이므로)
  Serial.print(distance);   // 거리 출력
  Serial.println("cm");     // "cm" 출력
  delay(100);               // 100ms=0.1s 지연
}