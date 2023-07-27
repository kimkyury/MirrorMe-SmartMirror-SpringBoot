#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

void detectMultiScale(InputArray image,	// 입력 이미지
	std::vector<Rect>& objects,			// 추출된 영역 
	double scaleFactor = 1.1,			// 이미지 배율 축소 정도
	int minNeighbors = 3, 			// 도형의 이웃 수 
	int flags = 0,				// 플래그
	Size minSize = Size(),			// 추출할 영역의 최소 크기 (해당 크기 이하는 무시)
	Size maxSize = Size() 			// 추출할 영역의 최대 크기 (해당 크기 이상는 무시)
);

int main(int ac, char** av) {

	VideoCapture cap(0, CAP_DSHOW);
	cap.set(CAP_PROP_FRAME_WIDTH, 1920);
	cap.set(CAP_PROP_FRAME_HEIGHT, 1080);

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

		std::vector<Rect> faceRect, eyeRect;
		CascadeClassifier face, eye;

		face.load("haarcascade_frontalface_default.xml");	// 얼굴 탐지 cascade load
		if (!face.empty())
			face.detectMultiScale(grayImg, faceRect, 1.05, 10, 0, Size(50, 50));

		/*
		eye.load("haarcascade_eye.xml");		// 눈 탐지 cascade load
		if (!eye.empty())
			eye.detectMultiScale(grayImg, eyeRect, 1.05, 5, 0, Size(15, 15));
		*/
		for (int i = 0; i < faceRect.size(); i++)
			rectangle(img, Rect(faceRect[i]), Scalar(50, 0, 200), 2);	// 얼굴 영역 그리기


		//for (int i = 0; i < eyeRect.size(); i++)
		//	rectangle(img, Rect(eyeRect[i]), Scalar(200, 0, 50), 2);


		imshow("camera img", img);
		if (waitKey(1) == 27)
			break;
	}


	return 0;
}