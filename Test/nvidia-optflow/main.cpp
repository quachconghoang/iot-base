#include "opencv2/opencv.hpp"


int main()
{
    std::string ip = "192.168.100.13";
    cv::VideoCapture vCap;
    cv::Mat image;

    std::string command = "rtsp://admin:123@Abc.@192.168.100.13:554/Streaming/Channels/101/";

    //    cv::cuda::GpuMat img1, img2;
//    cv::cudacodec::VideoReader * nvCap = cv::cudacodec::createVideoReader(command);
//    while(true)
//    {
//        nvCap->nextFrame(img1);
//        img1.download(image);
//        cv::resize(image,image,cv::Size(640,360));
//        cv::imshow("Output Window", image);
//        if(cv::waitKey(1) >= 0) break;
//    }

    vCap.open(command);

    const std::string n = vCap.getBackendName();
    while (true)
    {
        if(!vCap.read(image)) {
            std::cout << "No frame" << std::endl;
            cv::waitKey();
        }
        cv::resize(image,image,cv::Size(640,360));
        cv::imshow("Output Window", image);

        if(cv::waitKey(1) >= 0) break;
    }
    vCap.release();
    cv::destroyAllWindows();
    return 0;
}