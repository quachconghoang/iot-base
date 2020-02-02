//
// Created by hoangqc on 02/02/2020.
//

#include "VideosManager.h"

VideosManager::VideosManager() {

}

void VideosManager::loadConfigFile(std::string filePath) {
    cv::FileStorage fs(filePath, 0);

    IPCamInfo tInfo;
    tInfo.protocol = std::string(fs["protocol"]);
    tInfo.id = std::string(fs["user-id"]);
    tInfo.psw = std::string(fs["user-pwd"]);

    cv::FileNode tLocations = fs["locations"];
    for (int i = 0; i < tLocations.size(); i++) {
        tInfo.location = std::string(tLocations[i]);
        VideoSession tSession;
        tSession.setCamInfo(tInfo);
        tSession.sessionID = std::to_string(i);
        m_sessions.push_back(tSession);
    }

//    std::string vInput = vProtocol + vUsrName + ":" + vUsrPsw + "@" + vIP;
}

void VideosManager::connectToCameras() {
    int numThreads = m_sessions.size();
    m_threads.resize(numThreads);

    for (int i = 0; i < numThreads; ++i) {
        m_sessions[i].startSession();
        // LOOP ...
//        m_threads[i] = std::thread(&VideoSession::loop, m_sessions[i]);
//        m_threads.push_back(th);
    }

    for (int i = 0; i < numThreads; ++i) {
        m_threads[i].join();
    }
}

VideosManager::~VideosManager() {

}