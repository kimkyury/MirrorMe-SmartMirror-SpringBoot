// opencv 470
#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/core.hpp>

using namespace std;
using namespace cv;

#define RECORDINGTIME 150;

void recoding_message() {
	VideoCapture inputVideo(1);

	if (!inputVideo.isOpened()) {

		cout << "Can not open capture!!" << endl;

		return;

	}

	Size size = Size((int)inputVideo.get(CAP_PROP_FRAME_WIDTH), (int)inputVideo.get(CAP_PROP_FRAME_HEIGHT));

	cout << "Size = " << size << endl;

	int fourcc = VideoWriter::fourcc('D', 'X', '5', '0');

	double fps = inputVideo.get(CAP_PROP_FPS);

	bool isColor = true;

	// 확장자에 따라 오류가 뜰 수도 있음.
	VideoWriter outputVideo("message.mp4", fourcc, fps, size, isColor);

	cout << "파일 생성\n";

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

	cout << "녹화중...\n";

	while (cnt--) {

		inputVideo >> frame;

		if (frame.empty()) break;

		outputVideo << frame;
	}

	cout << "녹화끝\n";

	return;
}

int face_recognition() {
	VideoCapture cap(1, CAP_DSHOW);

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

		face.load("./data/haarcascades/haarcascade_frontalface_default.xml");	// 얼굴 탐지 cascade load
		if (!face.empty())
			face.detectMultiScale(grayImg, faceRect, 1.05, 10, 0, Size(50, 50));


		sideface.load("./data/haarcascades/haarcascade_profileface.xml");		// 옆 모습 탐지 cascade load
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
