#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
//#include "cameraManager.h"
#include "opencv2/opencv.hpp"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

public slots:
    void setCameraIP();
    void dipslayCameraIP();


private:
    Ui::MainWindow *ui;

    cv::VideoCapture vCap;
    cv::Ptr<cv::cudacodec::VideoReader> nvCap;
    cv::cuda::GpuMat m_img1;
    cv::Mat m_displayImg;
    QImage m_qImg;
    QTimer * m_timer_video;

//    CameraManager m_cam;
    void setupDefault();
    void setupVideoCap();

};

#endif // MAINWINDOW_H
