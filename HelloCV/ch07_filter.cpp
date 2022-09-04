#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 엠보싱 필터링
void filter_embossing() {
	Mat src = imread("aloeL.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	float data[] = { -1,-1,0,-1,0,1,0,1,1 };
	Mat emboss(3, 3, CV_32FC1, data);   // 필터

	Mat dst;
	filter2D(src, dst, -1, emboss, Point(-1, -1), 128);   // 커널 중심이 고정점

	imshow("src", src);
	imshow("dst", dst);
	waitKey();
}

int main(void) {
	filter_embossing();
	return 0;
}