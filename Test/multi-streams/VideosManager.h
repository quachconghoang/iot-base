//
// Created by hoangqc on 02/02/2020.
//

#ifndef MULTICAMERA_VIDEOSMANAGER_H
#define MULTICAMERA_VIDEOSMANAGER_H

#include "opencv2/opencv.hpp"
#include "VideoSession.h"

class VideosManager {
public:
    VideosManager();
    ~VideosManager();
    void loadConfigFile(std::string filePath);
    void connectToCameras();

private:
    std::vector<VideoSession> m_sessions;
    std::vector<std::thread> m_threads;
    float m_fps_preview = 25;
    float m_fps_process = 1;
    float m_fps_of = 2;
    cv::Size m_size_prev;
    cv::Size m_size_proc;
};


#endif //MULTICAMERA_VIDEOSMANAGER_H
