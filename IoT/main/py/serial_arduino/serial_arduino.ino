#define trig 6
#define echo 7

void setup() {
  Serial.begin(9600);     // 시리얼포트 통신속도 9600 설정
  pinMode(trig, OUTPUT);  // trigger(발신부)를 출력모드로 설정
  pinMode(echo, INPUT);   // echo(수신부)를 입력모드로 설정
}

bool distance(float cut, bool before){
  digitalWrite(trig, HIGH); // trig핀(2)에 1입력
  delayMicroseconds(10);    // 10us 대기
  digitalWrite(trig, LOW);  // trig핀(2)에 0입력
  int sen_distance = pulseIn(echo, HIGH)*340 / 2 / 10000; 

  if (sen_distance < cut) return true;
  else if (sen_distance > cut + 30) return false;
  else return before;
}

bool before = false;
bool now = false;

unsigned long set_time = 0;

void loop() {
  now = distance(50, before);
  // 나타났을때
  if (!before && now)
  {
    set_time = millis();
  }

  // 사라졌을 때
  elif (before && !now) 
  {
    set_time = millis();
  }

  // 나타난 상태가 유지
  elif (before && now)
  {
    if(millis() - set_time >= 1000) Serial.print("appear!/n/r")
  }

  // 사라진 상태가 유지
  elif (!before && !now)
  {
    if(millis() - set_time >= 10000) Serial.print("disappear!/n/r")
  }

  before = now;
  
  delay(100);               // 100ms=0.1s 지연
}