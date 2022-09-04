#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
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