#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

void brightness1() {
	Mat src = imread("rubberwhale1.png", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	Mat dst = src + 100;

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

// 포화 연산을 고려하지 않은 영상의 밝기 증가 직접 구현
void brightness2() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	Mat dst(src.rows, src.cols, src.type());

	for (int j = 0; j < src.rows; j++) {
		for (int i = 0; i < src.cols; i++)
			dst.at<uchar>(j, i) = 255 - src.at<uchar>(j, i) + 100;
	}

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

// 포화 연산을 고려한 영상의 밝기 증가 직접 구현
void brightness3() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	Mat dst(src.rows, src.cols, src.type());

	for (int j = 0; j < src.rows; j++) {
		for (int i = 0; i < src.cols; i++)
			dst.at<uchar>(j, i) = saturate_cast<uchar>(src.at<uchar>(j, i) + 100);
	}

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

// 트랙바를 이용한 영상의 밝기 조절하기
void on_brightness(int pos, void* userdata) {
	Mat src = *(Mat*)userdata;
	Mat dst = src + pos;
	
	imshow("dst", dst);
}

void brightness4() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	namedWindow("dst");
	createTrackbar("Brightness", "dst", 0, 100, on_brightness, (void*)&src);
	on_brightness(0, (void*)&src);

	waitKey();
}

int main(void) {
	brightness3();
	return 0;
}