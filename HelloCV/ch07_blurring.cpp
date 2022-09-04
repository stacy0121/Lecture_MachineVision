#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 평균값 필터를 이용한 블러링
void blurring_mean() {
	Mat src = imread("aloeL.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}
	
	imshow("src", src);

	Mat dst;
	for (int ksize = 3; ksize <= 7; ksize += 2) {
		blur(src, dst, Size(ksize, ksize));   // 커널 크기 변환

		String desc = format("Mean: %dx%d", ksize, ksize);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}
}

// 가우시안 필터링
void blurring_gaussian() {
	Mat src = imread("blox.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}
	
	imshow("src", src);

	Mat dst;
	for (int sigma = 1; sigma <= 5; sigma ++) {
		GaussianBlur(src, dst, Size(),(double)sigma);   // 커널 크기 변환

		String text = format("sigma: %d", sigma);
		putText(dst, text, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}
}

int main(void) {
	blurring_gaussian();
	return 0;
}