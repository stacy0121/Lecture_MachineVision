#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
using namespace std;

int main() {
	cout << "Hello OpenCV " << CV_VERSION << endl;   // opencv 라이브러리 버전 출력

	Mat img;   // Mat 타입 변수 img
	img = imread("lena.jpg");   // Mat 객체로 변환

	if (img.empty()) {   // Mat 클래스 멤버 함수
		cerr << "Image load failed!" << endl;
		return -1;
	}

	//namedWindow("image");
	imshow("image", img);

	waitKey();

	return 0;
}