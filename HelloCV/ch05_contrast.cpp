#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// �⺻���� ������ ��Ϻ� ����
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

// ȿ������ ��Ϻ� ����
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