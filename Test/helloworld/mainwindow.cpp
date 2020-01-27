#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "qdebug.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setupDefault();
    setupVideoCap();
}

void MainWindow::setupDefault()
{
    ui->groupBox->setTitle("IP Camera Configs");
    connect(ui->pushButton,&QPushButton::clicked,this, &MainWindow::setCameraIP);
    m_qImg = QImage(480,270,QImage::Format_RGB888);
//    m_qImg.set
}

void MainWindow::setupVideoCap()
{
    std::string t_input = "rtsp://admin:123@Abc.@192.168.1.136:554/Streaming/Channels/101/";
    nvCap = cv::cudacodec::createVideoReader(t_input);
    m_timer_video = new QTimer(this);
    QObject::connect(m_timer_video, SIGNAL(timeout()), this, SLOT(dipslayCameraIP()));
    m_timer_video->start(30);
}


void MainWindow::setCameraIP()
{
//    qDebug() << ui->lineEdit_IP1->text();
//    qDebug() << ui->lineEdit_IP2->text();
//    qDebug() << ui->lineEdit_IP3->text();
//    qDebug() << ui->lineEdit_IP4->text();
    std::string t_IP = ui->lineEdit_IP1->text().toStdString();
    std::string t_Port = "544/Streaming/Channels/101/";
    std::string t_usr_psw = "admin:123@Abc.";
    std::string t_input = "rtsp://" + t_usr_psw + "@" + t_IP + ":" + t_Port;
    qDebug() << QString::fromStdString(t_input);
}

void MainWindow::dipslayCameraIP()
{
    if(!nvCap->nextFrame(m_img1)) {
        qDebug() << "No GPU frame";
    }else{
        m_img1.download(m_displayImg);
        cv::Mat temp;
        cv::resize(m_displayImg,m_displayImg,cv::Size(480,270));
        cvtColor(m_displayImg, temp,cv::COLOR_BGR2RGB);
        m_qImg = QImage((uchar*) temp.data, temp.cols, temp.rows, temp.step, QImage::Format_RGB888);
        ui->pre_cam_1->setPixmap(QPixmap::fromImage(m_qImg));
//        cv::imshow("GPU Output Window", m_displayImg);
//        cv::waitKey(1);
    }
}

MainWindow::~MainWindow()
{
    nvCap.release();
    m_timer_video->stop();
    cv::destroyAllWindows();
    delete ui;
}
