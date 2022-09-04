#include "opencv2/opencv.hpp"
#include <iostream>   // c++ ǥ�� ����� ����

using namespace cv;   // cv:: ����
using namespace std;

void on_level_change(int pos, void* userdata);

int main(void) {
	Mat img = Mat::zeros(400, 400, CV_8UC1);

	namedWindow("image");
	createTrackbar("level", "image", 0, 16, on_level_change, (void*)&img);   // userdata �ʿ�(&img)

	imshow("image", img);
	waitKey();

	return 0;
}

void on_level_change(int pos, void* userdata) {
	Mat img = *(Mat*)userdata;

	img.setTo(pos * 16);   // �ִ� 256-1=255
	imshow("image", img);
}