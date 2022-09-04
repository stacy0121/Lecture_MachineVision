#include "opencv2/opencv.hpp"
#include <iostream>   // c++ ǥ�� ����� ����

using namespace cv;   // cv:: ����
using namespace std;

int main(void) {
	Mat img = imread("lena.jpg");
	
	if (img.empty()) {
		cerr << "Image open failed!" << endl;
		return -1;
	}

	namedWindow("img");
	imshow("img", img);

	while (true) {
		int keycode = waitKey();

		if (keycode == 'i' || keycode == 'I') {
			img = ~img;
			imshow("img", img);
		}
		else if (keycode == 27 || keycode == 'q' || keycode == 'Q')
			break;
	}

	return 0;
}