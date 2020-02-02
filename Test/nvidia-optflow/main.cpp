#include "opencv2/opencv.hpp"
#include <thread>
#include <chrono>

bool needClose = false;

void loop(cv::Ptr<cv::cudacodec::VideoReader> nvCap, cv::Ptr<cv::cuda::GpuMat> img, cv::Ptr<cv::cuda::Stream> _Stream)
{
    while(!needClose) {
        if(!nvCap->nextFrame(*img, *_Stream)) {
            std::cout << "No GPU frame" << std::endl;
        }
//        else{
//            cv::cuda::resize(*img,*img, cv::Size(960,540),0,0, cv::INTER_LINEAR, _Stream);
//        }
        std::this_thread::sleep_for(std::chrono::milliseconds(30));
    }
}

int main()
{
//SETUP CONFIGS
    std::string filePath = std::string(getenv("HOME")) + "/IP_Camera.json";
    cv::FileStorage fs(filePath, 0);
    std::string vProtocol = fs["protocol"];
    std::string vIP = fs["locations"][0];
    std::string vUsrName = fs["user-id"];
    std::string vUsrPsw = fs["user-pwd"];
    std::string vInput = vProtocol + vUsrName + ":" + vUsrPsw + "@" + vIP;

    cv::cuda::setDevice(0);
    cv::Ptr<cv::cuda::Stream> stream0 = new cv::cuda::Stream();
    cv::Ptr<cv::cuda::Stream> stream1 = new cv::cuda::Stream();
    cv::Mat image0, image1;

    cv::Ptr<cv::cuda::GpuMat> img0 = new cv::cuda::GpuMat(1080,1920,CV_8UC4);
    cv::Ptr<cv::cuda::GpuMat> img1 = new cv::cuda::GpuMat(1080,1920,CV_8UC4);

    cv::Ptr<cv::cudacodec::VideoReader> nvCap0 = cv::cudacodec::createVideoReader(vInput);
    cv::Ptr<cv::cudacodec::VideoReader> nvCap1 = cv::cudacodec::createVideoReader(vInput);
    std::thread th1 = std::thread(loop, nvCap0, img0, stream0);
    std::thread th2 = std::thread(loop, nvCap1, img1, stream1);

    while (true)
    {
        img0->download(image0, *stream0);
        img1->download(image1, *stream1);
        cv::resize(image0,image0, cv::Size(960,540));
        cv::resize(image1,image1, cv::Size(960,540));
        cv::imshow("GPU 0", image0);
        cv::imshow("GPU 1", image1);
        if(cv::waitKey(30) >= 0)
        {
            needClose = true;
            break;
        }
    }

    th1.join();
    th2.join();
//    cv::Ptr<cv::cudacodec::VideoReader> nvCap0 = cv::cudacodec::createVideoReader(vInput);
//    cv::Ptr<cv::cudacodec::VideoReader> nvCap1 = cv::cudacodec::createVideoReader(vInput);
//    while(true) {
//        if(!nvCap0->nextFrame(img0, stream0)) {
//            std::cout << "No GPU frame" << std::endl;
//            if(cv::waitKey(30) >= 0) break;
//        }else{
//            cv::cuda::resize(img0,img0, cv::Size(960,540),0,0, cv::INTER_LINEAR, stream0);
//            img0.download(image0, stream0);
//            cv::imshow("GPU 0", image0);
//            if(cv::waitKey(30) >= 0) break;
//        }
//    }
//    nvCap0.release();
//    cv::destroyAllWindows();

    return 0;
}
