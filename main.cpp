#pragma comment (lib, "wldap32.lib")
#pragma comment (lib, "ws2_32.lib")

#ifdef _DEBUG
#pragma comment (lib, "libcurld.lib")
#else
#pragma comment (lib, "libcurl.lib")
#endif

#define CURL_STATICLIB

using namespace std;

#include <iostream>
#include <stdio.h>
#include <string>
#include <curl/curl.h>

string STT_Streaming(int x){
	string str1 = "엄마한테 영상메세지 보내고 싶어";
	string str2 = "어머니한테 영상메세지 보낼래";
	string str3 = "부모님한테 영상메세지";
	if (x == 1){
		return str1;
	}
	else if(x == 2){
		return str2;
	}
	else{
		return str3;
	}
};

int get(void) {
	// make easy handle
	CURL *curl = curl_easy_init();
	// result of curl
	CURLcode res;

	if (curl) {
		curl_easy_setopt(curl, CURLOPT_URL, "naver.com");
		/* example.com is redirected, so we tell libcurl to follow redirection */
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

		/* Perform the request, res will get the return code */
		res = curl_easy_perform(curl);
		/* Check for errors */
		if (res != CURLE_OK)
			fprintf(stderr, "curl_easy_perform() failed: %s\n",
				curl_easy_strerror(res));

		/* always cleanup */
		curl_easy_cleanup(curl);
	}
	
	return 0;

}

using namespace std;

void setup(){

}

void loop(){
    while (true){
        string str = "엄마한테 영상메세지 보내고 싶어";
        get();
        return;
    }
}

int main() {
    setup();
    loop();
    return 0;
}