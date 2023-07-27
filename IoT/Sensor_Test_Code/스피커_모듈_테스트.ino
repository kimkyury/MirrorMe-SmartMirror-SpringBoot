const int c = 1261;

const int buzzerPin = 2;
int counter = 0;
 
void setup()
{
  pinMode(buzzerPin, OUTPUT); //부저핀을 출력으로 설정
}
 
void loop()
{
  beep(c, 1000);  
  delay(500);
}
 
//소리를 설정하는 부분입니다. 스피커 모듈의 핀을 설정하는 부분입니다.
void beep(int note, int duration)
{
  //스피커 핀의 설정을 정의 합니다.
  tone(buzzerPin, note, duration);
  delay(5000);
  //스피커 핀을 멈춥니다.
  noTone(buzzerPin);
 
  delay(50);
 
  //카운터를 증가 시킵니다.
  counter++;
}