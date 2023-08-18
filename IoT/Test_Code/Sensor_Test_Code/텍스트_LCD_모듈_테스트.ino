#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,20,4);    

void setup()
{
  lcd.init();  // LCD초기 설정
  
  lcd.backlight(); // LCD초기 설정  
  
  lcd.setCursor(0,0); 
  
  //처음 텍스트가 LCD에 나타날 위치  lcd.setCursor(열, 행)
  
  lcd.print("We Are 1oT"); 
  
  lcd.setCursor(2,1); 
  
  lcd.print("Aduino TEST"); 
  
}

void loop()
{
  
}