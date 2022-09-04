#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

String filename = "mydata.json";

// ���Ͽ� ������ �����ϱ�
void writeData() {
	String name = "Jane";
	int age = 10;
	Point pt1(100, 200);
	vector<int> scores = { 80,90,50 };
	Mat mat1 = (Mat_<float>(2, 2) << 1.0f, 1.5f, 2.0f, 3.2f);   // �ʱ�ȭ ����Ʈ

	FileStorage fs(filename, FileStorage::WRITE);   // ������ �̸�, ������

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

    // �����͸� �����Ͽ� ����
	fs << "name" << name;
	fs << "age" << age;
	fs << "point" << pt1;
	fs << "scores" << scores;
	fs << "data" << mat1;

	fs.release();
}

// ���Ϸκ��� ������ �ҷ�����
void readData() {
	// ���� �ڷ��� ����
	String name;
	int age;
	Point pt1;
	vector<int> scores;
	Mat mat1;

	FileStorage fs(filename, FileStorage::READ);   // FileStorage ��ü �б� ���� ����

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

	// ��ü ���� �� ������ �о����
	fs["name"] >> name;
	fs["age"] >> age;
	fs["point"] >> pt1;
	fs["scores"] >> scores;
	fs["data"] >> mat1;

	fs.release();

	cout << "name: " << name << endl;
	cout << "age: " << age << endl;
	cout << "point: " << pt1 << endl;
	cout << "scores: " << Mat(scores).t() << endl;   // 1�� ��ġ ���
	cout << "data:\n" << mat1 << endl;
}

int main(void) {
	readData();
	return 0;
}