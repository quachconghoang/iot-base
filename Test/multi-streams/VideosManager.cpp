//
// Created by hoangqc on 02/02/2020.
//

#include "VideosManager.h"
#include <functional>

VideosManager::VideosManager() {

}

void VideosManager::loadConfigFile(std::string filePath) {
    cv::FileStorage fs(filePath, 0);

    IPCamInfo tInfo;
    tInfo.protocol = std::string(fs["protocol"]);
    tInfo.id = std::string(fs["user-id"]);
    tInfo.psw = std::string(fs["user-pwd"]);

    cv::FileNode tLocations = fs["locations"];
    int num_sessions = tLocations.size();
    threads_video.resize(num_sessions);
    __globVideoThreads.resize(num_sessions);

    for (int i = 0; i < tLocations.size(); i++) {
        tInfo.location = std::string(tLocations[i]);
        VideoSession tSession;
        tSession.setCamInfo(tInfo);
        tSession.setSessionID(i);
        sessions.push_back(tSession);
    }
}

void VideosManager::connectToCameras() {
    int numThreads = sessions.size();
    for (int i = 0; i < numThreads; ++i) {
        threads_video[i] = std::thread(&VideoSession::captureFrames, sessions[i]);
    }
}

void VideosManager::disconnect()
{
    for (int i = 0; i < threads_video.size(); ++i)
        __globVideoThreads[i] = VS_CLOSING;

    for (int i = 0; i < threads_video.size(); ++i)
    {
        if(threads_video[i].joinable())
            threads_video[i].join();
    }
}

bool VideosManager::checkVideosStatus() {
    bool all_opened = true;
    for (int i=0; i < threads_video.size(); i++){
//        std::cout << i << "Status: " << (__globVideoThreads[i] == VS_OPENED) << std::endl;
        all_opened = all_opened && (__globVideoThreads[i] == VS_OPENED);
    }
    return all_opened;
}

VideosManager::~VideosManager() {
    cv::getTickCount();
}