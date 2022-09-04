#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

String filename = "mydata.json";

// 파일에 데이터 저장하기
void writeData() {
	String name = "Jane";
	int age = 10;
	Point pt1(100, 200);
	vector<int> scores = { 80,90,50 };
	Mat mat1 = (Mat_<float>(2, 2) << 1.0f, 1.5f, 2.0f, 3.2f);   // 초기화 리스트

	FileStorage fs(filename, FileStorage::WRITE);   // 데이터 이름, 데이터

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

    // 데이터를 구분하여 저장
	fs << "name" << name;
	fs << "age" << age;
	fs << "point" << pt1;
	fs << "scores" << scores;
	fs << "data" << mat1;

	fs.release();
}

// 파일로부터 데이터 불러오기
void readData() {
	// 여러 자료형 변수
	String name;
	int age;
	Point pt1;
	vector<int> scores;
	Mat mat1;

	FileStorage fs(filename, FileStorage::READ);   // FileStorage 객체 읽기 모드로 생성

	if (!fs.isOpened()) {
		cerr << "File open failed!" << endl;
		return;
	}

	// 객체 접근 및 데이터 읽어오기
	fs["name"] >> name;
	fs["age"] >> age;
	fs["point"] >> pt1;
	fs["scores"] >> scores;
	fs["data"] >> mat1;

	fs.release();

	cout << "name: " << name << endl;
	cout << "age: " << age << endl;
	cout << "point: " << pt1 << endl;
	cout << "scores: " << Mat(scores).t() << endl;   // 1행 전치 행렬
	cout << "data:\n" << mat1 << endl;
}

int main(void) {
	readData();
	return 0;
}