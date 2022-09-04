#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
using namespace std;

// Scalar 클래스
void ScalarOp() {
	Scalar gray = 128;   // [128, 0, 0, 0]
	cout << "gray: " << gray << endl;

	Scalar yellow(0, 255, 255);   // [0, 255, 255, 0]
	cout << "yellow: " << yellow << endl;

	Mat img1(256, 256, CV_8UC3, yellow);

	for (int i = 0;i < 4;i++)
		cout << yellow[i] << endl;
}

int main() {
	ScalarOp();
	return 0;
}