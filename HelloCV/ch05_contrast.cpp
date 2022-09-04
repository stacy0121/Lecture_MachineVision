#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 기본적인 영상의 명암비 증가
void contrast1() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	float s = 2.f;
	Mat dst = s * src;

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

// 효과적인 명암비 조절
void contrast2() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	float alpha = 1.f;
	Mat dst = src + (src - 128) * alpha;

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

int main(void) {
	contrast2();
	return 0;
}