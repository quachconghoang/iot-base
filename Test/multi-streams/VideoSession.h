//
// Created by hoangqc on 02/02/2020.
//

#ifndef MULTICAMERA_VIDEOSESSION_H
#define MULTICAMERA_VIDEOSESSION_H

#include "opencv2/opencv.hpp"
#include <thread>

struct IPCamInfo
{
    std::string protocol;
    std::string id;
    std::string psw;
    std::string location;
};

class VideoSession {
public:
    VideoSession();
    ~VideoSession();

    cv::Ptr<cv::cudacodec::VideoReader> nvCap;
    std::string sessionID;
    void setCamInfo(IPCamInfo & _info);
    void startSession();
    void loop();
    void callStopSession();


protected:
    IPCamInfo info;

private:
    bool needClosing = false;
    cv::cuda::Stream m_stream;
    cv::cuda::GpuMat rawImg;
    cv::cuda::GpuMat procImg;

};


#endif //MULTICAMERA_VIDEOSESSION_H
