//
// Created by hoangqc on 02/02/2020.
//

#ifndef MULTICAMERA_VIDEOSESSION_H
#define MULTICAMERA_VIDEOSESSION_H

#include "opencv2/opencv.hpp"
#include <thread>
#include <chrono>
#include <atomic>

#define RAW_IMG_WIDTH 1920
#define RAW_IMG_HEIGHT 1080
#define PROC_IMG_WIDTH 640
#define PROC_IMG_HEIGHT 360

// INTERVAL TIME in Milliseconds
#define CAPTURE_INTERVAL_TIME 30
#define QUEUEING_INTERVAL_TIME 1000

struct IPCamInfo
{
    std::string protocol;
    std::string id;
    std::string psw;
    std::string location;
};

enum VideoStatus
{
    VS_CLOSED = 0,
    VS_OPENED = 1,
    VS_CLOSING = 2
};

extern std::vector<VideoStatus> __globVideoThreads; // OLD BUT GOLD T_T

class VideoSession {
public:
    VideoSession();
    ~VideoSession();

    cv::Ptr<cv::cudacodec::VideoReader> nvCap;

    void setCamInfo(IPCamInfo & _info);
    void setSessionID(int id);
    IPCamInfo getInfo();
    void captureFrames();

    cv::Mat h_Img;
    cv::Mat img_proc;
    cv::Mat img_prev;

protected:


private:
    IPCamInfo m_info;
    int m_id;
    int64 m_sample_tick;

    void getSampling(cv::Mat & _img);

    cv::Ptr<cv::cuda::Stream> m_stream;
    cv::Ptr<cv::cuda::GpuMat> d_RawImg;
    cv::Ptr<cv::cuda::GpuMat> d_ProcImg;

};


#endif //MULTICAMERA_VIDEOSESSION_H
