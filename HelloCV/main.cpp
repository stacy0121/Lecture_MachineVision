#include "opencv2/opencv.hpp"
#include <iostream>   // c++ ǥ�� ����� ����

using namespace cv;   // cv:: ����
using namespace std;

int main() {
	cout << "Hello OpenCV " << CV_VERSION << endl;   // opencv ���̺귯�� ���� ���

	Mat img;   // Mat Ÿ�� ���� img
	img = imread("lena.jpg");   // Mat ��ü�� ��ȯ

	if (img.empty()) {   // Mat Ŭ���� ��� �Լ�
		cerr << "Image load failed!" << endl;
		return -1;
	}

	//namedWindow("image");
	imshow("image", img);

	waitKey();

	return 0;
}