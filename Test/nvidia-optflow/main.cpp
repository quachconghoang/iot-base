#include "opencv2/opencv.hpp"
cv::cudacodec::VideoReader * nvCap;

int main()
{
    cv::cuda::setDevice(0);
    cv::VideoCapture vCap;
    cv::Mat image;
    cv::cuda::GpuMat img1, img2;

    std::string command = "rtsp://admin:123@Abc.@192.168.1.136:554/Streaming/Channels/101/";
//    command = "/home/hoangqc/star_wars_1080p.mp4";

    cv::Ptr<cv::cudacodec::VideoReader> nvCap = cv::cudacodec::createVideoReader(command);
//    vCap.open(command);

    while(true)
    {
        if(!nvCap->nextFrame(img1)) {
            std::cout << "No GPU frame" << std::endl;
            if(cv::waitKey(30) >= 0) break;
        }else{
            img1.download(image);
            cv::resize(image,image,cv::Size(960,540));
            cv::imshow("GPU Output Window", image);
            if(cv::waitKey(30) >= 0) break;
        }
//        if(!vCap.read(image)){
//            std::cout << "No CPU frame" << std::endl;
//            cv::waitKey(30);
//        }
//        else{
//            cv::resize(image,image,cv::Size(960,540));
//            cv::imshow("CPU Output Window", image);
//            if(cv::waitKey(1) >= 0) break;
//        }

    }
//    vCap.release();
    nvCap.release();

    cv::destroyAllWindows();
    return 0;
}