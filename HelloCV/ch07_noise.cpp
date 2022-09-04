#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 가우시안 잡음 추가
void noise_gaussian() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	imshow("src", src);

	for (int stddev = 10; stddev <= 30; stddev += 10) {   // 표준편차 증가
		Mat noise(src.size(), CV_32SC1);
		randn(noise, 0, stddev);   // 가우시안 분포 난수

		Mat dst;
		add(src, noise, dst, Mat(), CV_8U);   // src + noise

		String desc = format("stddev: %d", stddev);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}
}

// 양방향 필터링
void filter_bilateral() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	Mat noise(src.size(), CV_32SC1);
	randn(noise, 0, 5);
	add(src, noise, src, Mat(), CV_8U);   // src + noise

	Mat dst1;
	GaussianBlur(src, dst1, Size(), 5);

	Mat dst2;
	bilateralFilter(src, dst2, -1, 10, 5);   // 잡음 제거

	imshow("src", src);
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	waitKey();
}

// 미디언 필터링
void filter_median() {
	Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	int num = (int)(src.total() * 0.1);   // 전체 원소 개수의 10%
	for (int i = 0; i < num; i++) {
		int x = rand() % src.cols;
		int y = rand() % src.rows;
		src.at<uchar>(y, x) = (i % 2) * 255;   // 0 아니면 255?
 }

	Mat dst1;
	GaussianBlur(src, dst1, Size(), 1);

	Mat dst2;
	medianBlur(src, dst2, 3);

	imshow("src", src);
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	waitKey();
}

int main(void) {
	filter_median();
	return 0;
}