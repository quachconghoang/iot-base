#include "opencv2/opencv.hpp"

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
    cv::VideoCapture vCap;
    cv::Mat image;
    cv::cuda::GpuMat img1, img2;
    cv::Ptr<cv::cudacodec::VideoReader> nvCap = cv::cudacodec::createVideoReader(vInput);

    while(true) {
        if(!nvCap->nextFrame(img1)) {
            std::cout << "No GPU frame" << std::endl;
            if(cv::waitKey(30) >= 0) break;
        }else{
            img1.download(image);
            cv::resize(image,image,cv::Size(960,540));
            cv::imshow("GPU Output Window", image);
            if(cv::waitKey(30) >= 0) break;
        }
    }
    nvCap.release();
    cv::destroyAllWindows();
    return 0;
}
