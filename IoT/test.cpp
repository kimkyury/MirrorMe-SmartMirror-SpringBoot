#include <cstdlib>

#include <wiringPi.h>
#include <unistd.h>

int main(){
//      std::system("xset dpms force off");
	wiringPiSetup();
	
	int pinNumber = 1;
	
	pinMode(pinNumber, OUTPUT);
	
	digitalWrite(pinNumber, 1);
	delay(1000);
	
	digitalWrite(pinNumber, 0);
	delay(1000);

        return 0;
}

