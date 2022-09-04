#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
using namespace std;

void on_level_change(int pos, void* userdata);

int main(void) {
	Mat img = Mat::zeros(400, 400, CV_8UC1);

	namedWindow("image");
	createTrackbar("level", "image", 0, 16, on_level_change, (void*)&img);   // userdata 필요(&img)

	imshow("image", img);
	waitKey();

	return 0;
}

void on_level_change(int pos, void* userdata) {
	Mat img = *(Mat*)userdata;

	img.setTo(pos * 16);   // 최댓값 256-1=255
	imshow("image", img);
}