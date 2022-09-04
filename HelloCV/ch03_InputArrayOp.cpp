#include "opencv2/opencv.hpp"
#include <iostream>   // c++ ǥ�� ����� ����

using namespace cv;   // cv:: ����
using namespace std;

void printMat(InputArray _mat) {
	Mat mat = _mat.getMat();
	cout << mat << endl;
}

void InputArrayOp() {
	uchar data1[] = { 1,2,3,4,5,6 };
	Mat mat1(2, 3, CV_8U, data1);
	printMat(mat1);    // Mat Ÿ�� �μ�

	vector<float> vec1 = { 1.2f, 3.4f, -2.1f };
	printMat(vec1);    // vector<T> Ÿ�� �μ�
}

int main() {
	InputArrayOp();
	return 0;
}