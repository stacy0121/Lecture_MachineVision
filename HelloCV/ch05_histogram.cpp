#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// 그레이스케일 영상의 히스토그램 구하기
Mat calcGrayHist(const Mat& img) {
	CV_Assert(img.type() == CV_8UC1);   // img 영상이 그레이스케일 영상인지 검사

	Mat hist;
	int channels[] = { 0 };   // 0채널
	int dims = 1;   // 1차원 행렬
	const int histSize[] = { 256 };
	float graylevel[] = { 0,256 };
	const float* ranges[] = { graylevel };

	calcHist(&img, 1, channels, noArray(), hist, dims, histSize, ranges);

	return hist;
}

// 그레이스케일 영상의 히스토그램 그래프 그리기
Mat getGrayHistImage(const Mat& hist) {
	CV_Assert(hist.type() == CV_32FC1);
	CV_Assert(hist.size() == Size(1, 256));

	double histMax;
	minMaxLoc(hist, 0, &histMax);

	// 수직 막대 그래프
	Mat imgHist(100, 256, CV_8UC1, Scalar(255));   // 256개의 빈
	for (int i = 0; i < 256; i++) {
		line(imgHist, Point(i, 100),
			Point(i, 100 - cvRound(hist.at<float>(i, 0) * 100 / histMax)), Scalar(0));
	}

	return imgHist;
}

// 히스토그램 스트레칭
void histogram_stretching() {
	Mat src = imread("aero1.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	double gmin, gmax;
	minMaxLoc(src, &gmin, &gmax);

	Mat dst = (src - gmin) * 255 / (gmax - gmin);   // normalize

	imshow("src", src);
	imshow("srcHist", getGrayHistImage(calcGrayHist(src)));
	
	imshow("dst", dst);
	imshow("dstHist", getGrayHistImage(calcGrayHist(dst)));

	waitKey();
}

// 히스토그램 평활화
void histogram_equalization() {
	Mat src = imread("aero1.jpg", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image open failed!" << endl;
		return;
	}

	Mat dst;
	equalizeHist(src, dst);

	imshow("src", src);
	imshow("srcHist", getGrayHistImage(calcGrayHist(src)));
	
	imshow("dst", dst);
	imshow("dstHist", getGrayHistImage(calcGrayHist(dst)));

	waitKey();
}

int main(void) {
	//Mat src = imread("lena.jpg", IMREAD_GRAYSCALE);
	//Mat hist = calcGrayHist(src);   // 히스토그램 정보 행렬
	//Mat hist_img = getGrayHistImage(hist);   // 히스토그램 그래프 영상

	//imshow("src", src);
	//imshow("hist_img", hist_img);
	//waitKey();

	histogram_equalization();
	return 0;
}