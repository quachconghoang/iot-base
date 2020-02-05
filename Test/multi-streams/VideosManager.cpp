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
    m_threads.resize(num_sessions);
    __globVideoThreads.resize(num_sessions);

    for (int i = 0; i < tLocations.size(); i++) {
        tInfo.location = std::string(tLocations[i]);
        VideoSession tSession;
        tSession.setCamInfo(tInfo);
        tSession.setSessionID(i);
        m_sessions.push_back(tSession);
    }
}

void VideosManager::connectToCameras() {
    int numThreads = m_sessions.size();
    for (int i = 0; i < numThreads; ++i) {
        m_threads[i] = std::thread(&VideoSession::captureFrames, m_sessions[i]);
    }
}

void VideosManager::disconnect() {

    for (int i = 0; i < m_threads.size(); ++i)
        __globVideoThreads[i] = VS_CLOSING;

    for (int i = 0; i < m_threads.size(); ++i)
    {
        if(m_threads[i].joinable())
            m_threads[i].join();
    }

    for (int i = 0; i < m_threads.size(); ++i)
        __globVideoThreads[i] = VS_CLOSED;

}

VideosManager::~VideosManager() {

}