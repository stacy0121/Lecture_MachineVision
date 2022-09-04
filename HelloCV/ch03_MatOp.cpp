#include "opencv2/opencv.hpp"
#include <iostream>   // c++ 표준 출력을 위해

using namespace cv;   // cv:: 생략
using namespace std;
void MatOp7();

int main() {
	MatOp7();
	return 0;
}

// Mat 객체 생성
void MatOp1() {
	Mat img1;

	Mat img2(480, 640, CV_8UC1);
	Mat img3(480, 640, CV_8UC3);
	Mat img4(Size(640, 480), CV_8UC3);

	Mat img5(480, 640, CV_8UC1, Scalar(128));
	Mat img6(480, 640, CV_8UC3, Scalar(0, 0, 255));

	Mat mat1 = Mat::zeros(3, 3, CV_32FC1);
	Mat mat2 = Mat::ones(3, 3, CV_32FC1);
	Mat mat3 = Mat::eye(3, 3, CV_32FC1);   // 단위 행렬

	// 사용자 지정 원소
	float data[] = { 1, 2, 3, 4, 5, 6 };
	Mat mat4(2, 3, CV_32FC1, data);

	Mat mat5 = (Mat_<float>(2, 3) << 1, 2, 3, 4, 5, 6);
	Mat mat6 = Mat_<uchar>({ 2, 3 }, { 1, 2, 3, 4, 5, 6 });   // 초기화 리스트(크기, 초기값). 부호 없는 1바이트 정수 타입

	mat4.create(256, 256, CV_8UC3);   // 행렬 할당
	mat5.create(4, 4, CV_32FC1);

	// 초기화
	mat4 = Scalar(255, 0, 0);
	mat5.setTo(1.f);
}

// 행렬의 다양한 복사 방법
void MatOp2() {
	Mat img1 = imread("lena.jpg");

   // 얕은 복사
	Mat img2 = img1;
	Mat img3;
	img3 = img1;

	// 깊은 복사
	Mat img4 = img1.clone();
	Mat img5;
	img1.copyTo(img5);

	img1.setTo(Scalar(0, 255, 255));   // yellow

	imshow("img1", img1);
	imshow("img2", img2);
	imshow("img3", img3);
	imshow("img4", img4);
	imshow("img5", img5);

	waitKey();
}

// 영상의 부분 영상 반전하기
void MatOp3() {
	Mat img1 = imread("starry_night.jpg");

	if (img1.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	//Rect bounds(0, 0, img1.cols, img1.rows);
	//Rect r(220, 120, 340, 240); // partly outside
	//Mat roi = img1(r & bounds); // cropped to fit image
	// roi
	Mat img2 = img1(Rect(220, 120, 340, 240));   // 주소 공유(얕은 복사)
	Mat img3 = img1(Rect(220, 120, 340, 240)).clone();   // 깊은 복사

	img2 = ~img2;   // 반전
	imshow("img1", img1);
	imshow("img2", img2);
	imshow("img3", img3);

	waitKey();
}

//행렬의 원소 값 참조 방법을 이용하여 원소값 증가시키기
void MatOp4() {
	Mat mat1 = Mat::zeros(3, 4, CV_8UC1);

	for (int j = 0; j < mat1.rows;j++) {
		for (int i = 0; i < mat1.cols; i++) {
			mat1.at<uchar>(j, i)++;
		}
	}

	for (int j = 0; j < mat1.rows;j++) {
		uchar* p = mat1.ptr<uchar>(j);   // j번째 행의 시작 주소
		for (int i = 0; i < mat1.cols; i++) {
			p[i]++;   // (*(p+i))++
		}
	}

	// 반복자 클래스 사용
	// 행렬의 크기를 벗어나 발생하는 에러 방지
	for (MatIterator_<uchar> it = mat1.begin<uchar>(); it != mat1.end<uchar>(); ++it) {
		(*it)++;
	}

	cout << "mat:\n" << mat1 << endl;
}

// Mat 행렬 정보 참조하기
void MatOp5() {
	Mat img1 = imread("lena.jpg");

	cout << "Width: " << img1.cols << endl;
	cout << "Height: " << img1.rows << endl;
	cout << "Channels: " << img1.channels() << endl;

	if (img1.type() == CV_8UC1)
		cout << "img5 is a grayscale image." << endl;
	else if (img1.type() == CV_8UC3)
		cout << "img5 is a truecolor image." << endl;

	float data[] = { 2.f, 1.414f, 3.f, 1.732f };
	Mat mat1(2, 2, CV_32FC1, data);
	cout << "mat1:\n" << mat1 << endl;
}

// Mat 클래스를 이용한 간단한 행렬 연산
void MatOp6() {
	float data[] = { 1,1,2,3 };
	Mat mat1(2, 2, CV_32FC1, data);
	cout << "mat1:\n" << mat1 << endl;

	Mat mat2 = mat1.inv();   // 역행렬
	cout << "mat2:\n" << mat2 << endl;

	cout << "mat1.t():\n" << mat1.t() << endl;   // 전치 행렬
	cout << "mat1 + 3:\n" << mat1 + 3 << endl;
	cout << "mat1 + mat2:\n" << mat1 + mat2 << endl;
	cout << "mat1 * mat2:\n" << mat1 * mat2 << endl;
}

// 크기 및 타입 변환 함수 사용
void MatOp7() {
	Mat img1 = imread("lenna.jpg", IMREAD_GRAYSCALE);

	Mat img1f;
	img1.convertTo(img1f, CV_32FC1);   // 타입 변경. 곱할 값, 더할 값 없음

	uchar data1[] = { 1,2,3,4,5,6,7,8,9,10,11,12 };
	Mat mat1(3, 4, CV_8UC1, data1);
	Mat mat2 = mat1.reshape(0, 1);   // 채널 수 변경 없음. 한 행으로 변경

	cout << "mat1:\n" << mat1 << endl;
	cout << "mat2:\n" << mat2 << endl;
	
	Mat mat3 = Mat::ones(1, 4, CV_8UC1) * 255;
	mat1.push_back(mat3);   // 원소 데이터 추가(열 개수 같음)
	cout << "mat1:\n" << mat1 << endl;

	mat1.resize(6, 100);   // 6개 행으로 변경. 100으로 초기화
	cout << "mat1:\n" << mat1 << endl;
}