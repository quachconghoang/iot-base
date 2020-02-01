#include "opencv2/opencv.hpp"

int main()
{
    cv::Mat image;
    std::string command = "rtsp://admin:1234Abc.@192.168.1.117:554/Streaming/Channels/101/";
    cv::VideoCapture vCap;
//    vCap.open(command);
    vCap.open("rtspsrc location=rtsp://admin:1234Abc.@192.168.1.117:554/Streaming/Channels/101/ latency=300 ! \
                rtph265depay ! h265parse ! omxh265dec ! nvvidconv ! \
                video/x-raw, width=960, height=540, format=BGRx ! \
                videoconvert ! appsink", cv::CAP_GSTREAMER);
    while(true){
        if(!vCap.read(image)){
            std::cout << "No CPU frame";
        }else{
            cv::imshow("Jetson GSTreamer", image);
            if(cv::waitKey(30) >= 0) break;
        }
	}
//    std::cout<<vCap.getBackendName();
    vCap.release();
    cv::destroyAllWindows();
    return 0;
}
