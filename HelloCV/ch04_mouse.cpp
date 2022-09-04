#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
using namespace std;

Mat img;
Point ptOld;
void on_mouse(int event, int x, int y, int flags, void*);

int main(void) {
	img = imread("lena.jpg");

	if (img.empty()) {
		cerr << "Image open failed!" << endl;
		return -1;
	}

	namedWindow("img");
	setMouseCallback("img", on_mouse);
	
	imshow("img", img);
	waitKey();

	return 0;
}

void on_mouse(int event, int x, int y, int flags, void*) {
	switch (event)
	{
	case EVENT_LBUTTONDOWN:
		ptOld = Point(x, y);   // 시작점
		cout << "EVENT_LBUTTONDOWN" << x << ", " << y << endl;
		break;
	case EVENT_LBUTTONUP:
		cout << "EVENT_LBUTTONUP" << x << ", " << y << endl;
		break;
	case EVENT_MOUSEMOVE:
		if (flags & EVENT_FLAG_LBUTTON) {
			line(img, ptOld, Point(x, y), Scalar(0, 255, 255), 2);   // 노란색 선
			imshow("img", img);
			ptOld = Point(x, y);   // 끝점 저장
		}
		break;
	default:
		break;
	}
}