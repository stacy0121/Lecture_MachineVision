#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// ¾ð»þÇÁ ¸¶½ºÅ© ÇÊÅÍ¸µ
void unsharp_mask() {
	Mat src = imread("blox.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	imshow("src", src);

	for (int sigma = 1; sigma <= 5; sigma++) {
		Mat blurred;
		GaussianBlur(src, blurred, Size(), sigma);

		float alpha = 1.f;
		Mat dst = (1 + alpha) * src - alpha * blurred;   // »þÇÁ´×

		String desc = format("sigma: %d", sigma);
		putText(dst, desc, Point(10, 30), FONT_HERSHEY_SIMPLEX, 1.0, Scalar(255), 1, LINE_AA);

		imshow("dst", dst);
		waitKey();
	}
}

int main(void) {
	unsharp_mask();
	return 0;
}