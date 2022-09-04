#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 마스크 영상을 이용한 픽셀 값 설정
void mask_setTo() {
	Mat src = imread("lena.jpg", IMREAD_COLOR);
	Mat mask = imread("chessboard.png", IMREAD_GRAYSCALE);

	if (src.empty()||mask.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	src.setTo(Scalar(0, 255, 255), mask);   // 마스크 적용

	imshow("src", src);
	imshow("mask", mask);

	waitKey();
}

// 마스크 영상을 이용하여 픽셀 값의 일부분만 복사하기
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

// 영상의 반전 시간 측정 예제
void time_inverse() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat dst(src.rows, src.cols, src.type());

	// 연산 시간 측정
	TickMeter tm;
	tm.start();

	for (int j = 0; j < src.rows; j++) {
		for (int i = 0; i < src.cols; i++)
			dst.at<uchar>(j, i) = 255 - src.at<uchar>(j, i);   // 픽셀 값 반전
	}

	tm.stop();
	cout << "Image inverse took " << tm.getTimeMilli() << "ms. " << endl;
}

int main(void) {
	time_inverse();
	return 0;
}