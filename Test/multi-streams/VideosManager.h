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
    void disconnect();

    std::vector<VideoSession> sessions;

protected:
    std::vector<std::thread> threads_video;

private:
    bool checkVideosStatus();
    float m_fps_preview = 25;
    float m_fps_process = 1;
    float m_fps_of = 2;

    int64 t1;
};

#endif //MULTICAMERA_VIDEOSMANAGER_H
