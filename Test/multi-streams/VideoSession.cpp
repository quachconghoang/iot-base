//
// Created by hoangqc on 02/02/2020.
//

#include "VideoSession.h"

std::vector<VideoStatus> __globVideoThreads;

VideoSession::VideoSession()
{
// Alloc Memory
    d_RawImg = new cv::cuda::GpuMat(RAW_IMG_HEIGHT, RAW_IMG_WIDTH, CV_8UC4);
    d_ProcImg = new cv::cuda::GpuMat(PROC_IMG_HEIGHT, PROC_IMG_WIDTH, CV_8UC4);
    h_Img = cv::Mat(PROC_IMG_HEIGHT, PROC_IMG_WIDTH, CV_8UC4);
    m_stream = new cv::cuda::Stream();
}

VideoSession::~VideoSession(){}

void VideoSession::setCamInfo(IPCamInfo & _info) { m_info = _info; }
void VideoSession::setSessionID(int id) { m_id = id;}
IPCamInfo VideoSession::getInfo() { return  m_info; }

void VideoSession::captureFrames() {
    std::string input = m_info.protocol + m_info.id + ":" + m_info.psw + "@" + m_info.location;
    std::cout << "Open: " << input << std::endl;
    nvCap = cv::cudacodec::createVideoReader(input);

    __globVideoThreads[m_id] = VS_OPENED;

    while (!(__globVideoThreads[m_id] == VS_CLOSING))
    {
        if(nvCap->nextFrame(*d_RawImg, *m_stream)){
            cv::cuda::resize(*d_RawImg, *d_ProcImg,  cv::Size(PROC_IMG_WIDTH, PROC_IMG_HEIGHT), 0 ,0 , cv::INTER_NEAREST, *m_stream);
            d_ProcImg->download(h_Img, *m_stream);
        }else{
            std::cout << "No GPU frame" << std::endl;
        }
//        std::cout << m_id << " ... RUNNING ... " << __globVideoThreads[m_id] << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(CAPTURE_INTERVAL_TIME));
    }

    nvCap.release();
    std::cout << m_id << " ... CLOSED ... \n";
}