#include "opencv2/opencv.hpp"
#include "VideosManager.h"
//#include "NvInfer.h"

int main()
{
    cv::cuda::setDevice(0);

    std::string filePath = std::string(getenv("HOME")) + "/IP_Camera.json";

    VideosManager videoManager;
    videoManager.loadConfigFile(filePath);
    videoManager.connectToCameras();

    return 0;
}