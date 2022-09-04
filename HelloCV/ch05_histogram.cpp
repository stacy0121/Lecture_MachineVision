#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

// �׷��̽����� ������ ������׷� ���ϱ�
Mat calcGrayHist(const Mat& img) {
	CV_Assert(img.type() == CV_8UC1);   // img ������ �׷��̽����� �������� �˻�

	Mat hist;
	int channels[] = { 0 };   // 0ä��
	int dims = 1;   // 1���� ���
	const int histSize[] = { 256 };
	float graylevel[] = { 0,256 };
	const float* ranges[] = { graylevel };

	calcHist(&img, 1, channels, noArray(), hist, dims, histSize, ranges);

	return hist;
}

// �׷��̽����� ������ ������׷� �׷��� �׸���
Mat getGrayHistImage(const Mat& hist) {
	CV_Assert(hist.type() == CV_32FC1);
	CV_Assert(hist.size() == Size(1, 256));

	double histMax;
	minMaxLoc(hist, 0, &histMax);

	// ���� ���� �׷���
	Mat imgHist(100, 256, CV_8UC1, Scalar(255));   // 256���� ��
	for (int i = 0; i < 256; i++) {
		line(imgHist, Point(i, 100),
			Point(i, 100 - cvRound(hist.at<float>(i, 0) * 100 / histMax)), Scalar(0));
	}

	return imgHist;
}

// ������׷� ��Ʈ��Ī
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

// ������׷� ��Ȱȭ
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
	//Mat hist = calcGrayHist(src);   // ������׷� ���� ���
	//Mat hist_img = getGrayHistImage(hist);   // ������׷� �׷��� ����

	//imshow("src", src);
	//imshow("hist_img", hist_img);
	//waitKey();

	histogram_equalization();
	return 0;
}