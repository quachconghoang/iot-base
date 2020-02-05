#include "opencv2/opencv.hpp"
#include "VideosManager.h"
#include <atomic>
//#include "NvInfer.h"

int main()
{
    cv::cuda::setDevice(0);

    std::string filePath = std::string(getenv("HOME")) + "/IP_Camera.json";

    VideosManager videoManager;
    videoManager.loadConfigFile(filePath);
    videoManager.connectToCameras();

    while (true)
    {
        for (int i=0; i< videoManager.m_sessions.size(); i++)
        {
            if(__globVideoThreads[i] == VS_OPENED)
            {
                std::string nameW = std::to_string(i) + " Img";
                cv::imshow(nameW, videoManager.m_sessions[i].h_Img);
            }

        }
        if(cv::waitKey(30) >= 0)
        {
            break;
        }
    }
    cv::destroyAllWindows();
    videoManager.disconnect();
    std::cout<< "END GAME";

//    videoManager.loop();
    return 0;
}