#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// ��հ� ���͸� �̿��� ����
void blurring_mean() {
	Mat src = imread("aloeL.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}
	
	imshow("src", src);

	Mat dst;
	for (int ksize = 3; ksize <= 7; ksize += 2) {
		blur(src, dst, Size(ksize, ksize));   // Ŀ�� ũ�� ��ȯ

		String desc = format("Mean: %dx%d", ksize, ksize);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}
}

// ����þ� ���͸�
void blurring_gaussian() {
	Mat src = imread("blox.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}
	
	imshow("src", src);

	Mat dst;
	for (int sigma = 1; sigma <= 5; sigma ++) {
		GaussianBlur(src, dst, Size(),(double)sigma);   // Ŀ�� ũ�� ��ȯ

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