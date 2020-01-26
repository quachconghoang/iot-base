#include "opencv2/opencv.hpp"
cv::cudacodec::VideoReader * nvCap;

int main()
{
    cv::cuda::setDevice(0);
    cv::VideoCapture vCap;
    cv::Mat image;

    std::string command = "rtsp://admin:123@Abc.@192.168.1.136:554/Streaming/Channels/101/";
//    command = "/home/hoangqc/star_wars_1080p.mp4";

    cv::Ptr<cv::cudacodec::VideoReader> nvCap = cv::cudacodec::createVideoReader(command);

    cv::cuda::GpuMat img1, img2;

    while(true)
    {
        nvCap->nextFrame(img1);
        img1.download(image);
        cv::resize(image,image,cv::Size(960,540));
        cv::imshow("Output Window", image);
        if(cv::waitKey(1) >= 0) break;
    }

//    vCap.open(command);
//    const std::string n = vCap.getBackendName();
//    while (true)
//    {
//        if(!vCap.read(image)) {
//            std::cout << "No frame" << std::endl;
//            cv::waitKey();
//        }
//        cv::resize(image,image,cv::Size(640,360));
//        cv::imshow("Output Window", image);
//
//        if(cv::waitKey(1) >= 0) break;
//    }
//    vCap.release();
    cv::destroyAllWindows();
    return 0;
}