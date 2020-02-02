//
// Created by hoangqc on 02/02/2020.
//

#include "VideoSession.h"

VideoSession::VideoSession(){

}

VideoSession::~VideoSession(){}

void VideoSession::setCamInfo(IPCamInfo & _info) {
    info = _info;
}

void VideoSession::startSession() {
    std::string input = info.protocol + info.id + ":" + info.psw + "@" + info.location;
    std::cout << "Open: " << input << std::endl;
//    nvCap = cv::cudacodec::createVideoReader(input);
}

void VideoSession::loop() {
//    while (!needClosing)
//    {
//        std::cout<< "Looping ... " << "" << std::endl;
//    }
    for(int i=0;  i< 100; i++)
    {
        std::cout<< sessionID << ":Looping ... " << i << std::endl;
    }
}

void VideoSession::callStopSession() {
    needClosing = true;
//    nvCap.release();
}