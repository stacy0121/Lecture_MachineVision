#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// ����ũ ������ �̿��� �ȼ� �� ����
void mask_setTo() {
	Mat src = imread("lena.jpg", IMREAD_COLOR);
	Mat mask = imread("chessboard.png", IMREAD_GRAYSCALE);

	if (src.empty()||mask.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	src.setTo(Scalar(0, 255, 255), mask);   // ����ũ ����

	imshow("src", src);
	imshow("mask", mask);

	waitKey();
}

// ����ũ ������ �̿��Ͽ� �ȼ� ���� �Ϻκи� �����ϱ�
void mask_copyTo() {
	Mat src = imread("chessboard.png", IMREAD_COLOR);
	Mat mask = imread("chessboard.png", IMREAD_GRAYSCALE);
	Mat dst = imread("lena.jpg");

	if (src.empty() || mask.empty() || dst.empty()) {
		cerr<<"Image load failed!" << endl;
		return;
	}

	src.copyTo(dst, mask);

	imshow("dst", dst);

	waitKey();
}

// ������ ���� �ð� ���� ����
void time_inverse() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat dst(src.rows, src.cols, src.type());

	// ���� �ð� ����
	TickMeter tm;
	tm.start();

	for (int j = 0; j < src.rows; j++) {
		for (int i = 0; i < src.cols; i++)
			dst.at<uchar>(j, i) = 255 - src.at<uchar>(j, i);   // �ȼ� �� ����
	}

	tm.stop();
	cout << "Image inverse took " << tm.getTimeMilli() << "ms. " << endl;
}

int main(void) {
	time_inverse();
	return 0;
}