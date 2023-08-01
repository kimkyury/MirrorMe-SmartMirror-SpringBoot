#include <opencv2/imgcodecs.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <string>
#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
    string temp;
    cin >> temp;
    Mat img = imread(temp + ".png");

    imshow("img", img);
    waitKey(0);

    return 0;
}