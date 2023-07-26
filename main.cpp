/*
#pragma comment (lib, "wldap32.lib")
#pragma comment (lib, "ws2_32.lib")

#ifdef _DEBUG
#pragma comment (lib, "libcurld.lib")
#else
#pragma comment (lib, "libcurl.lib")
#endif

#define CURL_STATICLIB
*/

#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>
// #include <curl/curl.h>

// opencv 460
#include <opencv2/opencv.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>
// Serial
#include <Windows.h>
#include <atlstr.h>

using namespace std;
using namespace cv;

#define RECORDINGTIME 120;
#define BUFFER_SIZE 128;

void recoding_message() {
	VideoCapture inputVideo(0);

	if (!inputVideo.isOpened()) {

		cout << "Can not open capture!!" << endl;

		return;

	}

	Size size = Size((int)inputVideo.get(CAP_PROP_FRAME_WIDTH), (int)inputVideo.get(CAP_PROP_FRAME_HEIGHT));

	cout << "Size = " << size << endl;

	int fourcc = VideoWriter::fourcc('D', 'X', '5', '0');

	double fps = 24;

	bool isColor = true;

	VideoWriter outputVideo("videomessage.avi", fourcc, fps, size, isColor);

	if (!outputVideo.isOpened()) {

		cout << "Can not do!!" << endl;

		return;

	}

	if (fourcc != -1) {

		imshow("frame", NULL);

		waitKey(100);

	}

	int delay = 1000 / fps;

	Mat frame;

	int cnt = RECORDINGTIME;
	while (cnt--) {

		inputVideo >> frame;

		if (frame.empty()) break;

		outputVideo << frame;

		imshow("frame", frame);
	}

	return;
}

int face_recognition() {
	VideoCapture cap(0, CAP_DSHOW);

	/*
	cap.set(CAP_PROP_FRAME_WIDTH, 1920);
	cap.set(CAP_PROP_FRAME_HEIGHT, 1080);
	*/

	if (!cap.isOpened())
	{
		printf("Can't open the camera");
		return -1;
	}

	Mat img;

	while (1)
	{
		cap >> img;
		flip(img, img, 1);

		Mat grayImg;
		cvtColor(img, grayImg, COLOR_BGR2GRAY);		// 정확도를 높히기 위해 gray 이미지로 변경

		std::vector<Rect> faceRect, sidefaceRect;
		CascadeClassifier face, sideface;

		face.load("./opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml");	// 얼굴 탐지 cascade load
		if (!face.empty())
			face.detectMultiScale(grayImg, faceRect, 1.05, 10, 0, Size(50, 50)); 


		sideface.load("./opencv/sources/data/haarcascades/haarcascade_profileface.xml");		// 옆 모습 탐지 cascade load
		if (!sideface.empty())
			sideface.detectMultiScale(grayImg, sidefaceRect, 1.05, 5, 0, Size(15, 15));

		for (int i = 0; i < faceRect.size(); i++)
			rectangle(img, Rect(faceRect[i]), Scalar(50, 0, 200), 2);	// 얼굴 영역 그리기


		for (int i = 0; i < sidefaceRect.size(); i++)
			rectangle(img, Rect(sidefaceRect[i]), Scalar(200, 0, 50), 2);


		imshow("camera img", img);
		if (waitKey(1) == 27)
			break;
	}

	/*
	Mat img = imread("./faceimg/temp.jpg", 1);
	imshow("img", img);
	waitKey(0);
	*/
	return 0;
}

string STT_Streaming(int x) {
	string str1 = "엄마한테 영상메세지 보내고 싶어";
	string str2 = "어머니한테 영상메세지 보낼래";
	string str3 = "부모님한테 영상메세지";
	if (x == 1) {
		return str1;
	}
	else if (x == 2) {
		return str2;
	}
	else {
		return str3;
	}
};

int get() {
	/*
	// make easy handle
	CURL* curl = curl_easy_init();
	// result of curl
	CURLcode res;

	if (curl) {
		curl_easy_setopt(curl, CURLOPT_URL, "naver.com");
		// example.com is redirected, so we tell libcurl to follow redirection
		curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

		// Perform the request, res will get the return code
		res = curl_easy_perform(curl);
		// Check for errors
		if (res != CURLE_OK)
			fprintf(stderr, "curl_easy_perform() failed: %s\n",
				curl_easy_strerror(res));

		// always cleanup
		curl_easy_cleanup(curl);
	}
	*/
	return 2;

}

void setup() {

}

void loop() {
	while (true) {
		string str = "엄마한테 영상메세지 보내고 싶어";
		switch (get()) {
		case 1:
			recoding_message();
		case 2:
			face_recognition();
		}
		return;
	}
}

int main() {
	setup();
	loop();
	return 0;
}
